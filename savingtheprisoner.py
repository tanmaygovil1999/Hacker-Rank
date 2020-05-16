t = int(input())

for t_itr in range(t):
    nms = input().split()

    n = int(nms[0])

    m = int(nms[1])

    s = int(nms[2])
    if s + m < n:
        print (s + m - 1)
    else:
        if (s+m - 1) % n == 0:
            print (n)
        else:
            print ((s+m - 1) % n)
