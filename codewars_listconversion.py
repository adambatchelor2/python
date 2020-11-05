
# solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"

# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python

listIn = [1,4,3,5,7,9,10,12,13]
listIn.sort()
print(listIn)
# print(listIn)
outlist = []
cumList = []
x = 0
y = 0
# for x in range(0,len(listIn)-1):
#

while x <= len(listIn)-1:
    # print(x)
    if x==0:
        if listIn[x] != listIn[x + 1] - 1:
            outlist.append(listIn[x])
    elif x==len(listIn)-1:
        if (listIn[x] != listIn[x - 1] + 1):
            outlist.append(listIn[x])
        else:
            cumList.append(listIn[x])
    elif (listIn[x] != listIn[x + 1] - 1) and (listIn[x] != listIn[x - 1] + 1):
        outlist.append(listIn[x])
    elif (listIn[x] == listIn[x + 1] - 1) or (listIn[x] == listIn[x - 1] + 1):
        cumList.append(listIn[x])
    # print("first {} - second {} - third {}".format(listIn[x - 1],listIn[x],listIn[x + 1]))
    x +=1

print(outlist)
print(cumList)


