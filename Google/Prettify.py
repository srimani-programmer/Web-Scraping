import requests
import bs4 

req = requests.get("https://www.google.com/")

soup_obj = bs4.BeautifulSoup(req.text,"lxml")

# prettify() will produce the good html format to analyse.
print(soup_obj.prettify())