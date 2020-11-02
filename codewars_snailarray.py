
# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# expected = [1,2,3,6,9,8,7,4,5]

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

print(array[0][0])
# array[1].pop(1)
# array.pop(0)

outList = []

for x in array[0]:
    outList.append(x)
array.pop(0)
current_height = len(array)
current_width = len(array[0])
print('current height {} and width ')
for x in range(0,len(array)):
    print(array[x][current_width])

print(array)
print(len(array))
print(outList)
