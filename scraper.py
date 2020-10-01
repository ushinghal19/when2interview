from selenium import webdriver
import time
from selenium.webdriver import ActionChains

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


box1 = driver.find_element_by_id("GroupTime1595246400")
actions.move_to_element_with_offset(box1, 0, 0).click().perform()

date = driver.find_element_by_id("AvailableDate")

available = driver.find_element_by_id("Available")
unavailable = driver.find_element_by_id("Unavailable")

print(date.text)
print(available.text)
print(unavailable.text)
