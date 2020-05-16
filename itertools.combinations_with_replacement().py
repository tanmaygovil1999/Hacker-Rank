from itertools import combinations_with_replacement
x= list(input().split())
m=x[0]
n=int(x[1])
t=[]
for i in combinations_with_replacement(sorted(m),n):
    t.append(list(i))
print (*[''.join(sorted(i)) for i in t],sep='\n')
