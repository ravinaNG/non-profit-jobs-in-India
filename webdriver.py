from selenium import webdriver
from pprint import pprint
from LinkedIn_jobs import selecting_some_data
from LinkedIn_jobs import extract_source_data
import time

url = "https://in.linkedin.com/jobs/nonprofit-jobs?currentJobId=1797022549&position=1&pageNum=0"
driver = webdriver.Chrome(r"C:\Users\Ravina\Documents\non-profit-jobs\chromedriver_win32\chromedriver.exe")
driver.get(url)
SCROLL_PAUSE_TIME = 5

last_height = 0
while True:
    #Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculater new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    
    if new_height == last_height:
        break
    last_height = new_height

# print (driver)
data = extract_source_data(driver)
selected_data = selecting_some_data(data)
pprint (selected_data) 

