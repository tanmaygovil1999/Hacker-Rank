n = int(input())
s = input()
count=0
mount=0
for i in range (n):
    if s[i]=='U':
        count+=1
        if count==0:
            mount+=1
    else :
        count-=1
print (mount)
