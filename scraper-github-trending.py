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


# get number of stars
for repo in repo_list:
  full_repo_name = repo.find('a').text.split('/')
  developer = full_repo_name[0].strip()
  repo_name = full_repo_name[1].strip()
  stars = repo.find(class_='octicon octicon-star').parent.text.strip()
  print('developer', developer)
  print('name', repo_name)
