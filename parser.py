from datetime import date, datetime

from models import ClanWarEntry, Coleader, Elder


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


def process_coleaders(participants: list[dict], coleaders: list[str], war_minimum: int) -> list[Coleader]:
    """Check war commitment for co-leaders specifically.
    Returns list of Coleader objects for each coleader."""
    parsed = []
    names = []
    for entry in coleaders:
        parts = entry.split()
        rank = int(parts[0:-1])
        member_name = parts[1]
        already_fulfilled = parts[2].lower() == '*'
        parsed.append((rank, member_name, already_fulfilled))
        names.append(member_name)

    commitment = check_war_commitment(participants, names, war_minimum)

    results = []
    for rank, member_name, already_fulfilled in parsed:
        fulfilled = already_fulfilled or commitment.get(member_name, False)
        results.append(
            Coleader(
                name=member_name,
                war_commitment_fulfilled=fulfilled,
                rank=rank,
            )
        )
    return results


def check_war_commitment(participants: list[dict], names: list[str], war_minimum: int) -> dict[str, bool]:
    """Check which members met the war minimum score. Returns {name: fulfilled}."""
    scores = {}
    for p in participants:
        scores[p["name"]] = p.get("fame", 0)

    commitment = {}
    for name in names:
        commitment[name] = scores.get(name, 0) >= war_minimum
    return commitment


def process_elders(participants: list[dict], elders: list[str], war_minimum: int) -> list[Elder]:
    """Check war commitment for elders specifically.
    Returns list of Elder objects for each elder."""
    parsed = []
    names = []
    for entry in elders:
        parts = entry.split()
        rank = int(parts[0:-1])
        member_name = parts[1]
        start_month = parts[2]
        parsed.append((rank, member_name, start_month))
        names.append(member_name)

    commitment = check_war_commitment(participants, names, war_minimum)

    results = []
    for rank, member_name, start_month in parsed:
        fulfilled = commitment.get(member_name, False)
        results.append(
            Elder(
                name=member_name,
                rank=rank,
                title_held_since=datetime(
                    datetime.today().year,
                    datetime.strptime(start_month, "%B").month,
                    1,
                ),
                candidate=fulfilled,
            )
        )
    return results
