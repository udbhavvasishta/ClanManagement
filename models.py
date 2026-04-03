from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Rules:
    war_minimum: int = 300
    max_inactivity: int = 7
    coleader_candidate_eligibility: int = 3


@dataclass
class Coleader:
    name: str
    war_commitment_fulfilled: bool = False
    rank: int = 0


@dataclass
class Elder:
    name: str
    rank: int = 0
    title_held_since: Optional[datetime] = None
    candidate: bool = False
    promotion_delay: int = 0


@dataclass
class ClanWarEntry:
    date_str: str
    trophies: int
    trophy_change: int
    leader: str
    is_peak: bool = False

    def to_log_line(self) -> str:
        change_str = f"+{self.trophy_change}" if self.trophy_change > 0 else str(self.trophy_change)
        line = f"{self.date_str}\t{self.trophies}\t{change_str}\t{self.leader}"
        if self.is_peak:
            line += "\t\t*"
        return line + "\n"
