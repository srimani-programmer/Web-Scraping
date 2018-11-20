import requests as req
import bs4 as b

# Making a request.
res = req.get('https://www.learncodeonline.in')

# converting request object to soup object.
soup = b.BeautifulSoup(res.text,'lxml')

title = soup.select('title')

# getting all details from the data variable.

for i in title:
    print(i.getText())

