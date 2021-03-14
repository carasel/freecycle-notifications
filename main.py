import requests

from bs4 import BeautifulSoup


url = 'https://groups.freecycle.org/group/CardiffUK/posts/all?page=2&resultsperpage=100&showall=on'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find(id='group_posts_table')
table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    status = td[0]
    title = td[1]
    print(status.text.strip())
    print(title.text.strip())
    print('-------------------------------')
