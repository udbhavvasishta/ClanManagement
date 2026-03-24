from dataclasses import dataclass

@dataclass
class Rules:
    war_minimum: int = 300
    max_inactivity: int = 7
    coleader_candidate_eligibility: int = 3
