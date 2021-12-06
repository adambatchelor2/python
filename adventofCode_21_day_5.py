
def coords(str): # split string into a list with two items
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

outCords = []
for x in y: #loop through rows of data
    newCoords = coords(x) #call function to split from text into a lits
    
    if newCoords[0][0] == newCoords[1][0] or newCoords[0][1] == newCoords[1][1]: # only coords where one part is matching i.e. 3,7 - 8,7
        
        newCoords.sort() # order so that smallest is first
        
        # section to append all missing values into list i.e. 4,7 5,7 6,7 7,7
        if newCoords[0][0] == newCoords[1][0]:
            for x in range(int(newCoords[0][1])+1,int(newCoords[1][1])): #create range for gap between coords
                newCoords.append([newCoords[0][0],str(x)]) # fill in gap 
        elif newCoords[0][1] == newCoords[1][1]: #all coords matching
            for x in range(int(newCoords[0][0])+1,int(newCoords[1][0])):
                newCoords.append([str(x),newCoords[0][1]])
       
        outCords.append(newCoords)

# print(outCords)

deDupeList = []
final_list = []

#dedupe list so when counting have a unique base
for x in outCords:
    for y in x:
        final_list.append(y)
        if y not in deDupeList:
            deDupeList.append(y)


list_with_2 = []

for x in deDupeList:
    if final_list.count(x) >= 2: #add all those with 2 or more count into list
        list_with_2.append(x)

print(len(list_with_2)) #count list length

# Answer = 4541 INCORRECT