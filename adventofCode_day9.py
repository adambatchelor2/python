
with open("aoc9.txt", 'r', encoding="utf8") as f:
    data = f.read()

y = data.split("\n")
z = []
for x in y:
    z.append(int(x))

pre_amble = 25
pre_list = []

def pre_check(listIn, valIn):
    for x in listIn:
        if (valIn-x) in listIn and valIn-x != valIn:
            return "True"
    return "False"

final_list = []
for x in range(pre_amble,len(z)):

    final_list.append([z[x],pre_check(z[x-pre_amble:pre_amble+(x-pre_amble)],z[x])])


for a in final_list:
    if a[1]=='False':
        print (a[0])