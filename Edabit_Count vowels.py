#Count vowels

# count_vowels("Celebration") ➞ 5

# count_vowels("Palm") ➞ 1

# count_vowels("Prediction") ➞ 4

str_vowel = "ADA"
count = 0

vowels = ["a","e","i","o","u"]
for x in range(0,len(str_vowel)):
	if str_vowel[x].lower() in vowels:
		count += 1

print (count)