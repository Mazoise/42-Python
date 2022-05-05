from sqlite3 import Timestamp
from time import time, sleep


def ft_progress(lst):
    beg = time()
    for i in range(len(lst)):
        fract = i / len(lst)
        elapsed = time() - beg
        if fract:
            eta = elapsed / fract - elapsed
            print('\rETA: {0:.2f}s'.format(eta), end=' ')
        print('[{0:3.0f}%]'.format(fract * 100), end=' ')
        phrase = (("=" * (round(fract * 20) - 1)) + ">").ljust(20)
        print('[{0:20s}]'.format(phrase), end=' ')
        print(i + 1, '/', len(lst), end=' ')
        print('| elapsed time {0:.2f}s'.format(elapsed), end=' ')
        yield lst[i]
