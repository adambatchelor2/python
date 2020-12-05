
# Move the first letter of each word to the end of it,
# then add "ay" to the end of the word. Leave punctuation marks untouched.

str = "Pig in a dog."
strOut = ""

strList = str.split(" ")
for x in strList:
    print(x)
    strOut += x[2:]+x[0:2]+"ay"

print(strOut)