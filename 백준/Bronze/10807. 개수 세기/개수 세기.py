n = input()
nums = list(map(int, input().split()))
v = int(input())

ctr = 0

for num in nums:
    if num == v:
        ctr += 1

print(ctr)