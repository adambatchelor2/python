# Ask the user to enter a number and have the program find the next prime number
# after that value. If you don’t remember, a prime number is a number which can
# only be divided by 1 and itself. Thus if the user enters 3, have the program find
# the next prime number (5) and print it out.

#loop through odd numbers - ignore even

def primeTest(integer):
    x=2
    while x < integer:
        #print(x)
        if integer % x == 0:
            return False
            #break
        else:
            x+=1
    return True


def nextPrime(integer):
    integer += 1
    while True:
        if primeTest(integer):
            return integer
        else:
            integer += 1


inNumber = 50
print(nextPrime(inNumber))