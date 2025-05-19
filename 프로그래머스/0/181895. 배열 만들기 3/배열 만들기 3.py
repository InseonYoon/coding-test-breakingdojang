def solution(arr, intervals):
    answer = []
    r1, r2 = intervals
    a1, b1 = r1
    a2, b2 = r2
    for i in range(a1, b1+1):
        answer.append(arr[i])
    for i in range(a2, b2+1):
        answer.append(arr[i])
    return answer