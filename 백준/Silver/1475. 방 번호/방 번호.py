from math import ceil

n = input()
ctr = [0 for _ in range(10)]

for i in range(len(n)):
    ctr[int(n[i])] += 1
ctr[6] = ceil((ctr[6]+ctr[9])/2)
ctr[9] = ctr[6]

print(ctr[ctr.index(max(ctr))])