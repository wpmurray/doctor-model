'''
#Webscraper for ontario doctor directory
from bs4 import BeautifulSoup
import time
import requests
import csv
from pandas import DataFrame as df
import urllib.request

url = "https://www.ontariodoctordirectory.ca/rating/Burlington/Doctor-Rosalind-Antonia-Ward-Smith-13594.html"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

print(soup.prettify())

docs = soup.find_all('strong')

for doc in docs:
    print(doc)
'''
'''
Use beautifulsoup & selenium based webscraper for the ratemds website
'''

from bs4 import BeautifulSoup
import requests
import time


reviews = []
page = 2
url = 'https://www.ratemds.com/best-doctors/on/toronto/family-gp/?page={}'.format(page)
url_doc = 'https://www.ratemds.com/doctor-ratings/dr-sandy-van-toronto-on-ca?page=1'
page = requests.get(url)
#soup = BeautifulSoup(page.text, 'html.parser')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
#options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
#options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(30)
driver.get(url)



more_doctors = driver.find_elements_by_class_name('search-item-doctor-link')
for x in range(len(more_doctors)):
    driver.execute_script("arguments[0].click();", more_doctors[x])
    time.sleep(30)
    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')
    docReviews = soup.find_all('div', class_='rating')
    x += 1
    for reviewSelector in docReviews:
        reviewDiv = reviewSelector.find('div', class_='rating-comment')
        review = reviewDiv.find('div', class_='rating-comment-body').find('p').get_text()
        review = review.strip()
        reviews.append(review)

print(reviews)

'''
source = driver.page_source
soup = BeautifulSoup(source, 'lxml')
reviews = []
doctors = soup.find_all('a', class_='search-item-doctor-link')

for doctor in range(len(doctors)):
    if doctors[x].is_displayed():
        driver.execute_script("arguments[0].click();")
soup.select('.search-item-doctor-link')  # href .rating-comment
driver.close()
# install selenium
# download the driver
# addd the driver to your path
'''
