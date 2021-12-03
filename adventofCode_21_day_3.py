
with open("aoc_2021_3.txt", 'r', encoding="utf8") as f:
    data = f.read()

y = data.split("\n")
y2 = y

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

# oxygen

for z in range(0,13): #loop through each column
    sum = 0
    for x in y: #loop through each item in list
        sum = sum + int(x[z]) #sum the column for each item in list

    if sum >= (len(y)/2): #if greater than half the count 1 must be dominant
        y = [item for item in y if item[z] == '1']
          
    else:
        y = [item for item in y if item[z] == '0']
    if len(y) == 1:
        #print(y)
        break

print (y) 

#CO2

for z in range(0,13): #loop through each column
    sum = 0
    for x in y2: #loop through each item in list
        sum = sum + int(x[z]) #sum the column for each item in list
    if sum >= (len(y2)/2): #if greater than half the count 1 must be dominant
        y2 = [item for item in y2 if item[z] == '0'] 
    else:
        y2 = [item for item in y2 if item[z] == '1']

    if len(y2) == 1:
        #print(y)
        break
print(y2)

print(int(y[0],2) * int(y2[0],2))





