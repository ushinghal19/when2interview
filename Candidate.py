from TimeBox import TimeBox
from typing import *
from datetime import datetime
# from Exec import Exec

class Candidate:
    """ Represents a single candidate """

    name: str
    available_times: List[datetime]
    interview_time: datetime
    booked: bool
    # execs: List[Exec]

    def __init__(self, name):
        self.available_times = []
        self.interview_time = None
        self.booked = False
        self.execs = []

    def bookInterview(self, exec, date):
        self.execs.append(exec)
        self.meeting_time = date
        self.booked = True
    
    def addAvailable(self, date):
        self.available_times.append(date)


    

