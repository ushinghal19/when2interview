from datetime import datetime
from dateutil import parser
from typing import *
# from Exec import Exec
# from Candidate import Candidate

class TimeBox:
    """ Represents one box of time in the when2meet"""

    date: datetime
    execs: List
    candidates: List
    num_of_execs: int
    num_of_applicants: int

    def __init__(self, date):
        self.date = date
        self.execs = []
        self.candidates = []
        self.num_of_execs = len(self.execs)
        self.num_of_candidates = len(self.candidates)

    def addExec(self, executive):
        self.execs.append(executive)

    def addCandidate(self, candidate):
        self.candidates.append(candidate)


