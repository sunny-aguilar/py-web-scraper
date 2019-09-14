# webscraper
import requests
from bs4 import BeautifulSoup

# Get the page
page = requests.get('https://github.com/trending')
print(page)

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')
#print(soup)


# Exctracting data - get teh repo list
repo = soup.find(class_="Box")

# Extracing data - find all instances of this class
repo_list = repo.find_all(class_='Box-row ')

print(repo_list)
