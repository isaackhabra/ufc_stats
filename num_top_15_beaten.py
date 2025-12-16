from bs4 import BeautifulSoup
import requests
import os

UFC_RANKINGS_WEBSITE_URL = 'https://www.ufc.com/rankings'

soup = BeautifulSoup(requests.get(UFC_RANKINGS_WEBSITE_URL).content, 'html.parser')
html_rankings = soup.find_all(class_='view-grouping')
all_ranked_fighters = set()

for ranking in html_rankings:
    # Create a list of only the ranked fighters, including the links to their athlete pages
    temp = ([s.rstrip() for s in ranking.get_text().splitlines() if len(s.rstrip()) > 2 and s != 'Champion' and not s[:4] == 'Rank'][2:])
    all_ranked_fighters.update(temp)
    
    
print(all_ranked_fighters)
print(len(all_ranked_fighters))


# Now, we want to iterate through every ranked fighters, and build a dictionary of who's beaten them
# We will get this data from wherever it's convenient

ranked_fighters_beaten = {}

