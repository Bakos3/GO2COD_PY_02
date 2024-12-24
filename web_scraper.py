import requests
from bs4 import BeautifulSoup

url = input('enter url(eg:-https://example.com):\n')

response = requests.get(url)

html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

headlines = soup.find_all(input('enter tag name(eg:-h1):\n'))

for headline in headlines:
    print(headline.text)
