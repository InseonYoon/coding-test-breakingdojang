import sys

orders = sys.stdin.readlines()
N = int(orders[0].strip())
stack = []

for i in range(1, N+1):
    order = orders[i].strip().split()

    if order[0] == 'push':
        stack.append(int(order[1]))
    elif order[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        print(0 if stack else 1)
    else: # order[0] == 'top'
        if stack:
            print(stack[-1])
        else:
            print(-1)