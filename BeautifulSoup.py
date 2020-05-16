from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re 

b=[]
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input()
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")


tags = soup('span')
for tag in tags:
    print('Contents:', tag.contents[0])
    b.append(int(tag.contents[0]))
print(sum(b))
