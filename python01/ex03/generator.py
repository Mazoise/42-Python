import sys
import string
import random


def shuffle(lst):
    for i in range(len(lst)):
        j = random.randint(0, len(lst) - 1)
        tmp = lst[i]
        lst[i] = lst[j]
        lst[j] = tmp
    return lst


def generator(text, sep=" ", option=None):
    '''Option is an optional arg, sep is mandatory'''
    if (type(text) != str
       or (option is not None and
           (option == "shuffle"
            or option == "unique"
            or option == "ordered") is False)):
        print("ERROR")
        return
    result = text.split(sep=sep)
    if option == "ordered":
        result.sort()
    elif option == "shuffle":
        shuffle(result)
    elif option == "unique":
        result = list(set(result))
    # print("Before")
    for word in result:
        # print("Word here", word)
        yield word
