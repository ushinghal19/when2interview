from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from TimeBox import TimeBox
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

time_boxes = []

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

        #Finds the people who are execs (Have CSSU in their name)
        available_execs = [person for person in available if "CSSU" in person]

        available_candidates = [person for person in available if not "CSSU" in person]

        # print(date.text)
        # print("Execs = " + str(available_execs))
        # print("Candidates = " + str(available_candidates))
        # print()

        time_boxes.append(TimeBox(date.text, available_execs, available_candidates))

print(time_boxes[0].date)
print(time_boxes[0].execs)
print(time_boxes[0].candidates)
