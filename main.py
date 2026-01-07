#!/usr/bin/env python3
"""
Main entry point for the Clan Management application.
"""

from api_requests import Requests

def main():
    """Main function."""
    requests = Requests()
    print("requests initialized")
    war_data = requests.get_war_data()
    print("war data fetched")
    print(war_data)


if __name__ == "__main__":
    main()
