with open("aoc_2021_2.txt", 'r', encoding="utf8") as f:
    data = f.read()

y = data.split("\n")

x_pos = 0
y_pos = 0
aim = 0

# Part 1
# for r in y:
#     z = r.split()
#     if z[0] == 'forward':
#         x_pos = x_pos + int(z[1])
#     if z[0] == 'down':
#         y_pos = y_pos + int(z[1])
#     if z[0] == 'up':
#         y_pos = y_pos - int(z[1])

# print(x_pos*y_pos)


# Part 2

for r in y:
    z = r.split()
    if z[0] == 'forward':
        x_pos = x_pos + int(z[1])
        y_pos = y_pos + (aim * int(z[1]))
    if z[0] == 'down':
        #y_pos = y_pos + int(z[1])
        aim = aim + int(z[1])
    if z[0] == 'up':
        #y_pos = y_pos - int(z[1])
        aim = aim - int(z[1])
    #print(r,x_pos,y_pos,aim)

print(x_pos,y_pos)
print(x_pos*y_pos)