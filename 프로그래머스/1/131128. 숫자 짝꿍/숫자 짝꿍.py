def solution(X, Y):
    answer = ''
    ctrX = [0 for i in range(10)]
    ctrY = [0 for i in range(10)]
    ctr = [0 for i in range(10)]

    for c in str(X):
        ctrX[int(c)] += 1
    for c in str(Y):
        ctrY[int(c)] += 1
    for i in range(10):
        ctr[i] = ctrX[i] if ctrX[i]<= ctrY[i] else ctrY[i]
        
    if sum(ctr) == 0:
        return '-1'
    elif sum(ctr[1:10]) == 0:
        return '0'
    else:
        for i in range(9, -1, -1):
            for j in range(0, ctr[i]):
                answer += str(i)
        return answer