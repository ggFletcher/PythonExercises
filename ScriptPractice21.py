import requests

from bs4 import BeautifulSoup

outputFileName = input("Enter the name for the output file: ")
openFile = open(outputFileName, 'w')

base_url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, features="html.parser")
 
for textP in soup.find_all('p'): 
    if textP.a: 
        openFile.write(textP.a.text.replace("\n", " ").strip())
    else: 
        openFile.write(textP.contents[0].strip())

openFile.close()