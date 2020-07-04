import re

def vowelCount(sting):
    vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for x in vowels:  # dict loop
        vowels[x] = strIn.count(x)
    return (vowels)

def uniqueCharacter(string):
    unique = []
    string = re.findall("[a-z]", string)  # just letters

    for x in range(0, len(string)):
        if string[x] not in unique:
            unique.append(string[x])
    return sorted(unique)

strIn = input("Enter a sentence..")

strLength = len(strIn)
vowel_Count = vowelCount(strIn)
uniqueChar = uniqueCharacter(strIn)
CountUniqueChar = len(uniqueChar)

print("-----STRING ANALYSIS-----")
print(f"There are {strLength} characters in the sentence")
print(f"And these are counts of each vowel: {vowel_Count}")
print(f"Overall there are {CountUniqueChar} unique characters and these are {uniqueChar}")

