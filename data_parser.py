from datetime import date
import os

from file_writer import FileWriter
from file_reader import FileReader

class DataParser:
    def __init__(self, war_data, clan_tag, clan_trophies):
        self.war_data = war_data
        self.clan_tag = clan_tag
        self.clan_trophies = clan_trophies

    def parse_war_data(self):
        """Parse war data to extract relevant information."""
        trophy_change, participants = self.extract_clan_data()
        #self.log_trophy_change(trophy_change)
        self.parse_participants(participants)
        
    def extract_clan_data(self):
        """Extract and format clan data for display."""
        
        standings = self.war_data['items'][0]['standings']
        
        for clan in standings:
            if clan['clan']['tag'].replace('#', '%23') == self.clan_tag:
                trophy_change = clan['trophyChange']

                participants = clan['clan']['participants']

                return trophy_change, participants
    
    def log_trophy_change(self, trophy_change):
        month = date.today().month
        day = date.today().day
        date_str = date.today().strftime('%B %d')
        if month == 4 and day > 1 and day - 7 < 1:
            date_str += f", {date.today().year}"

        if trophy_change > 0:
            trophy_change = '+' + trophy_change

        log = f"{date_str}\t{self.clan_trophies}\t{trophy_change}\t{os.getenv('LEADER')}"

        if self.clan_trophies > int(os.getenv('PEAKTROPHIES')):
            os.environ['PEAKTROPHIES'] = str(self.clan_trophies)

            log += '\t\t*'
        
        log += '\n'
        
        FileWriter().update_clan_war_data(log)

    def parse_participants(self, participants):
        coleaders, elders = FileReader().read_clan_war_data()
        self.process_coleaders(coleaders, participants)
        
    def process_coleaders(self, coleaders):
        for coleader in coleaders:
            line = coleader.split()

            if line[-1] == '*':
