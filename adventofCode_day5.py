
with open("aoc5.txt", 'r', encoding="utf8") as f:
    data = f.read()

data_list = data.split("\n")
max_id = 0
min_id = 100
all_ID = []

for z in data_list:

    long = [x for x in range(0,128)]
    width = [y for y in range(0,8)]

    for x in z:
        dist = int(len(long) / 2)
        if x == 'F':
            long = long[:dist]
        elif x == 'B':
            long = long[dist:]

    for x in z:
        dist = int(len(width) / 2)
        if x == 'L':
            width = width[:dist]
        elif x == 'R':
            width = width[dist:]

    seat_id = (long[0]*8)+width[0]
    all_ID.append(seat_id)

    if seat_id > max_id:
        max_id = seat_id
    if seat_id < min_id:
        min_id = seat_id

print(min_id)
print(max_id)
print(all_ID)

for x in range(min_id,max_id):
    if x not in all_ID and x-1 in all_ID and x+1 in all_ID:
        print(x)