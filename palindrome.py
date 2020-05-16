pal=str(input())
for i in range(0, len(pal)):
    if pal[i] != pal[len(pal)-i-1]:
        print("not a palindrome")
        break
else:
    print("a palindrome")
 
