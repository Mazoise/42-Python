import sys

morse_dict = {
    'A':	'.-',
    'B':	'-...',
    'C':	'-.-.',
    'D':	'-..',
    'E':	'.',
    'F':	'..-.',
    'G':	'--.',
    'H':	'....',
    'I':	'..',
    'J':	'.---',
    'K':	'-.-',
    'L':	'.-..',
    'M':	'--',
    'N':	'-.',
    'O':	'---',
    'P':	'.--.',
    'Q':	'--.-',
    'R':	'.-.',
    'S':	'...',
    'T':	'-',
    'U':	'..-',
    'V':	'...-',
    'W':	'.--',
    'X':	'-..-',
    'Y':	'-.--',
    'Z':	'--..',
    '0':	'-----',
    '1':	'.----',
    '2':	'..---',
    '3':	'...--',
    '4':	'....-',
    '5':	'.....',
    '6':	'-....',
    '7':	'--...',
    '8':	'---..',
    '9':	'----.'
}


def last_word():
    if (word_len != len(arg.split()) - 1 or arg_len != len(sys.argv) - 2):
        return False
    return True


for arg_len, arg in enumerate(sys.argv[1::]):
    if ''.join(arg.split()).isalnum():
        for word_len, word in enumerate(arg.split()):
            for i in word:
                print(morse_dict[i.upper()], end=" ")
            if (last_word() is False):
                print('/', end=' ')
    else:
        print("ERROR")
        exit()
if len(sys.argv) > 1:
    print()
