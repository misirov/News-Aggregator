#prints national german news from Der Spiegel
#MUST REVIEW, INEFFICIENT OUTUP!

import html5lib
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.spiegel.de/international/germany/')
rc = r.content
soup = BeautifulSoup(rc , 'html5lib')
article = soup.findAll('article')
article = article[0:20]
counter = 0

for h in article:
    if h.text != ' ':
        counter +=1
        print('#Header number '+str(counter)+' ;'+ h.text )
    
