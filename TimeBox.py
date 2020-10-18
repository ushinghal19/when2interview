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

    def addExec(self, executive):
        self.execs.append(executive)
        self.num_of_execs += 1

    def addCandidate(self, candidate):
        self.candidates.append(candidate)
        self.num_of_candidates += 1

    def getNumCandidates(self):
        return self.num_of_candidates
    
    def getNumExecs(self):
        return self.num_of_execs
    
    def getCandidates(self):
        return self.candidates
    
    def getExecs(self):
        return self.execs
