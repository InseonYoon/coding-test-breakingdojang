for tc in range(1, 11):
    n = int(input())
    blist = list(map(int, input().split()))
    vlist = [0 for i in range(n)]

    for i in range(2, n-2):
        h = blist[i]
        v1 = max(h-blist[i-2], 0)
        v2 = max(h-blist[i-1], 0)
        v3 = max(h-blist[i+1], 0)
        v4 = max(h-blist[i+2], 0)
        vlist[i] = min(v1, v2, v3, v4)
    
    print(f'#{tc}', end=' ')
    print(sum(vlist))