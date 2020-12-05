# 16 -->  1 + 6 = 7
# 942 -->  9 + 4 + 2 = 15 -->  1 + 5 = 6

test = 16

def num_check(intIn):
    y = 0
    for x in list(str(intIn)):
        y += int(x)
    return y

def loopIt(intIn):
    while len(str(intIn)) > 1:
        intIn = num_check(intIn)
    return intIn

print(loopIt(942))