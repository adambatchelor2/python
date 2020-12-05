
# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]

array = [[1,1,1,1],
         [2,2,2,2],
         [3,3,3,3],
         [4,4,4,4]]
# print(array[0][0])
# array[1].pop(1)
# array.pop(0)

outList = []

while len(array)>1:

    # Along the top
    for x in array[0]:
        outList.append(x)
    array.pop(0)

    current_height = len(array)
    current_width = len(array[0])

    # print('current height {0} and width {1}'.format(current_height,current_width))

    # Down the back
    for x in range(0,current_height):
        outList.append(array[x][current_width-1])
        array[x].pop(current_width-1)

    # Reverse the bottom list
    array[current_height-1].reverse()
    for x in array[current_height-1]:
        outList.append(x)
    array.pop(current_height-1)

    # up left side
    for x in range(current_height-2,0,-1):
        outList.append(array[x][0])
        array[x].pop(0)

if len(array)>0:
    for x in array[0]:
        outList.append(x)
    array.pop(0)

print(outList)
