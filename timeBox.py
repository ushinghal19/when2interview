from datetime import datetime
from dateutil import parser

parser.parse("Aug 28 1999 12:00AM")  # datetime.datetime(1999, 8, 28, 0, 0)
print(parser.parse("Aug 28 1999 12:00AM"))

class timeBox:
    """ Represents one box of time in the when2meet"""

    date: datetime
    available: list
    unavailable: list
    num_of_execs: int
    num_of_applicants: int

    def __init__(date, available, unavailable, execs, applicants):
        this.date = parser.parse(date)
        this.available = available
        this.unavailable = unavailable
        this.num_of_applicants = len(applicants)
        this.num_of_execs = len(execs)
