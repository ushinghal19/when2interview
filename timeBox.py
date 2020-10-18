from datetime import datetime
from dateutil import parser
from typing import *

class TimeBox:
    """ Represents one box of time in the when2meet"""

    date: datetime
    execs: List[str]
    candidates: List[str]
    num_of_execs: int
    num_of_applicants: int

    def __init__(self, date, execs, candidates):
        self.date = parser.parse(date)
        self.execs = execs
        self.candidates = candidates
        self.num_of_execs = len(self.execs)
        self.num_of_candidates = len(self.candidates)
