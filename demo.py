import requests
from bs4 import BeautifulSoup

url = "https://www.naukri.com/non-profit-jobs"
linkedIn = "https://in.linkedin.com/jobs/nonprofit-jobs?position=1&pageNum=0"

def extract_source(url):
    source = requests.get(linkedIn).content
    return source

print (extract_source(linkedIn))
