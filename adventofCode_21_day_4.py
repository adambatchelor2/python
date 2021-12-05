def listtocombo(a_list):
        
    final_list = []

    for b in a_list:
        c = b.split(' ')
        final_list.append(list(filter(None, c))) #remove blanks

    morelist = []

    for a in range(0,len(final_list[0])):
        addlist = []
        for x in final_list:
            addlist.append(x[a])
        morelist.append(addlist)

    return(morelist + final_list)

def intersect_len(lst1, lst2):
    return len(list(set(lst1) & set(lst2)))


with open("aoc_2021_4.txt", 'r', encoding="utf8") as f:
    data = f.read()

y = data.split("\n\n")

bingo_order = y[0].split(",")
y.pop(0)

print("Bingo order = {}".format(bingo_order))

card_list = []

# create all combinations of horizontal and vertical squares

for x in y:
    card = listtocombo(x.split("\n")) #general list of all possible combos
    # print(x)
    a = 0
    for x in range(5,len(bingo_order)+1):
        z = bingo_order[:x]
        final_val = z[-1:]
        if a == 1:
            break
        # loop through card lists
        for op in card:
                
            if intersect_len(z,op) == 5:
                print("We have a winner {} from {} last val {} current call".format(op,x,final_val),z)
                a = 1

# need to work out all 5 digit combos of bingo calls
# then test which intersects first




# We have a winner ['75', '8', '98', '94', '34'] from 23 last val ['8']