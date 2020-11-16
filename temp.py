


def unique_in_order(strIn):

    # listOut = [x for i,x in enumerate(strIn) if strIn[i+1] != strIn[i]]
    listOut = []

    for i,x in enumerate(strIn):
        if strIn[i+1] != strIn[i]:
            listOut.append(x)
        print(listOut)
    return listOut


print (unique_in_order('AAAABBBCCDAABBB'))