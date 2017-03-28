#Beautifulsoup is used to extract any kind of data between html tags
#BeautifulSoup.py should be added to ur project folder
import urllib
from BeautifulSoup import *

url=raw_input('Enter - ')
#it open the url and reads the html data of the given link and returns string
html=urllib.urlopen(url).read()
#creating obj of beautifulsoup by passing our resultant string
soup=BeautifulSoup(html)

#mention the tag which u want to retrieve
tags=soup('a')
print type(tags)
for tag in tags:
    print tag.get('href',None); 


#retrieving the values of h1 tag
print "H1 tag values--------"
h1tags=soup('h1')
i=0
for tag in h1tags:
    h1value = soup.findAll("h1")[i].string.strip()
    i=i+1;
    print h1value