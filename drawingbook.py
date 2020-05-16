n = int(input())
p = int(input())
count=0
mount=0
if n%2!=0:
    if p in range (n-1,n+1):
        mount+=0
    for i in range (1,n-1):
        if p in range (2*i,2*i+2):
            count+=i
    for i in range (1,n-1):
        if p in range (n-2*i-1,n-2*i+1):
            mount+=i
if n%2==0:
    if p in range (n,n+1):
        mount+=0
    for i in range (1,n-1):
        if p in range (2*i,2*i+2):
            count+=i
    for i in range (1,n-1):
        if p in range (n-2*i,n-2*i+2):
            mount+=i        
if p in range (0,2):
    count+=0


print (min(count,mount))
