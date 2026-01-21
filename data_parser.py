class DataParser:
    def __init__(self, war_data, clan_tag):
        self.war_data = war_data
        self.clan_tag = clan_tag

    def parse_war_data(self):
        """Parse war data to extract relevant information."""
        war_data = self.extract_clan_data()
        
    def extract_clan_data(self):
        """Extract and format clan data for display."""
        
        standings = self.war_data['items'][0]['standings']
        
        for clan in standings:
            if clan['clan']['tag'].replace('#', '%23') == self.clan_tag:
                trophy_change = clan['trophyChange']

                participants = clan['clan']['participants']

                return participants
    
    def parse_participants(self):
        
