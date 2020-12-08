
with open("aoc8.txt", 'r', encoding="utf8") as f:
    data = f.read()

y = data.split("\n")
mydict = {}
mydict1 = {}

#Part 2
# for i,x in enumerate(y):
#     mydict[i] = [x[0:3],int(x[4:]),0]
#
# counter = 0
# acc = 0
#
# print(mydict)
#
# # while counter < 10:
# while mydict[counter][2] == 0:
#     print(['counter',counter])
#
#     if mydict[counter][0] == 'jmp':# and mydict[counter][2] == 0:
#         print(['Increment',mydict[counter][0],mydict[counter][1]])
#         mydict[counter] = [mydict[counter][0], mydict[counter][1], 1]
#         counter = counter+mydict[counter][1]
#
#     elif mydict[counter][0] == 'acc':
#         acc += mydict[counter][1]
#         mydict[counter] = [mydict[counter][0], mydict[counter][1], 1]
#         counter += 1
#     else: #mydict[counter][2] == 0:
#         mydict[counter] = [mydict[counter][0], mydict[counter][1], 1]
#         counter += 1
#
# print(acc)
# print(mydict)

#Part 2
for i, x in enumerate(y):
    mydict[i] = [x[0:3], int(x[4:]), 0,0]

counter = 0
acc = 0

for x in range(0,len(mydict)):

    for z in range(0, len(mydict)):
        mydict[z][2] = 0

    # print(['pre change',mydict])
    if mydict[x][0]=='jmp':
        mydict[x][0] = 'nop'
    elif mydict[x][0]=='nop':
        mydict[x][0] = 'jmp'

    acc = 0
    # print(['post',mydict])

    print(['refresh',mydict])
    # print(len(mydict)) 9
    while mydict[counter][2] == 0 or counter >= len(mydict):
        # print(['counter', counter])

        if mydict[counter][0] == 'jmp' and mydict[counter][1] != 0:  # and mydict[counter][2] == 0:
            mydict[counter] = [mydict[counter][0], mydict[counter][1], 1,acc]
            counter = counter + mydict[counter][1]
            print(acc)

        elif mydict[counter][0] == 'acc':
            acc += mydict[counter][1]
            mydict[counter] = [mydict[counter][0], mydict[counter][1], 1,acc]
            counter += 1
            print(acc)

        else:  # mydict[counter][2] == 0:
            mydict[counter] = [mydict[counter][0], mydict[counter][1], 1,acc]
            counter += 1
            print(acc)

    # print(mydict)

    if mydict[8][2] == 1: #if all measures hit then reset
        print(mydict)
        print (acc)
        break

    #reset to previous val
    if mydict[x][0]=='nop':
        mydict[x][0] = 'jmp'
    elif mydict[x][0]=='jmp':
        mydict[x][0] = 'nop'
