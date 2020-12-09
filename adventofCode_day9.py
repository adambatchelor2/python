
with open("aoc9.txt", 'r', encoding="utf8") as f:
    data = f.read()

y = data.split("\n")
z = []
for x in y:
    z.append(int(x))

print(z)
# pre_amble = 25
# pre_list = []

# Part 1
# def pre_check(listIn, valIn):
#     for x in listIn:
#         if (valIn-x) in listIn and valIn-x != valIn:
#             return "True"
#     return "False"
#
# final_list = []
# for x in range(pre_amble,len(z)):
#
#     final_list.append([z[x],pre_check(z[x-pre_amble:pre_amble+(x-pre_amble)],z[x])])
#
#
# for a in final_list:
#     if a[1]=='False':
#         print (a[0])

pre_amble = 0

#Part 2
def pre_check(listIn, valIn):
    # print([listIn,valIn])
    y = 0
    for x in listIn:
        # print(x)
        y+=x
    # print(['final',y])
    if y == valIn:
        return "True"
    return "False"

final_list = []
for a in range(2,20):

    pre_amble = a
    final_list = []
    for x in range(pre_amble,len(z)):
        final_list.append([z[x],pre_check(z[x-pre_amble:pre_amble+(x-pre_amble)],1492208709),x])

    for c in final_list:
        if c[1]=='True' :
            print ([c[0],c[2],pre_amble])




