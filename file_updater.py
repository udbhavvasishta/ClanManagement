import os

class FileUpdater:
    def update_clan_war_data(self, data):
        clan_war = os.getenv('CLANWAR')
        with open(clan_war, 'a') as file:
            file.write(data)

    def update_leadership_data(self, data):
        with open(self.leadership, 'w') as file:
            file.write(data)