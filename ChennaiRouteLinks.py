import bs4 
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup 

myUrl = 'https://chennaicitybus.in/page/'
page_count = 72
file = open("/home/maddy/Desktop/scrap/chennai.txt","w")
for page in range(1,page_count+1):
    url = myUrl+str(page)
    print(url)
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()

    soup = BeautifulSoup(page_html, 'html.parser')
    header = soup.findAll('h3')
    count=len(header)
    for i in range(count):
        route_link = header[i].a['href']
        file.write(route_link+'\n')
file.close()
print("Finished Scaping Route Links")
