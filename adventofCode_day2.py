
import re

with open("aoc2.txt", 'r', encoding="utf8") as f:
    data = f.read()

y = data.split("\n")

pass_count = 0

# Part 1
# for x in y:
#     z = re.search("([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)",x)
#     pw = z.group(4)
#     letter = z.group(3)
#     min_count = int(z.group(1))
#     max_count = int(z.group(2))
#     count = 0
#     for z in list(pw):
#         if letter == z:
#             count += 1
#     if count >= min_count and count <= max_count:
#         pass_count += 1
#         print([x,count,letter])
#
# print (pass_count)

#Part 2
for x in y:
    z = re.search("([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)",x)
    pw = z.group(4)
    letter = z.group(3)
    min_count = int(z.group(1))
    max_count = int(z.group(2))

    if (pw[min_count-1] == letter and pw[max_count-1] != letter) or (pw[min_count-1] != letter and pw[max_count-1] == letter):

        # print([x,pw,pw[min_count-1],pw[max_count-1],letter])
        pass_count += 1

print (pass_count)