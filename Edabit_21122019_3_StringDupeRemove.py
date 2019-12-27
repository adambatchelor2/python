#Write a function that takes a string, and returns a new string with any duplicate consecutive letters removed.
#i.e. Streeeeeetch to Stretch

#def removeDupe(inStr):
#	for x in range (1,inStr.length)


inStr = ("SSStreeeeeeetcch")

instr_list = list(set([x*2 for x in inStr]))

for x in instr_list:
	while inStr.find(x) != -1:
		inStr = inStr[:inStr.find(x)]+inStr[inStr.find(x)+1:]
		
print(inStr)


# def unstretch(word):
# 	instr_list = list(set([x*2 for x in word]))

# 	for x in instr_list:
# 		while word.find(x) != -1:
# 			inStr = word[:word.find(x)]+word[word.find(x)+1:]
# 	return word

# print(unstretch("Teeeeest"))