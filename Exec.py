from TimeBox import TimeBox
from typing import *
from datetime import datetime
# from Candidate import Candidate

class Exec:
    """ Represents a single exec """

    name:str
    available_times: List[datetime]
    interview_time: datetime
    booked: bool
    # candidates: List[Candidate]

    def __init__(self, name):
        self.available_times = []
        self.interview_time = None
        self.booked = False
        self.candidates = []

    def bookInterview(self, exec, date):
        self.execs.append(exec)
        self.meeting_time = date
        self.booked = True
    
    def addAvailable(self, date):
        self.available_times.append(date)


    

