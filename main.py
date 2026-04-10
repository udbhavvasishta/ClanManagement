#!/usr/bin/env python3
"""
Clan Management — fetches war data from the Clash Royale API,
logs trophy changes, and tracks leadership war commitment.
"""

import json
from dotenv import load_dotenv

from api_client import ClashApiClient
from parser import extract_clan_standings, build_war_log_entry, check_war_commitment
from file_io import read_leadership, append_war_log
from models import Rules

load_dotenv()


def main():
    rules = Rules()

    # Fetch data from the API
    client = ClashApiClient()
    print("Loading clan data...")
    trophies = client.get_clan_trophies()
    print(f"Current war trophies: {trophies}")

    print("Fetching latest war...")
    war_data = client.get_latest_war()

    # Parse war results
    trophy_change, participants = extract_clan_standings(war_data, client.clan_tag)
    print(f"Trophy change: {'+' if trophy_change > 0 else ''}{trophy_change}")

    # Log the war result
    with open("stats.json") as f:
        stats = json.load(f)
    peak_trophies = stats["PEAKTROPHIES"]
    entry = build_war_log_entry(trophy_change, trophies, stats["LEADER"], peak_trophies)
    append_war_log(entry)
    print(f"War log updated: {entry.date_str}")

    if entry.is_peak:
        print(f"New peak trophies: {trophies}")
        stats["PEAKTROPHIES"] = trophies
        with open("stats.json", "w") as f:
            json.dump(stats, f, indent=4)

    # Check war commitment for co-leaders and elders
    coleaders, elders = read_leadership()
    all_names = coleaders + elders
    commitment = check_war_commitment(participants, all_names, rules.war_minimum)

    for name, fulfilled in commitment.items():
        status = "met" if fulfilled else "DID NOT meet"
        print(f"  {name}: {status} war minimum ({rules.war_minimum})")


if __name__ == "__main__":
    main()
