h = []
for _ in range(9):
    h.append(int(input()))
h.sort()
hsum = sum(h)

for i in range(9):
    for j in range(i+1, 9):
        if hsum-h[i]-h[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    pass
                else:
                    print(h[k])
            exit()