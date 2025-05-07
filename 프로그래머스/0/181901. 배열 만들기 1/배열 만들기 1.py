def solution(n, k):
    # answer = []
    # maxi = (n//k)
    # for i in range(maxi):
    #     answer.append((i+1)*k)
    # return answer
    return [i for i in range(k, n+1, k)]