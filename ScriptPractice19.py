import requests

from bs4 import BeautifulSoup

base_url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, features="html.parser")
 
for textP in soup.find_all('p'): 
    if textP.a: 
        print(textP.a.text.replace("\n", " ").strip())
    else: 
        print(textP.contents[0].strip())