
import re

final_count = 0
final_list = []
mydict = {}
listfinal = []

with open("aoc7.txt", 'r', encoding="utf8") as f:
    data = f.readlines()

for z in data:
    out = re.findall("([a-z]+ [a-z]+) bag", z)
    mydict[out[0]] = out[1:]

print(mydict)

def find_in_dict(dict, findValue,listOut):
    for key, value in mydict.items():
        if findValue in key:
            listOut.append(value)
            find_in_dict(dict,value,listOut)

    return listOut


final_list = find_in_dict(mydict,'shiny gold',listfinal)
print(final_list)
print(len(final_list))

res = []
for i in final_list:
    if i not in res:
        res.append(i)

print(res)
print(len(res))
# 141