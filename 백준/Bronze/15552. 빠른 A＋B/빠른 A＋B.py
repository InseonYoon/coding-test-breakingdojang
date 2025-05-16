import sys

lines = sys.stdin.readlines()
T = int(lines[0].rstrip())
output = []

for i in range(1, T+1):
    a, b = map(int, lines[i].split())
    output.append(f'{a+b}\n')

sys.stdout.write(''.join(output))