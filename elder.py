from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional

@dataclass
class Elder:
    rank: int
    title_held_since: datetime = None
    candidate: bool = False
    promotion_delay: int