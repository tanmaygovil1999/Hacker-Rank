import re
y=re.findall(r'(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])',input())
if (len(y)==0):
    print('-1')
for i in (y):
    print(i)
