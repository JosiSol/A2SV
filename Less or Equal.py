def L():
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    l.sort()
    if k == n or l[k - 1] < l[k]:
        print(l[k-1])
    elif k == 0 and l[k] != 1:
        print(l[k] - 1)
    else:
        print(-1)
L()
