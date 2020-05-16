def merge_the_tools(string, k):
    from collections import OrderedDict
    t=[]
    n=int(len(string))/k
    for i in range(int(n)):
        t.append(string[i*int(k):int(k)+i*int(k)])
    for j in t:
        p=(list(OrderedDict.fromkeys(j)))
        print(''.join(p)) 
    # your code goes here

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
