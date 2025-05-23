import sys

orders = sys.stdin.readlines()
N = int(orders[0].strip())
queue = []
head = 0
tail = 0

for i in range(1, N+1):
    order = orders[i].strip().split()

    if order[0] == 'push':
        queue.append(int(order[1]))
        tail += 1
    elif order[0] == 'pop':
        if head == tail:
            print(-1)
        else:
            print(queue[head])
            head += 1
    elif order[0] == 'size':
        print(tail-head)
    elif order[0] == 'empty':
        print(1 if head == tail else 0)
    elif order[0] == 'front':
        if head == tail:
            print(-1)
        else:
            print(queue[head])
    else: # order[0] == 'back'
        if head == tail:
            print(-1)
        else:
            print(queue[tail-1])