import requests
import bs4

file = open('Data.txt','wb')
req = requests.get('https://en.wikipedia.org/wiki/Machine_learning')

soup_obj = bs4.BeautifulSoup(req.text,'lxml')
paragraph = soup_obj.select('a')
for i in paragraph:
    data = i.get_text()
    file.write(data.encode())

file.close()



