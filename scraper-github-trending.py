# webscraper
import requests
from bs4 import BeautifulSoup
import csv

# Get the page
page = requests.get('https://github.com/trending')
print(page)

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')
#print(soup)


# Exctracting data - get the repo list
repo = soup.find(class_="explore-pjax-container container-lg p-responsive pt-6")

# Extracing data - find all instances of this class
repo_list = repo.find_all(class_='h3 lh-condensed')

print(len(repo_list))

# create a file object and write column names
file_name = 'github_trending_today.csv'
f = csv.writer(open(file_name, 'w', newline=''))
f.writerow(['Developer', 'Repo Name'])


# get developer and repo name
for repo in repo_list:
  # find the first a tax and split using '/' to get an array with the name and repo
  full_repo_name = repo.find('a').text.split('/')

  # remove unwanted characters
  developer = full_repo_name[0].strip()
  repo_name = full_repo_name[1].strip()

  # get the starts for each repo
  stars = repo.find(class_='f6 text-gray mt-2').text.strip()

  # display information
  print('developer: ', developer)
  print('name: ', repo_name)
  print('stars: ', stars)

  # add the info as a row into the CSV file
  f.writerow([developer, repo_name])
