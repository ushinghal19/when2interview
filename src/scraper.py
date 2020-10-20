from selenium import webdriver
import time
from collections import OrderedDict
from datetime import datetime
from dateutil import parser
from selenium.webdriver import ActionChains
from TimeBox import TimeBox
from Candidate import Candidate
from Exec import Exec


def book_interview(candidate, execs, date):
    """ Books an interview between a candidate and exec at a certain date """

    minimum = 500
    executive = None
    for executives in execs:
        if executives.num_interviews < minimum:
            executive = executives
    candidate.book_interview(executive, date)
    executive.book_interview(candidate, date)


def arrange_interviews(times):
    """ Arranges interviews between candidates and execs """
    for time in times:
        timebox = times[time]
        if timebox.get_num_candidates() == 0 or timebox.get_num_execs() == 0:
            continue
        else:
            for candidate in timebox.get_candidates():
                if candidate.booked == False:
                    book_interview(candidate, timebox.get_execs(), timebox.date)
                else:
                    continue

def scrape_data(path, website, keyword):
    """ Scrapes data from the when2meet link, and returns a list of TimeBox objects """

    # Setting up the webdriver
    driver = webdriver.Chrome(path)

    # Setting up actions
    actions = ActionChains(driver)

    # Getting the when2meet link
    link = website

    # Opening the site
    driver.get(link)
    #driver.minimize_window()


    # Waiting for the site to load
    time.sleep(3)

    # Finding the table of data
    grid = driver.find_element_by_id("GroupGridSlots")

    # Finding the rows of the table
    list_of_rows = grid.find_elements_by_xpath(
        ".//div[@style='font-size:0px;vertical-align:top;']")

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

            # Makes the unavailable into a list
            unavailable = unavailable.text.split("\n")

            for person in available:
                if keyword in person:
                    if person in execs:
                        execs[person].add_available(parser.parse(date.text))     # Adding this time as available to the exec's list of available times
                    else:
                        executive = Exec(person)                                 # Creating a new exec object
                        executive.add_available(parser.parse(date.text))         # Adding this as an available time
                        execs[person] = executive                                # Storing them in the dictionary

                else:
                    if person in candidates:                            
                        candidates[person].add_available(parser.parse(date.text)) # Adding this time as available to the candidate's list of available times                   

                    else:
                        candidate = Candidate(person)                             # Creating a new candidate object
                        candidate.add_available(parser.parse(date.text))          # Adding this as an available time
                        candidates[person] = candidate                            # Storing them in the dictionary

            timebox = TimeBox(parser.parse(date.text))                            # Creating a new timebox object with given date
            times[parser.parse(date.text)] = timebox                              # Storing the timebox in the dictionary with the date as the key

    for executive in execs:                                                       # Storing the exec objects in the timebox objects
        for available_time in execs[executive].available_times:
            times[available_time].add_exec(execs[executive])

    for candidate in candidates:                                                  # Storing the candidate objects in the timebox objects
        for available_time in candidates[candidate].available_times:
            times[available_time].add_candidate(candidates[candidate])


    # Arranging the interviews
    arrange_interviews(times)

    # Minimizing the chrome window
    driver.close()

    # Printing the results
    for candidate in candidates:
        print(candidates[candidate].name + " " + str(candidates[candidate].interview))
