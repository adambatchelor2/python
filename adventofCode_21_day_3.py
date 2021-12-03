
with open("aoc_2021_3 test.txt", 'r', encoding="utf8") as f:
    data = f.read()

y = data.split("\n")


# #Part 1

# outList = []

# for z in range(0,len(y[0])):
#     #print(str(z) + " list")   
#     sum = 0
#     for x in y:
#         sum = sum + int(x[z])
#     outList.append(sum)

# gamma = ''

# for a in outList:
#     if a > (len(y)/2):
#         gamma = gamma + '1'
#     else:
#         gamma = gamma + '0'

# epsilon = ''
# for b in outList:
#     if b < (len(y)/2):
#         epsilon = epsilon + '1'
#     else:
#         epsilon = epsilon + '0'

# print(int(gamma,2) * int(epsilon,2))


#Part 2

# Discard numbers not matching criteria
# Stop when one number left
# Otherwise keep going right
# Most common valu keep

outList = []

# pop from list if != popular character

for z in range(0,1): #loop through each column
#for z in range(0,len(y[0])): #loop through each column    
    #print(str(z) + " list")   
    sum = 0
    for x in y: #loop through each item in list
        sum = sum + int(x[z]) #sum the column for each item in list
    print("Sum is " + str(sum))
    if sum > (len(y)/2): #if greater than half the count 1 must be dominant
        #while x:
            if x[z] == '1':
                y.remove(x)
    else:
        for x in y:
            if x[z] == '0':
                outList.append(x)
print (y)  






