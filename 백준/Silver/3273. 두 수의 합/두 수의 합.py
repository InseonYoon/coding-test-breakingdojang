n = input()
nums = list(map(int, input().split()))
x = int(input())

ctr = 0
seens = set()

for num in nums:
    if x-num in seens:
        ctr += 1
    else:
        seens.add(num)

print(ctr)