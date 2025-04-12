from collections import Counter

def solution(array):
    ctr = Counter(array)
    answer = [k for k,v in ctr.items() if v == max(ctr.values())]
    return answer[0] if len(answer) == 1 else -1