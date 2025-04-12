from collections import Counter

def solution(a, b, c, d):
    dlist = [a, b, c, d]
    cnt = Counter(dlist)
    
    if len(cnt) == 4:
        return min(dlist)
    elif len(cnt) == 3:
        qr = [k for k, v in cnt.items() if v == 1]
        return qr[0]*qr[1]
    elif len(cnt) == 2:
        pq2 = [k for k, v in cnt.items() if v == 2]
        if len(pq2) == 2:
            return (pq2[0]+pq2[1])*abs(pq2[0]-pq2[1])
        else:
            p3 = next((k for k, v in cnt.items() if v == 3), None)
            q1 = next((k for k, v in cnt.items() if v == 1), None)
            return (10*p3+q1)**2
    else:
        return 1111*dlist[0]