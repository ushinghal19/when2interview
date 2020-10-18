from datetime import datetime
from dateutil import parser
from typing import *

class TimeBox:
    """ Represents one box of time in the when2meet"""

    date: datetime
    execs: List
    candidates: List
    num_of_execs: int
    num_of_candidates: int

    def __init__(self, date):
        self.date = date
        self.execs = []
        self.candidates = []
        self.num_of_execs = 0
        self.num_of_candidates = 0

    def add_exec(self, executive):
        self.execs.append(executive)
        self.num_of_execs += 1

    def add_candidate(self, candidate):
        self.candidates.append(candidate)
        self.num_of_candidates += 1

    def get_num_candidates(self):
        return self.num_of_candidates

    def get_num_execs(self):
        return self.num_of_execs

    def get_candidates(self):
        return self.candidates

    def get_execs(self):
        return self.execs
