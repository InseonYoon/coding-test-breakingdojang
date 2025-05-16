from collections import defaultdict
from math import ceil

n, k = map(int, input().split())
students = defaultdict(int)
rooms = 0

for _ in range(n):
    gender, grade = input().split()
    students[gender+grade] += 1

for value in students.values():
    rooms += ceil(value/k)

print(rooms)