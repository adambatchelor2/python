from itertools import zip_longest
  
  
x =[1, 2, 3, 4, 5, 6, 7]
y =[8, 9, 10]
z = list(zip_longest(x, y))
print(z)