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
driver.get(link)

time.sleep(3)

box1 = driver.find_element_by_id("GroupTime1595246400")
actions.move_to_element(box1).build().perform()

# applicants = driver.find_element_by_id("Available").text
# print(applicants)
print("test")