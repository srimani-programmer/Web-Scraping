import requests as req
import bs4 as b

res = req.get('https://www.learncodeonline.in')

soup = b.BeautifulSoup(res.text,'lxml')

for i in soup.find_all('a', href = True):
    if i['href'] == '#':
        continue
    else:
        print(i['href'])