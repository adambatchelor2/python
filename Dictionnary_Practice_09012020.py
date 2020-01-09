

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict) #print dict

thisdict["year"] = 2018 #change value

print(thisdict['brand']) #print one element

for x in thisdict: #dict loop
  print(thisdict[x])

for x in thisdict.values():
	print(x)

for x, y in thisdict.items():
  print(x, y)

  if "year" in thisdict:
  	print("Yes it is")

print(len(thisdict))

thisdict["color"] = "red"  #add element

thisdict.pop("model") #remove element

del thisdict #delete dict
thisdict.clear() #clears dict


# Nested dict
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print (myfamily["child1"]) #bring back the nested dict
print (myfamily["child1"]["name"])

# thisdict = dict(brand="Ford", model="Mustang", year=1964) #build a new dict