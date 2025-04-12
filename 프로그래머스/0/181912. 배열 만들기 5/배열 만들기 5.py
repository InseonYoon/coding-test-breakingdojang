def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        newi =int(i[s:s+l])
        if newi > k:
            answer.append(newi)
    return answer