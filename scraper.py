from selenium import webdriver
import time
#first get the when2meet link from the user

#ask "do you want me to set one meeting for everyone to attend,
# or do you want me to set a meeting with 2 cssu members and a
# non cssu members, for each non cssu member"

#ask how long each meeting should be
#Setting up the webdriver
driver = webdriver.Chrome('C:/Users/eklut/.wdm/drivers/chromedriver/win32/84'
                          '.0.4147.30/chromedriver.exe')

#Getting the names of the CSSU execs:
execs = ['Alex Kozin']

#The names of the applicants:
applicants = []

#Getting the when2meet link
link = "https://www.when2meet.com/?9397833-x1ZoE"
driver.get(link)

box1 = driver.find_element_by_id("GroupTime1595246400")

hover = driver.move_to_element(box1)
hover.perform()
