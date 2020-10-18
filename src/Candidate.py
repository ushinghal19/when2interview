from TimeBox import TimeBox
from typing import *
from datetime import datetime
# from Exec import Exec

class Candidate:
    """ Represents a single candidate """

    name: str
    available_times: List
    interview: Dict
    booked: bool

    def __init__(self, name):
        self.name = name
        self.available_times = []
        self.interview = {}
        self.booked = False

    def book_interview(self, executive, date):
        self.interview[date] = executive.name
        self.booked = True

    def add_available(self, date):
        self.available_times.append(date)




