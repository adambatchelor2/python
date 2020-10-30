

# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

intIn = 1652
intStr = str(intIn)
intLen = len(intStr)
y = 0

for x in range(0,intLen):
    y += int(intStr[x])**intLen
print( y==intIn)
