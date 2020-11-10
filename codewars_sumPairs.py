
# https://www.codewars.com/kata/54d81488b981293527000c8f/train/python

# Given a list of integers and a single sum value, return the first two values
# (parse from the left please) in order of appearance that add up to form the sum.

# sum_pairs([11, 3, 7, 5],10) - answer is 7 and 3 [7,3]

def sum_pairs(ints,s):
    myDict = {}

    for i,z in enumerate(ints):
        for j,y in enumerate(ints):
            if z + y == s and i!=j:
                if i > j:
                    myDict[i] = [y,z]
                else:
                    myDict[j] = [y,z]
    if len(myDict) > 0:
        temp = min(myDict.items())
        return temp[1]
    else:
        return None

print(sum_pairs([10, 5, 2, 3, 7, 5],10))