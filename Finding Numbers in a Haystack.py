import re 
hand=open('regex_sum_415039.txt')
numlist=[]
for line in hand:
    line=line.rstrip()
    stuff=re.findall('\.*([0-9]+)',line)
    if len(stuff)<1:continue
    elif len(stuff)>=1:
        i=len(stuff)
        for j in range (i):
            num=int(stuff[j])
            numlist.append(num)
print(sum(numlist))


