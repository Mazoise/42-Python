
from itertools import count


import string
import re


def text_analyzer(*kwargs):
    """This function counts the number of upper characters,\
 lower characters, punctuation and spaces in a given text."""
    if len(kwargs) == 0:
        print("What is the text to analyse?")
        arg = input()
    elif len(kwargs) > 1:
        print("ERROR")
        return
    else:
        arg = kwargs[0]
    repunct = re.compile('[%s]' % string.punctuation)
    respace = re.compile('[%s]' % string.whitespace)
    print("The text contains", len(arg), "characters:")
    print("-", sum(map(str.isupper, arg)), "upper letters")
    print("-", sum(map(str.islower, arg)), "lower letters")
    print("-", len(re.findall(repunct, arg)), "punctuation marks")
    print("-", len(re.findall(respace, arg)), "spaces")
