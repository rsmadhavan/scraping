import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup

url = 'https://chennaicitybus.in/route-no/m147n/'
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

route_no = url.split('/')[4].upper()
print(route_no)
soup = BeautifulSoup(page_html,'html.parser')
stops = soup.findAll('table')[1].findAll('td')
count = len(stops)
print(count)