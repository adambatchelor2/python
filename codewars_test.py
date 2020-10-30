

# alphabet_position("The sunset sets at twelve o' clock.")

def alphabet_position(strIn):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    myDict = {}
    outStr = ''
    strIn = strIn.lower()

    for x in range(0,len(alpha)):
        myDict[alpha[x]] = x+1

    for x in range(0,len(strIn)):
        if strIn[x] in myDict:
            outStr += ' ' + str(myDict[strIn[x]])
    return outStr.lstrip()

print(alphabet_position("The sunset sets at twelve o' clock."))