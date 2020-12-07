
def tri_recursion(k):
  if(k>0):
    print(k)
    result = k+tri_recursion(k-1) #loops through at this point until - at 1 k-1 = 0 so result = 0 and 1+0 = 1
    print(result)
  else:
    result = 0
  return result

tri_recursion(6)