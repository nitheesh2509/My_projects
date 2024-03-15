import requests
from bs4 import BeautifulSoup
url = 'http://quotes.toscrape.com/'
responses = requests.get(url)
soup = BeautifulSoup(responses.text,'lxml')
quotes = soup.findAll('span',class_='text')
authors = soup.findAll('small',class_='author')
tags = soup.findAll('div',class_='tags')
for i in range(0,len(quotes)):
    print(authors[i].text)
    print(quotes[i].text)
    quotetag = tags[i].findAll('a',class_="tag")
    for quote in quotetag:
        print(quote.text)