

import random

a = []
b = []
ans = []

#print([x for x in a])

for _ in range(200):
	a.append(random.randint(0, 200))

for _ in range(200):
	b.append(random.randint(0, 200))

print("List 1: ")
print([x for x in a])
print("\nList 2: ")
print([x for x in b])
print("\nOverlap: ")
for x in a:	
	if x in b and x not in ans:
		ans.append(x)

print([y for y in ans])