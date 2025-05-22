import sys

orders = sys.stdin.readlines()
K = int(orders[0].strip())
stack = []

for i in range(1, K+1):
    order = int(orders[i].strip())

    if order:
        stack.append(order)
    else:
        stack.pop()

print(sum(stack))