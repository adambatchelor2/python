
#"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
import re

str1 = "is2 Thi1s T4est 3a"
num = ['1','2','3','4','5','6','7','8','9']
mydict = {}
strOut = ''

for x in str1.split():
    word = ''
    for y in range(0,len(x)):
        if x[y] in num:
            intOut = int(x[y])
    mydict[intOut] = x
print(mydict)

for x in range(1, len(mydict)+1):
    strOut += ' ' + mydict[x]

print(strOut.lstrip())