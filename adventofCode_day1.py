
import re

with open("aoc1.txt", 'r', encoding="utf8") as f:
    data = f.readlines()

for i,x in enumerate(data):
    y = re.search("([0-9]+)",x)
    data[i] = int(y.group(1))

z = 2020

# part 1
# for a in data:
#     if z-a in data:
#         print((z-a)*a)
#         break

# part 2
# Three numbers that add up to 2020

for c in data:
    for d in data:
        for e in data:
            if c+d+e == z:
                print(c*d*e)
                break