from bs4 import BeautifulSoup
from requests import get

base_url = 'https://weworkremotely.com/remote-jobs/search?term='
search_term = 'python'

response = get(f'{base_url}{search_term}')

if not response.status_code == 200:
    print('cant requests')
else:
    soup = BeautifulSoup(response.content, 'html.parser').prettify()
    print(soup)
