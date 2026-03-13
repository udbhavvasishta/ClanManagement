from dataclasses import dataclass

@dataclass
class Rule:
    id: int
    name: str
    description: str = ""
    active: bool = True
    priority: int = 0
    war_minimum: int = 300
    max_inactivity: int = 7