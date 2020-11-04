
# solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"

# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python

listIn = [1,4,3]
listIn.sort()
outlist = []

for x in range(0,len(listIn)-1):
    if listIn[x] == listIn[x+1]-1:
        print(listIn[x])

