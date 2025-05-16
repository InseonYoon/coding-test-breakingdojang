from collections import Counter

str1 = input()
str2 = input()
c1 = Counter(str1)
c2 = Counter(str2)
intersection = c1&c2
union = c1|c2
diff = union - intersection

ctr = 0
for value in diff.values():
   ctr += value 
print(ctr)