from bs4 import BeautifulSoup
import requests
import html5lib

#india-times
r = requests.get("https://timesofindia.indiatimes.com/briefs")
rc = r.content
soup = BeautifulSoup(rc , "html5lib")
soup = soup.find_all('h2')

#hindu-times
r2 = requests.get("https://www.hindustantimes.com/india-news/")
rc2 = r2.content
soup2 = BeautifulSoup(rc2 , "html5lib")
soup2 = soup2.find_all("div" , {"class":"headingfour"})



