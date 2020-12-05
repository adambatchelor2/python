
# with open("aoc5.txt", 'r', encoding="utf8") as f:
#     data = f.read()
#
# y = data.split("\n")

y = 'FBFBBFFRLR' # row 44

range = [x for x in range(0,128)]
width = [y for t in range(0,8)]
for x in y:
    dist = int(len(range) / 2)
    if x == 'F':
        range = range[:dist]
        print(['F',range])
    elif x == 'B':
        range = range[dist:]
        print(['B', range])
print(range)