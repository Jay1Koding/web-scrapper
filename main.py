from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # 크롬 드라이버 자동 업데이트

from extractors.wwr import extract_wwr_jobs

chrome_options = Options()  # 브라우저 꺼짐 방지
chrome_options.add_experimental_option("detach", True)


browser = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=chrome_options)

# 크롬 드라이버 최신 버전 자동 설치 후 서비스 만들기
service = Service(executable_path=ChromeDriverManager().install())

base_url = 'https://kr.indeed.com/jobs?q='
search_term = 'python'

browser.get(f'{base_url}{search_term}')

soup = BeautifulSoup(browser.page_source, 'html.parser')
print(soup.prettify())
