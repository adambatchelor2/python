#The volume of a spherical shell is the difference between the enclosed volume of the outer 
#sphere and the enclosed volume of the inner sphere:

#Volume of Inner Sphere Formula - 4/3 * pie (R squared - r cubed)   - where R is outer circle radius and r is inner circle radius

#Create a function that takes r1 and r2 as arguments and returns the volume of a spherical shell rounded to the nearest thousandth.

import math

def get_shell(r1,r2):

	if r1 > r2:
		volume_shell = (4/3)*math.pi*((r1*r1*r1)-(r2*r2*r2))
	else:
		volume_shell = (4/3)*math.pi*((r2*r2*r2)-(r1*r1*r1))
	return round(volume_shell,3)

print (get_shell(2,7))