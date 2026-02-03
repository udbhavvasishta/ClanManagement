import os

class FileWriter:
    def update_clan_war_data(self, data):
        clan_war = os.getenv('CLANWAR')
        with open(clan_war, 'a') as file:
            file.write(data)

    def update_leadership_data(self, data):
        leadership = os.getenv('LEADERSHIP')
        with open(leadership, 'w') as file:
            file.write(data)