# Suppose you have a guest list of students and the country they are from, stored as key-value pairs in a dictionary.


# Write a function that takes in a name and returns a name tag, that should read:

# "Hi! I'm [name], and I'm from [country]."
# If the name is not in the dictionary, return:

# "Hi! I'm a guest."




def find_guest(name_guest, name_list):

	if name_guest in name_list:
		return ("Hi! I'm "+name_guest+", and I'm from "+name_list[name_guest])
	else:
		return("Hi! I'm a guest.")


GUEST_LIST = {
"Randy": "Germany",
"Karla": "France",
"Wendy": "Japan",
"Norman": "England",
"Sam": "Argentina"
}

print(find_guest('Randy',GUEST_LIST))


