# Factorial of a number i.e. 1*2*3
def fact(n):
    out = 1
    for x in range(1, n + 1):
        out *= x

    return out
