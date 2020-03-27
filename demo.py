import requests
from bs4 import BeautifulSoup # python librery to pull out data from 
import html5lib # pure python library for parshing markup into html
from pprint import pprint

url = "https://www.naukri.com/non-profit-jobs"
linkedIn = "https://in.linkedin.com/jobs/nonprofit-jobs?position=1&pageNum=0"

def extract_source(url):
    source = requests.get(linkedIn).content
    return source

def extract_data(source):
    soup = BeautifulSoup(source, "html5lib")
    # names = soup.findAll('title')
    return soup

source = extract_source(linkedIn)
jobs = extract_data(source)
pprint (jobs)

