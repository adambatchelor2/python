
# solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"

#'-63,-62,-60,-58,-56,-55,-53--50,-47,-45--43,-40,-39,-36

# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python

listIn = [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
listIn.sort()
print(listIn)
# print(listIn)
cumList = []
x = 0
y = 0
# for x in range(0,len(listIn)-1):
#

while x <= len(listIn)-1:
    if x==0 or x==len(listIn)-1: #first or last entry
        cumList.append(listIn[x])
    #print("first {} - second {} - third {}".format(listIn[x - 1], listIn[x], listIn[x + 1]))
    elif (listIn[x] == listIn[x + 1] - 1) and (listIn[x] == listIn[x - 1] + 1):
        # listIn[x] = '-'
        cumList.append('-')
    else:
        cumList.append(listIn[x])
    x +=1


while y <= len(cumList)-1: #pop double '-'
    if cumList[y]=='-' and cumList[y+1]=='-':
        cumList.pop(y)
        y -= 1
    y += 1

y =0
print(cumList)

while y <= len(cumList)-2:
    print(str(y) + ' ' + str(len(cumList)))
    if cumList[y+1]=='-':

        cumList[y] = str(cumList[y]) + cumList[y+1] + str(cumList[y+2])
        cumList.pop(y+1)
        cumList.pop(y+1)
        print(cumList)
    y += 1

outStr = ''

for x in cumList:
    outStr +=','+str(x)

print(outStr[1:])
