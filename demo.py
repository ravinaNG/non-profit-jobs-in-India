import requests
from bs4 import BeautifulSoup # python librery to pull out data from 
import html5lib # pure python library for parshing markup into html
from pprint import pprint 

url = "https://www.naukri.com/non-profit-jobs"
linkedIn = "https://www.linkedin.com/jobs/nonprofit-jobs/?originalSubdomain=in"

def extract_source_data(url):
    source = requests.get(linkedIn).text
    extract_data = BeautifulSoup(source, "html5lib")
    return extract_data

data = extract_source_data(linkedIn)
print (data)
home_page = data.find('div', {'class':'jobs-search-two-pane__results display-flex'})
pprint (home_page)

