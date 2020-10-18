from selenium import webdriver
import time
from datetime import datetime
from dateutil import parser
from selenium.webdriver import ActionChains
from TimeBox import TimeBox
from Candidate import Candidate
from Exec import Exec
from dotenv import load_dotenv
import os
load_dotenv()

#Setting up the webdriver
driver = webdriver.Chrome(os.getenv('CHROME_DRIVER_PATH'))

#Setting up actions
actions = ActionChains(driver)

#Getting the when2meet link
link = "https://www.when2meet.com/?10117137-FRjsY"

#Opening the site
driver.get(link)

#Waiting for the site to load
time.sleep(3)


grid = driver.find_element_by_id("GroupGridSlots")
list_of_rows = grid.find_elements_by_xpath(".//div[@style='font-size:0px;vertical-align:top;']")

python_grid = []

for row in list_of_rows:
    boxes = []
    boxes.extend(row.find_elements_by_tag_name("div"))
    python_grid.append(boxes)

# time_boxes = []

# Dictionary of exec objects
execs = {}

# Dictionary of candidate objects
candidates = {}


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

        #Creating executives
        for person in available:
            if "CSSU" in person:
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

print(execs)
print(candidates)


# def algorithm(time_boxes):
#     for box in time_boxes:
#         if box.num_of_candidates == 0:
#             continue
#         elif box.num_of_execs == 0:
#             continue
#         else:
#             for candidate in box.candidates:
#                 if candidate.booked:
#                     continue
#                 else:

