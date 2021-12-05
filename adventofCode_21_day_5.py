
def coords(str):
    b = str.split(" -> ")
    newlist = []

    for x in b:
        x = x.split(",")
        newlist.append(x)

    cord1 = [newlist[0][0],newlist[0][1]]
    cord2 = [newlist[1][0],newlist[1][1]]

    return([cord1,cord2])


with open("aoc_2021_5.txt", 'r', encoding="utf8") as f:
    data = f.read()

y = data.split("\n")
# print(y)
outCords = []
for x in y:
    newCoords = coords(x)
    # print(newCoords)
    if newCoords[0][0] == newCoords[1][0] or newCoords[0][1] == newCoords[1][1]: #all coords matching
        # print(newCoords)
        newCoords.sort()
        # create all coords in line
        if newCoords[0][0] == newCoords[1][0]:
            for x in range(int(newCoords[0][1])+1,int(newCoords[1][1])):
                newCoords.append([newCoords[0][0],str(x)])
        elif newCoords[0][1] == newCoords[1][1]: #all coords matching
            for x in range(int(newCoords[0][0])+1,int(newCoords[1][0])):
                newCoords.append([str(x),newCoords[0][1]])
       
        outCords.append(newCoords)

# print(outCords)

deDupeList = []
final_list = []

for x in outCords:
    for y in x:
        final_list.append(y)
        if y not in deDupeList:
            deDupeList.append(y)

# print(deDupeList)
list_with_2 = []

for x in deDupeList:
    if final_list.count(x) >= 2:
        list_with_2.append(x)
print(list_with_2)
print(len(list_with_2))
# print(outCords)
# populate all potential points in a grid
# use dict to count how many of each point
# Work out all coordinates in route

# Answer = 4541 INCORRECT