from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from timeBox import timeBox

#ask "do you want me to set one meeting for everyone to attend,
# or do you want me to set a meeting with 2 cssu members and a
# non cssu members, for each non cssu member"

#ask how long each meeting should be
#Setting up the webdriver
driver = webdriver.Chrome()

#Setting up actions
actions = ActionChains(driver)

#Asking what sort of algorithm is required:


#Getting the names of the CSSU execs:
execs = ['Alex Kozin']

#The names of the applicants:
applicants = []

#Getting the when2meet link
link = "https://www.when2meet.com/?9397833-x1ZoE"

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

times = {}

for row in python_grid:
    for box in row:
        box.click()
        date = driver.find_element_by_id("AvailableDate")
        available = driver.find_element_by_id("Available")
        unavailable = driver.find_element_by_id("Unavailable")
        print("date = " + date.text)
        print("available = " + available.text)
        print("unavailable = " + unavailable.text)



