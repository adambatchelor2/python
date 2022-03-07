

def foo(list):
    new_list = sum([float(x) for x in list])
    return new_list


listy = ['2.3','2.4']

print(foo(listy))