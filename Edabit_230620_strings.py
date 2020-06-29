# coding=utf-8
# Create a function that returns true if a given inequality expression is correct and false otherwise.
# correct_signs("3 < 7 < 11") ➞ True
# correct_signs("13 > 44 > 33 > 1") ➞ False
# correct_signs("1 < 2 < 6 < 9 > 3") ➞ True
import re
import math

inStr = "3 < 7 < 11"

splitList = re.split('\s', inStr)
print (splitList)

for x in range(0,math.ceil(len(splitList)/2.5)):

    firstChar = 0+x
    comparison= 1+x
    secondChar = 2+x

    if splitList[comparison] == '<':
        if splitList[firstChar] < splitList[secondChar]:
            print(True)
        else:
            print(False)
    else:
        if splitList[firstChar] > splitList[secondChar]:
            print(True)
        else:
            print(False)