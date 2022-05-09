from ft_filter import ft_filter
from ft_map import ft_map
from ft_reduce import ft_reduce
import functools

print("FT_MAP :")
print(">> a = [1, 2, 3]")
a = [1, 2, 3]
print(">> ft_map(lambda x: x * 2, a) : ")
print(ft_map(lambda x: x * 2, a))
print(">> list(ft_map(lambda x: x * 2, a)) : ")
print(list(ft_map(lambda x: x * 2, a)))
print("\n>> map(lambda x: x * 2, a) : ")
print(map(lambda x: x * 2, a))
print(">> list(map(lambda x: x * 2, a)) : ")
print(list(map(lambda x: x * 2, a)))
print("\n>> x = [5, 3, 1, -1, -3, -5]")
b = [5, 3, 1, -1, -3, -5]
print(">> ft_map(lambda x: x + 1, b) : ")
print(ft_map(lambda x: x + 1, b))
print(">> list(ft_map(lambda x: x + 1, b)) : ")
print(list(ft_map(lambda x: x + 1, b)))
print("\n>> map(lambda x: x + 1, b) : ")
print(map(lambda x: x + 1, b))
print(">> list(map(lambda x: x + 1, b)) : ")
print(list(map(lambda x: x + 1, b)))
print("\n>> ft_map(lambda x: x + 1, []) : ")
print(ft_map(lambda x: x + 1, []))
print(">> list(ft_map(lambda x: x + 1, [])) : ")
print(list(ft_map(lambda x: x + 1, [])))
print("\n>> map(lambda x: x + 1, []) : ")
print(map(lambda x: x + 1, []))
print(">> list(map(lambda x: x + 1, [])) : ")
print(list(map(lambda x: x + 1, [])))
try:
    print("\n>> ft_map(None, b) : ")
    print(ft_map(None, b))
    print(">> list(ft_map(None, b)) : ")
    print(list(ft_map(None, b)))
except TypeError:
    print("TypeError")
try:
    print("\n>> map(None, b) : ")
    print(map(None, b))
    print(">> list(map(None, b)) : ")
    print(list(map(None, b)))
except TypeError:
    print("TypeError")
print("\nFT_FILTER :")
print(">> a = [1, 2, 3, 1, 2, 3, 1, 2, 3]")
a = [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(">> ft_filter(lambda x: x == 2, a) : ")
print(ft_filter(lambda x: x == 2, a))
print(">> list(ft_filter(lambda x: x == 2, a)) : ")
print(list(ft_filter(lambda x: x == 2, a)))
print("\n>> filter(lambda x: x == 2, a) : ")
print(filter(lambda x: x == 2, a))
print(">> list(filter(lambda x: x == 2, a)) : ")
print(list(filter(lambda x: x == 2, a)))
print("\n>> ft_filter(lambda x: x == 2, []) : ")
print(ft_filter(lambda x: x == 2, []))
print(">> list(ft_filter(lambda x: x == 2, [])) : ")
print(list(ft_filter(lambda x: x == 2, [])))
print("\n>> filter(lambda x: x == 2, []) : ")
print(filter(lambda x: x == 2, []))
print(">> list(filter(lambda x: x == 2, [])) : ")
print(list(filter(lambda x: x == 2, [])))
try:
    print("\n>> ft_filter(None, a) : ")
    print(ft_filter(None, a))
    print(">> list(ft_filter(None, a)) : ")
    print(list(ft_filter(None, a)))
except TypeError:
    print("TypeError")
try:
    print("\n>> filter(None, a) : ")
    print(filter(None, a))
    print(">> list(filter(None, a)) : ")
    print(list(filter(None, a)))
except TypeError:
    print("TypeError")

print("\nFT_REDUCE :")

print("lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']")
lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(">> ft_reduce(lambda x, y: x + y, lst) : ")
print(ft_reduce(lambda x, y: x + y, lst))
print(">> functools.reduce(lambda x, y: x + y, lst) : ")
print(functools.reduce(lambda x, y: x + y, lst))
print("\n>> a = [1, 2, 3, 4, 5]")
a = [1, 2, 3, 4, 5]
# b = [True, False, False, 1, [], 0]
print(">> ft_reduce(lambda x, y: x + y, a) : ")
print(ft_reduce(lambda x, y: x + y, a))
print(">> functools.reduce(lambda x, y: x + y, a) : ")
print(functools.reduce(lambda x, y: x + y, a))
try:
    print("\nft_reduce(lambda x, y: x + y, []) : ")
    print(ft_reduce(lambda x, y: x + y, []))
except TypeError:
    print("TypeError")
try:
    print("functools.reduce(lambda x, y: x + y, []) : ")
    print(functools.reduce(lambda x, y: x + y, []))
except TypeError:
    print("TypeError")
try:
    print("\n>> ft_reduce(lambda x, y: x + y, None) : ")
    print(ft_reduce(lambda x, y: x + y, None))
except TypeError:
    print("TypeError")
try:
    print(">> functools.reduce(lambda x, y: x + y, None) : ")
    print(functools.reduce(lambda x, y: x + y, None))
except TypeError:
    print("TypeError")
try:
    print("\n>> ft_reduce(None, a) : ")
    print(ft_reduce(None, a))
except TypeError:
    print("TypeError")
try:
    print(">> functools.reduce(None, a) : ")
    print(functools.reduce(None, a))
except TypeError:
    print("TypeError")
