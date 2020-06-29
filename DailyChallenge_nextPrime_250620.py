# Ask the user to enter a number and have the program find the next prime number
# after that value. If you don’t remember, a prime number is a number which can
# only be divided by 1 and itself. Thus if the user enters 3, have the program find
# the next prime number (5) and print it out.

#loop through odd numbers - ignore even

def primeTest(integer):
    x=2
    while x < integer:
        if integer % x == 0:
            return False
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

inNumber = int(input("Enter value to find next prime..."))
nextInt = nextPrime(inNumber)
print(f"Your next prime number is {nextInt}")