a,b = map(int, input().split())
a, b = (a, b) if a<b else (b,a)
if b-a > 1:
    print(b-a-1)
    print(*range(a+1, b))
else:
    print(0, end='\n')