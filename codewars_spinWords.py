
strTest = 'i love horses'

def loop_through(inStr):
    word_list = inStr.split()
    for x,word in enumerate(word_list):
        if len(word) >= 5:
            word_list[x] = word[::-1]

    return ' '.join(map(str, word_list))

print(loop_through(strTest))