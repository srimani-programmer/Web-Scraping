import requests
import bs4

req = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')

soup = bs4.BeautifulSoup(req.text,'lxml')

for i in soup.find_all('a', href = True):
    if(i['href'][0] != 'h'):
        continue
    else:
        print(i['href'])