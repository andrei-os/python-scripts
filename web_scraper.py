import sys
import selenium 

from selenium import webdriver
from bs4 import BeautifulSoup

def parse_hyperlinks(elements):
    links = []
    for element in elements:
        hyperlink = element.get('href')

        if isinstance(hyperlink, str):
            if url in hyperlink: links.append(hyperlink)
            elif hyperlink[0] == '/': links.append(url + hyperlink[1:])

    return links


if len(sys.argv) != 2:
    print('Provide a url.', file = sys.stderr)
    sys.exit(1)

url = sys.argv[1]

options = selenium.webdriver.ChromeOptions()
options.add_argument('headless')
browser = selenium.webdriver.Chrome(chrome_options = options)

browser.get(url)
html = browser.page_source

soup = BeautifulSoup(html, 'lxml')

links = parse_hyperlinks(soup.find_all('a'))
for link in links:
    print(link)

browser.quit()
