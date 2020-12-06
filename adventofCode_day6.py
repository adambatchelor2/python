with open("aoc6.txt", 'r', encoding="utf8") as f:
    data = f.read()

y = data.split("\n\n")
count_uniq = 0

for x in y:
    uniq_list = []
    z = x.split("\n")
    print(z)
    all = (''.join(map(str, z)))

    uniq_list = []

print(y)