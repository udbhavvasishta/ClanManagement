import os
import requests
from dotenv import load_dotenv

class Requests:
    def __init__(self):
        load_dotenv()
        self.headers = {"Authorization": f"Bearer {os.getenv('TOKEN')}"}

    def load_clan_data(self):
        url = "https://api.clashroyale.com/v1/clans/?name=Rao%20Gathering"
        clan_data = requests.get(url, headers=self.headers)
        if clan_data.status_code != 200:
            raise Exception(f"Clan data request failed with status code {clan_data.status_code}")
        clan_data = clan_data.json()['items'][0]
        self.clan_tag = clan_data['tag'].replace('#', '%23')
        return clan_data['clanWarTrophies']

    def get_war_data(self):
        url = f"https://api.clashroyale.com/v1/clans/{self.clan_tag}/riverracelog?limit=1"
        clan_data = requests.get(url, headers=self.headers).json()
        return clan_data