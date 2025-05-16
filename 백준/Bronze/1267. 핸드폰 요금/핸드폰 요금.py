calls = int(input())
times = list(map(int, input().split()))
y = [0 for _ in range(calls)]
m = [0 for _ in range(calls)]
for i in range(calls):
    y[i] = (times[i]//30+1)*10
    m[i] = (times[i]//60+1)*15
ysum = sum(y)
msum = sum(m)

if ysum == msum:
    print('Y M', end=' ')
    print(ysum)
else:
    print('Y' if ysum<msum else 'M', end=' ')
    print(ysum if ysum<msum else msum)