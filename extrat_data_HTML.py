import nltk   
import urllib
#from urllib import urlopen
import urllib.request
from bs4 import BeautifulSoup

url = "https://microtracker.org/profile/accion-east-new-york-ny/#whoIsBeingServed"  
sock = urllib.request.urlopen(url)

html = sock.read()  
#print(html)  
#raw = nltk.clean_html(html)  
raw=BeautifulSoup(html, 'html.parser').get_text()
print(raw)
tokens = nltk.word_tokenize(raw)
print(tokens)