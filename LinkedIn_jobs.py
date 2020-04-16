import requests # python module for sending all kind of http requests.
from bs4 import BeautifulSoup # python librery to pull out data from 
import html5lib # pure python library for parshing html
from pprint import pprint # "pretty print" is for data structures in a well-formate and in more readable way

# url = "https://www.naukri.com/non-profit-jobs"
linkedIn = "https://in.linkedin.com/jobs/nonprofit-jobs?currentJobId=1797022549&position=1&pageNum=0"

def extract_source_data(source):
    # source = requests.get(linkedIn).text
    extract_data = BeautifulSoup(source, "html5lib") 
    return extract_data

def selecting_some_data(whole_data):
    main_data = {}
    home_page = whole_data.find('div', {'class':'results__container results__container--two-pane'})
    job_link_list = home_page.findAll('a', {'class':'result-card__full-card-link'})
    numbe_of_job = 1
    for job in job_link_list:
        jobs = {}
        post = job.text
        url = job['href']
        jobs['post'] = post
        jobs['url'] = url
        main_data["number_of_job" + str(numbe_of_job)] = jobs
        numbe_of_job = numbe_of_job + 1
        
    return main_data


# data = extract_source_data(linkedIn)
# selected_data = selecting_some_data(data)
# pprint (len(selected_data))

