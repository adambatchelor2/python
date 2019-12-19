

waffleCount = int(input("How many waffles each? "))

peopleCount = int(input("How many in your family? "))

wafflesInPack = 10


wafflesWeNeed = waffleCount * peopleCount

packsNeeded = wafflesWeNeed / wafflesInPack

print ("We need " + str(wafflesWeNeed) + " waffles and that is " + str(packsNeeded) + " packs")
