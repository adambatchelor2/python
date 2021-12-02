with open("aoc_2021_1.txt", 'r', encoding="utf8") as f:
    data = f.read()

y = data.split("\n")
a = 0

#Part 1

# Version 1
# for i,x in enumerate(y):
#     print(x, y[i+1])
#     if y[i+1] > x:
#         z = z + 1
#         print (z)

# Version 2
# for z in range(0,len(y)-1):
#     if int(y[z+1]) >= int(y[z]):
#         a = a + 1

# print(a)

# Part 2

for z in range(0,len(y)-3):
    b = int(y[z+1])+int(y[z+2])+int(y[z+3])
    c = int(y[z])+int(y[z+1])+int(y[z+2])
    if b > c:
        a = a + 1
print(a)