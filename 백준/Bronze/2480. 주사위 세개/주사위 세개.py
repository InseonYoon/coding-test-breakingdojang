d = sorted(map(int, input().split()))
ds = set(d)

if len(ds) == 1:
    print(10000+int(d[0])*1000)
elif len(ds) == 2:
    print(1000+int(d[1])*100)
else:
    print(int(d[2])*100)