from bs4 import BeautifulSoup
from requests import get

from extractors.wwr import extract_wwr_jobs

print(extract_wwr_jobs('python'))
