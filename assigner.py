from typing import List, Tuple

class TimeBox:
    """=== Attributes ===
    available:
        The list of people that are available for a given time
    time:
        The date and time of a given Timebox, written as a string
    """
    available: List[str]
    time: str

    def __init__(self):
        self.available = []
        self.time = ""
