def replace(lists, start, end):
    lists[start-1:end] = lists[start-1:end][::-1]
    return

a, b = 0, 0
cards = [i+1 for i in range(20)]
for _ in range(10):
    a, b = map(int, input().split())
    replace(cards, a, b)
print(*cards)