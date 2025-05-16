import sys

T = sys.stdin.readline()
T = int(T.rstrip())
for i in range(T):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a+b)