from bs4 import BeautifulSoup
from requests import get


def extract_wwr_jobs(keyword):

    base_url = 'https://weworkremotely.com/remote-jobs/search?term='
    search_term = 'python'

    response = get(f'{base_url}{search_term}')

    if not response.status_code == 200:
        print('cant requests')
    else:
        results = []
        soup = BeautifulSoup(response.content, 'html.parser')
        jobs = soup.find_all('section', class_='jobs')
        for job_sections in jobs:
            job_posts = job_sections.find_all('li')
            job_posts.pop(-1)
            for posts in job_posts:
                anchors = posts.find_all('a')
                anchor = anchors[1]
                link = anchor['href']
                title = anchor.find('span', class_='title')
                company, time, region = anchor.find_all(
                    'span', class_='company')
                job_data = {
                    'link': f'https://weworkremotely.com{link}',
                    'title': title.string,
                    'company': company.string,
                    'time': time.string,
                    'region': region.string,
                }
                results.append(job_data)
        return results
