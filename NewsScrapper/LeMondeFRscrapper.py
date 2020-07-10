#Prints 65 news headlines from Le Monde

import html5lib
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.lemonde.fr/politique/')
rc = r.content
soup = BeautifulSoup(rc , 'html5lib')
teaser_title = soup.findAll('h3')

counter = 0
for h in teaser_title:
    counter +=1
    print('#Header number ',str(counter),' ;', h.text ,'\n')
    
