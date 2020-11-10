


# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
#
# What if the string is empty? Then the result should be empty object literal, {}.

strIn = "asdasda"
listIn = list(strIn)
listIn.sort()
dict = {}

for x in listIn:
    if x in dict:
        dict[x] += 1
    else:
        dict[x] = 1

print(dict)
# for x,i in dict.items():
#     print(x + str(i))