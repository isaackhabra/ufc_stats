from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import requests

UFC_RANKINGS_WEBSITE_URL = 'https://www.ufc.com/rankings'
UFC_ATHLETE_BASE_URL = 'https://www.ufc.com/athlete/'
UFC_AJAX_API_URL = 'https://www.ufc.com/views/ajax'

soup = BeautifulSoup(requests.get(UFC_RANKINGS_WEBSITE_URL).content, 'html.parser')
html_rankings = soup.find_all(class_='views-field views-field-title')
html_rankings.extend(soup.find_all('h5'))

all_ranked_fighters_names = set()
ranked_fighters_name_to_href = {}

for ranking in html_rankings:
    #print(ranking)
    #print(ranking.get_text())
    #print(ranking.find('a')['href'])
    # Create a list of only the ranked fighters, including the links to their athlete pages
    #temp = ([s.rstrip() for s in ranking.get_text().splitlines() if len(s.rstrip()) > 2 and s != 'Champion' and not s[:4] == 'Rank'][2:])
    fighter_name = ranking.get_text().rstrip()
    if fighter_name in all_ranked_fighters_names: continue
    
    ranked_fighters_name_to_href[fighter_name] = ranking.find('a')['href']
    all_ranked_fighters_names.update([fighter_name])
    
print('final list')
print('-----------------------------------')
print(all_ranked_fighters_names)
print(len(all_ranked_fighters_names))
print(ranked_fighters_name_to_href)




# Now, we want to iterate through every ranked fighters, and build a dictionary of who's beaten them
# We want to go to the athlete's page on the UFC website, and go through all their fight results, and find who beat them

ranked_fighters_beaten = {}


'''with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://example.com")

    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(2000)

    html = page.content()
    print(html)

    browser.close()'''

for fighter_name in all_ranked_fighters_names:
    print(fighter_name)
    fighter_href = ranked_fighters_name_to_href[fighter_name]
    
    # initial request
    
    

