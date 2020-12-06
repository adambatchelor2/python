def permutations(string):
    from itertools import permutations
    perm = permutations(list(string))

    inList = list(perm)
    outList = []
    outList = list(set([''.join(x) for x in inList]))

    return(outList)

print(permutations('anirbas '))