def coords(str):

    b = str.split(" -> ")
    newlist = []

    for x in b:
        x = x.split(",")
        newlist.append(x)

    cord1 = [newlist[0][0],newlist[0][1]]
    cord2 = [newlist[1][0],newlist[1][1]]

    return([cord1,cord2])

a = '424,924 -> 206,706'

print(coords(a))