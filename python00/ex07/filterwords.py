import sys
import re


if len(sys.argv) != 3:
    print("ERROR")
    exit()
try:
    nb = int(sys.argv[2])
except ValueError:
    print("ERROR")
    exit()
list = re.split(r'\W+', sys.argv[1])
newlist = [i for i in list if len(i) > nb]
print(newlist)
