import requests
from bs4 import BeautifulSoup


url = 'https://groups.freecycle.org/group/CardiffUK/posts/all?page=2&resultsperpage=100&showall=on&include_offers=off&include_wanteds=off&include_receiveds=off&include_takens=off'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
