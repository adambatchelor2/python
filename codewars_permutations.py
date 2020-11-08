# https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python
# In this kata you have to create all permutations of an input string and remove duplicates
# ,if present. This means, you have to shuffle all letters from the input in all possible orders.
# permutations('a');  # ['a']
# permutations('ab');  # ['ab', 'ba']
# permutations('aabb');  # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

instr = 'abc'
strLen = len(instr)

listOut = []
y = ''

listOut.append(instr[0]+instr[1]+instr[2])


print(listOut)
# 123 abc
# 213 bac
# 321 cba
# 312 cab
# 231 bca
# 132 acb

