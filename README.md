# Web Scrapper !!!

- venv 가상환경 조성 : 프로젝트 도구를 격리하고 충돌 방지

  - install
    `sudo apt install python3-venv`
  - project 내에 사용
    `python3 -m venv .venv`
  - 가상환경 시작
    `source .venv/bin/activate`
  - 가상 환경 비활성화  
    `deactivate`

---

- install `beautifulsoup4`, `requests`

- 만약 크롤링을 점검하는 로직이 있을 때
  - [user-agent-string](https://www.useragentstring.com/)
  - `get(url, headers={"User-Agent": "Jay"})`
  - [fake-useragent](https://pypi.org/project/fake-useragent/)

---

# Forbidden 403 Solution

- 403 Forbidden으로 solution이 필요함
  - [참고링크](https://goddino.tistory.com/353)
  - [selenium](https://www.selenium.dev/)
  - [webdriver-manager](https://pypi.org/project/webdriver-manager/)
  - [chrome-driver](https://chromedriver.chromium.org/downloads)

`pip3 install selenium #mac`
`pip3 install webdriver_manager #mac`

`pip install selenium #window`
`pip install webdriver_manager #window`
