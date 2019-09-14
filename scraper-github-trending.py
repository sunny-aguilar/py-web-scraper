# webscraper
import requests
from bs4 import BeautifulSoup

# Get the page
page = requests.get('https://github.com/trending')
#print(page)

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')
#print(soup)


# Exctracting data - get teh repo list
repo = soup.find(class_="explore-pjax-container container-lg p-responsive pt-6")

# Extracing data - find all instances of this class
repo_list = repo.find_all(class_='Box-row')

print(len(repo_list))


