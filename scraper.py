from selenium import webdriver
import time

#Setting up the webdriver
driver = webdriver.Chrome()

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