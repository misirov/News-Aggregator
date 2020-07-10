#Prints 25 articles located in the National directory


import html5lib
from bs4 import BeautifulSoup
import requests

r = requests.get('https://elpais.com/espana/')
rc = r.content
soup = BeautifulSoup(rc , 'html5lib')

headings = soup.find_all('a')
#find 'a' tags only related to news headlines,we dont need text for external links
headings = headings[29:-14]
counter = 0
links = []

for a in headings:
    #Gets rid of Author names (Headlines tend to be longer than 20 characters)
    if a.text > a.text[0:25]:
        counter += 1
        links.append(a.get('href'))
        print('#Headline number ' + str(counter) +'; ' + a.text + '\n')



