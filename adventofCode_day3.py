
with open("aoc3.txt", 'r', encoding="utf8") as f:
    data = f.read()

y = data.split("\n")
z = 0
count = 0
len_line = 31

# for x in y:
#
#     if z > 30:
#         z = z - 31
#     # print([x, z])
#     # print([x, z, x[z]])
#
#     if x[z] == "#":
#             count += 1
#     z+=3
#
# print(count)


for i,x in enumerate(y):
    if i%2!=0:
        if z > 30:
            z = z - 31
        # print([x, z])
        # print([x, z, x[z]])

        if x[z] == "#":
                count += 1
        z+=2

print(count)

# r3 d1 282
# r1 d1 53
# r5 d1 54
# r7 d1 54
# r1 d2 24