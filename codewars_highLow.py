#high_and_low("1 2 3 4 5")  # return "5 1"

strIn = "1 2 3 11 4 5"

listy = strIn.split()

for x,i in enumerate(listy):
    listy[x] = int(i)

print(str(max(listy)) + ' ' + str(min(listy)))


