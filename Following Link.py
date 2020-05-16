import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
b=[]
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count=input()
position=input()
for i in range (0,int(count)):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        b.append(tag.get('href', None))
    print (b[int(position)-1])
    url=b[int(position)-1]
    b=[]
