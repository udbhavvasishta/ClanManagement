#!/usr/bin/env python3
"""
Main entry point for the Clan Management application.
"""

from api_requests import Requests
from data_parser import DataParser

def main():
    """Main function."""
    requests = Requests()
    print("Loading clan data...")
    trophies = requests.load_clan_data()
    print("Fetching war data...")
    war_data = requests.get_war_data()

    parser = DataParser(war_data, requests.clan_tag, trophies)
    print(parser.extract_clan_data())

if __name__ == "__main__":
    main()
