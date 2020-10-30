
# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
def high(x):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    myDict = {}
    fin_score = 0

    for a in range(0,len(alpha)):
        myDict[alpha[a]] = a+1

    strList = x.split()

    for x in strList:
        z = 0
        for y in range(0,len(x)):
            z += myDict[x[y]]
        print(z)
        if z > fin_score:
            outStr = x
            fin_score = z
    return outStr

print(high('wrvxgcq winpgily'))