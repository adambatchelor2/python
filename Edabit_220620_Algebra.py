#https://edabit.com/challenge/NNhkGocuPMcryW7GP

# Imagine a circle and two squares: a smaller and a bigger one. For the smaller one, the circle is a circumcircle
# and for the bigger one, an incircle. Create a function, that takes an integer (radius of the circle)
# and returns the difference of the areas of the two squares.

import math

radius = 6

big_square = (radius*2)*(radius*2)

#2 pi radians in circle
radians = (2*math.pi)/8

opp = (math.sin(radians))*radius

inner_square = (opp*2)*(opp*2)

print(round(big_square-inner_square))
