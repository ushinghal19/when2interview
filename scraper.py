from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from timeBox import timeBox

#Setting up the webdriver
driver = webdriver.Chrome()

#Setting up actions
actions = ActionChains(driver)

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

# print(list_of_rows)

python_grid = []

for row in list_of_rows:
    boxes = []
    boxes.extend(row.find_elements_by_tag_name("div"))
    python_grid.append(boxes)

times = {}

for row in python_grid:
    for box in row:
        actions.move_to_element_with_offset(box, 0, 0).click().perform()
        date = driver.find_element_by_id("AvailableDate")
        available = driver.find_element_by_id("Available")
        unavailable = driver.find_element_by_id("Unavailable")
        print("date = " + date.text)
        print("available = " + available.text)
        print("unavailable = " + unavailable.text)



# for row in grid:
#     list_of_boxes = row.find_elements_by_tag_name("div")    
#     python_grid.append(list_of_boxes)

# print(len(python_grid))

#actions.move_to_element_with_offset(box1, 0, 0).click().perform()

# date = driver.find_element_by_id("AvailableDate")
# available = driver.find_element_by_id("Available")
# unavailable = driver.find_element_by_id("Unavailable")

# t1 = timeBox(date=date.text, available=available.text, unavailable=unavailable.text, applicants=applicants, execs=execs)

# print(date.text)
# print(available.text)
# print(unavailable.text)

# print()
# print(date.text)
# print(available.text)
# print(unavailable.text)
