# Create a program that calculates the Fibonacci sequence up to the Nth term.
# Ask the user to enter the Nth term and have the program calculate the sequence
# until it has printed that many terms.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def fib_input(nth_count):
    fib_list = [0, 1]

    for x in range(1, nth_count - 1):
        # calc next value
        new_val = fib_list[x] + fib_list[x - 1]
        # print(new_val)
        fib_list.append(new_val)
        # append next value to list
    return fib_list

print(fib_input(9))
