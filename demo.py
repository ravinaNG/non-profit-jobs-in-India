import requests
from bs4 import BeautifulSoup

url = "https://www.naukri.com/non-profit-jobs"
request = requests.get(url)
print (request)
