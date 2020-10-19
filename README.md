# when2interview
Arranges interviews by scraping when2meet.  

when2meet.com is a great site for seeing when people are available. But arranging interviews / meeting times through this site is very tedious!  

We designed a program that would take care of this for you!

Make sure you have all the requirements downloaded. Create a ".env" text file, with the following line:  
  CHROME_DRIVER_PATH = "{Your path to your chromedriver}".  
  EX: CHROME_DRIVER_PATH="C:\Webdrivers\chromedriver.exe"  

Then run the "main.py" file in the source folder. Input your when2meet link, and the keyword that distinguishes your interviewers from the candidates, and watch the algorithm at work!  

# optimization  
This project is currently not optimized - it arranges interviews on a "most available" / "first-come first-serve" basis. In the future, we plan to implement it so that it arranges a roughly equal amount of interviews for each executive.
