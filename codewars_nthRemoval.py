order = [1,2,1,3,4,1,2,1,2,3]
nth = 1

outList = []
uniqDict = {}

for x in order:
    if x not in uniqDict:
        uniqDict[x]=0
    uniqDict[x] += 1

    if uniqDict[x] <= nth:
        outList.append(x)

print(uniqDict)
print(outList)
