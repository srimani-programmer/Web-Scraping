import requests
import bs4

file = open('content.txt','wb')
req = requests.get('https://en.wikipedia.org/wiki/Web_scraping')

soup_obj = bs4.BeautifulSoup(req.text,'lxml')

data = soup_obj.select('a')
k = 0
for i in data:
    data = i.get_text() + '\n'
    file.write(data.encode())
    print('Processing...',k)
    k += 1
file.close()
