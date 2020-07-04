# Create a program that calculates the Fibonacci sequence up to the Nth term.
# Ask the user to enter the Nth term and have the program calculate the sequence
# until it has printed that many terms.
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

import matplotlib.pyplot as plt

def fib_input(nth_count):
    fib_list = [0, 1]

    for x in range(1, nth_count - 1):
        # calc next value
        new_val = fib_list[x] + fib_list[x - 1]
        # print(new_val)
        fib_list.append(new_val)
        # append next value to list
    return fib_list

def plot_line_chart(list_val,item_count):

    x = [x for x in range(item_count)]
    y = list_val

    plt.plot(x, y)
    plt.title('Fibonacci')
    plt.show()


def plot_col_chart(list_val,item_count):

    # x-coordinates of left sides of bars
    left = [x for x in range(item_count)]

    # heights of bars
    height = list_val

    # labels for bars
    #tick_label = ['one', 'two', 'three', 'four', 'five']

    # plotting a bar chart
    plt.bar(left, height, width=0.8, color=['red', 'green']) #tick_label=tick_label,

    plt.title('My bar chart!')

    # function to show the plot
    plt.show()

nth_count = int(input("How many do you want?"))
fib_out = (fib_input(nth_count))

fib_line_plot = plot_line_chart(fib_out,nth_count)

fib_col_plot = plot_col_chart(fib_out,nth_count)