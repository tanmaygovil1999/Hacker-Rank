from itertools import groupby
n=input()
print(*[i for i in list([(len(list(g)),int(k)) for k, g in groupby(n)])])
