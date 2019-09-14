# webscraper
import requests
from bs4 import BeautifulSoup

# Get the page
page = requests.get('https://github.com/trending')
print(page)

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text)
