from TimeBox import TimeBox
from typing import *
from datetime import datetime
# from Candidate import Candidate

class Exec:
    """ Represents a single exec """

    name:str
    available_times: List
    interviews: Dict
    num_interviews: int
    # candidates: List[Candidate]

    def __init__(self, name):
        self.available_times = []
        self.interviews = {}
        self.num_interviews = 0
        self.name = name

    def bookInterview(self, candidate, date):
        self.interviews[date] = candidate
        self.num_interviews += 1
    
    def addAvailable(self, date):
        self.available_times.append(date)


    

