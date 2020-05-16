n = int(raw_input().strip())
scores = map(int,raw_input().strip().split(' '))
m = int(raw_input().strip())
alice = map(int,raw_input().strip().split(' '))

leaderboard = sorted(set(scores), reverse = True)
l = len(leaderboard)

for a in alice:
    while (l > 0) and (a >= leaderboard[l-1]):
        l -= 1
    print (l+1)

-----------------------------------------------------------------------------

scores_count = int(input())
scores = list(map(int, input().rstrip().split()))
alice_count = int(input())
alice = list(map(int, input().rstrip().split()))
x = list(set(scores))
y=[]
for j in range (alice_count):
    x.append(alice[j])
    y=list(set(x))
    y.sort()
    y.reverse()
    print (y.index(alice[j])+1)
    x.remove(alice[j])
    
