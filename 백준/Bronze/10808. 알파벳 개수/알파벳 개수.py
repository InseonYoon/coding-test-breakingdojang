str = input()
letters = [0 for _ in range(26)]
for i in range(26):
    letters[i] = str.count(chr(97+i))
    print(letters[i], end=' ')