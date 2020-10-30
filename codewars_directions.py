a = ['NORTH', 'EAST']

lat = 0
ver = 0
outStr = []
ver_dict = {"NORTH":1,"SOUTH":-1}
lat_dict = {"EAST":1,"WEST":-1}

for x in a:
    if x in lat_dict:
        lat += lat_dict[x]
    if x in ver_dict:
        ver += ver_dict[x]

if ver>0:
    for x in range(0,abs(ver)):
        outStr.append("NORTH")
else:
    for x in range(0, abs(ver)):
        outStr.append("SOUTH")
if lat>0:
    for x in range(0,abs(lat)):
        outStr.append("EAST")
else:
    for x in range(0, abs(lat)):
        outStr.append("WEST")

print(outStr)