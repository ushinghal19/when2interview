from TimeBox import TimeBox
from typing import *
from datetime import datetime
# from Candidate import Candidate

class Exec:
    """ Represents a single exec """

    name:str
    available_times: List
    interview_times: Dict
    num_interviews
    # candidates: List[Candidate]

    def __init__(self, name):
        self.available_times = []
        self.interview_times = {}
        self.num_interviews = 0

    def bookInterview(self, candidate, date):
        self.interview_times[date] = candidate
        num_interviews += 1
    
    def addAvailable(self, date):
        self.available_times.append(date)


    

