import os
import requests
from dotenv import load_dotenv


class ClashApiClient:
    BASE_URL = "https://api.clashroyale.com/v1"

    def __init__(self):
        load_dotenv()
        self.headers = {"Authorization": f"Bearer {os.getenv('TOKEN')}"}
        self.clan_tag = self._resolve_clan_tag()

    def _resolve_clan_tag(self) -> str:
        url = f"{self.BASE_URL}/clans/?name=Rao%20Gathering"
        resp = requests.get(url, headers=self.headers)
        resp.raise_for_status()
        clan = resp.json()["items"][0]
        return clan["tag"].replace("#", "%23")

    def get_clan_trophies(self) -> int:
        url = f"{self.BASE_URL}/clans/{self.clan_tag}"
        resp = requests.get(url, headers=self.headers)
        resp.raise_for_status()
        return resp.json()["clanWarTrophies"]

    def get_latest_war(self) -> dict:
        url = f"{self.BASE_URL}/clans/{self.clan_tag}/riverracelog?limit=1"
        resp = requests.get(url, headers=self.headers)
        resp.raise_for_status()
        return resp.json()
