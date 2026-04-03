import os
from dotenv import load_dotenv

from models import ClanWarEntry

load_dotenv()

CLAN_WAR_PATH = os.getenv("CLANWAR")
LEADERSHIP_PATH = os.getenv("LEADERSHIP")


def read_leadership() -> tuple[list[str], list[str]]:
    """Read co-leaders and elders from the leadership file."""
    coleaders = []
    elders = []
    current_section = None

    with open(LEADERSHIP_PATH, "r") as f:
        for line in f:
            stripped = line.strip()
            if not stripped:
                continue
            if stripped == "Co-Leaders:":
                current_section = "coleaders"
                continue
            if stripped == "Elders:":
                current_section = "elders"
                continue

            if current_section == "coleaders":
                coleaders.append(stripped)
            elif current_section == "elders":
                elders.append(stripped)

    return coleaders, elders


def append_war_log(entry: ClanWarEntry) -> None:
    """Append a war log entry to the clan war file."""
    with open(CLAN_WAR_PATH, "a") as f:
        f.write(entry.to_log_line())


def write_leadership(coleaders: list[str], elders: list[str]) -> None:
    """Overwrite the leadership file with updated lists."""
    with open(LEADERSHIP_PATH, "w") as f:
        f.write("Co-Leaders:\n")
        for name in coleaders:
            f.write(f"{name}\n")
        f.write("\nElders:\n")
        for name in elders:
            f.write(f"{name}\n")
