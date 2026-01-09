#!/usr/bin/env python3
"""
Main entry point for the Clan Management application.
"""

from api_requests import Requests

def main():
    """Main function."""
    requests = Requests()
    print("requests initialized")
    requests.load_clan_data()
    print(requests.clan_tag)
    print("clan data fetched")


if __name__ == "__main__":
    main()
