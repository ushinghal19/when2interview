from dotenv import load_dotenv
import scraper
import os
load_dotenv()

path = os.getenv('CHROME_DRIVER_PATH')
link = input('Enter your when2meet link here: ')
keyword = input('Enter your keyword here (Ex: CSSU): ')

scrape_data(path, link, keyword)



