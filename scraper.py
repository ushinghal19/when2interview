from selenium import webdriver
import time
from collections import OrderedDict 
from datetime import datetime
from dateutil import parser
from selenium.webdriver import ActionChains
from TimeBox import TimeBox
from Candidate import Candidate
from Exec import Exec
from dotenv import load_dotenv
import os
load_dotenv()

def scrapeData(path, website, keyword):
    """ Scrapes the data required from the when2meet file and returns a list of TimeBox objects """

    #Setting up the webdriver
    driver = webdriver.Chrome(path)

    #Setting up actions
    actions = ActionChains(driver)

    #Getting the when2meet link
    link = link

    #Opening the site
    driver.get(link)

    #Waiting for the site to load
    time.sleep(3)

    # Finding the table of data
    grid = driver.find_element_by_id("GroupGridSlots")

    # Finding the rows of the table
    list_of_rows = grid.find_elements_by_xpath(".//div[@style='font-size:0px;vertical-align:top;']")

    # Storing the data in a Python List
    python_grid = []

    for row in list_of_rows:
        boxes = []
        boxes.extend(row.find_elements_by_tag_name("div"))
        python_grid.append(boxes)

    # Dictionary of exec objects
    execs = {}

    # Dictionary of candidate objects
    candidates = {}

    # List of time boxes
    times = OrderedDict()

    for row in python_grid:
        for box in row:
            # Moves to box
            box.click()

            # Finds the date element
            date = driver.find_element_by_id("AvailableDate")

            # Finds the available element
            available = driver.find_element_by_id("Available")

            # Finds the unavailable element
            unavailable = driver.find_element_by_id("Unavailable")

            # Makes the available into a list
            available = available.text.split("\n")

            #Makes the unavailable into a list
            unavailable = unavailable.text.split("\n")

            # Local list of execs / candidates
            local_list_of_execs = []
            local_list_of_candidates = []

            #Creating global / local lists of executives and candidates
            for person in available:
                if keyword in person:
                    if person in execs:
                        execs[person].addAvailable(parser.parse(date.text))
                    else:
                        executive = Exec(person)
                        executive.addAvailable(parser.parse(date.text))
                        execs[person] = executive

                else:
                    if person in candidates:
                        candidates[person].addAvailable(parser.parse(date.text))
                    else:
                        candidate = Candidate(person)
                        candidate.addAvailable(parser.parse(date.text))
                        candidates[person] = candidate

            timebox = TimeBox(parser.parse(date.text))
            times[parser.parse(date.text)] = timebox
    
    # Adding the executive / candidate objects to the timeboxes.
    for executive in execs:
        for available_time in execs[executive].available_times:
            times[available_time].addExec(execs[executive])

    for candidate in candidates:
        for available_time in candidates[candidate].available_times:
            times[available_time].addCandidate(candidates[candidate])

# addPeopleToTimeBox(times, execs, candidates)

def bookInterview(candidate, execs, date):
    minimum = 500
    executive = None
    for executives in execs:
        if executives.num_interviews < minimum:
            executive = executives
    candidate.bookInterview(executive, date)
    executive.bookInterview(candidate, date)

def arrangeInterviews(times):
    for time in times:
        timebox = times[time]
        if timebox.getNumCandidates() == 0 or timebox.getNumExecs() == 0:
            continue
        else:
            for candidate in timebox.getCandidates():
                if candidate.booked == False:
                    bookInterview(candidate, timebox.getExecs(), timebox.date)
                else:
                    continue

arrangeInterviews(times)

for candidate in candidates:
    print(candidates[candidate].name + " " + str(candidates[candidate].interview))