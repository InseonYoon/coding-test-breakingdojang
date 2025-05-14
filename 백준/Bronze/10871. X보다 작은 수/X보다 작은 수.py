N, X = map(int, input().split())
arr = list(map(int, input().split()))
result = list()

for i in range(0, N):
    if arr[i] < X:
        result.append(arr[i])

print(*result)