from dataclasses import dataclass

@dataclass
class Coleader:
    """Represents a co-leader with war commitment status and rank."""
    war_commitment_fulfilled: bool = False
    rank: int = 0