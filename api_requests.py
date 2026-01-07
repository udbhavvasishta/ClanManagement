import os
import requests
from dotenv import load_dotenv

class Requests:
    def __init__(self):
        load_dotenv()
        self.headers = {"Authorization": f"Bearer {os.getenv('TOKEN')}"}
    
    def get_war_data(self):
        url = "https://api.clashroyale.com/v1/clans/Rao Gathering/warlog"
        clan_data = requests.get(url, headers=self.headers).json()
        return clan_data