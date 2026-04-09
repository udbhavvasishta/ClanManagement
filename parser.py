from datetime import date

from models import ClanWarEntry


def extract_clan_standings(war_data: dict, clan_tag: str) -> tuple[int, list[dict]]:
    """Extract trophy change and participants for our clan from war standings."""
    standings = war_data["items"][0]["standings"]
    for clan in standings:
        if clan["clan"]["tag"].replace("#", "%23") == clan_tag:
            return clan["trophyChange"], clan["clan"]["participants"]
    raise ValueError(f"Clan {clan_tag} not found in war standings")


def build_war_log_entry(
    trophy_change: int,
    clan_trophies: int,
    leader: str,
    peak_trophies: int,
) -> ClanWarEntry:
    """Build a war log entry from the latest war results."""
    today = date.today()
    date_str = today.strftime("%B %d")

    # Add year marker at the start of each April (first week)
    if today.month == 4 and today.day <= 7:
        date_str += f", {today.year}"

    return ClanWarEntry(
        date_str=date_str,
        trophies=clan_trophies,
        trophy_change=trophy_change,
        leader=leader,
        is_peak=clan_trophies > peak_trophies,
    )


def check_war_commitment(participants: list[dict], names: list[str], war_minimum: int) -> dict[str, bool]:
    """Check which members met the war minimum score. Returns {name: fulfilled}."""
    scores = {p["name"]: p.get("fame", 0) for p in participants}
    return {name: scores.get(name, 0) >= war_minimum for name in names}
