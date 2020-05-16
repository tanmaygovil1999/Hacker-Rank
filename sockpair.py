n = int(input())
ar = list(map(int, input().rstrip().split()))
from collections import Counter
sock_count = Counter()
pairs = 0

for sock in ar:
     if sock not in sock_count:
         sock_count[sock] += 1
     else:
         pairs += 1
         del sock_count[sock]
    
print (pairs)
