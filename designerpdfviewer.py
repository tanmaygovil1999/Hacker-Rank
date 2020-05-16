h = list(map(int, input().rstrip().split()))

word = input()
maxHeight=0
for i in range(len(word)):
    if(h[ord(word[i])-97] > maxHeight):
        maxHeight=h[ord(word[i])-97]
print(len(word)*1*maxHeight)
