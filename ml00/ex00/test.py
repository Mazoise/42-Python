from matrix import Matrix
from vector import Vector
from numpy import matlib


print("----- MATRIX TESTS -----")

m1 = Matrix((1, 4))
print("TEST 1 : v1 = Matrix([[0.0], [1.0], [2.0], [3.0]])")
v1 = Matrix([[0.0], [1.0], [2.0], [3.0]])
print(str(v1))
print(v1.shape)
print("TEST 2 : v1 / 2.0")
print(str(v1 / 2.0))
print("TEST 3 : 3.0 / v1")
try:
    print(str(3.0 / v1))
except ValueError as e:
    print("ValueError :", e)
print("TEST 4 : v2 = ")
v2 = Matrix((3, 6))
print(str(v2))
print(v2.shape)
print("TEST 5 : v1 * 4")
print(str(v1 * 4))
try:
    print("TEST 6 : Matrix(6)")
    print(Matrix(6).data)
    print(Matrix(6).shape)
except TypeError as e:
    print("TypeError :", e)
try:
    print("TEST 7 : Matrix([0.0, 1.0, 2.0, 3.0])")
    print(Matrix([0.0, 1.0, 2.0, 3.0]).data)
    print(Matrix([0.0, 1.0, 2.0, 3.0]).shape)
except TypeError as e:
    print("TypeError :", e)
print("TEST 8 : v1 + v2")
try:
    print(v1 + v2)
except ValueError as e:
    print("ValueError :", e)
print("TEST 9 : v1 + v1 * 2")
print(str(v1 + v1 * 2))
print("TEST 10 : v1.T()")
print(" => BEFORE")
print(str(v1))
print(v1.shape)
print(" => AFTER")
print(str(v1.T()))
print(v1.T().shape)
print("TEST 11 : v2.T()")
print(" => BEFORE")
print(str(v2))
print(v2.shape)
print(" => AFTER")
print(str(v2.T()))
print(v2.T().shape)

print("\n----- VECTOR TESTS -----")

print("TEST 1 : v1 = Vector([[0.0], [1.0], [2.0], [3.0]])")
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
print(str(v1))
print(v1.shape)
print("TEST 2 : v1 / 2.0")
print(str(v1 / 2.0))
print("TEST 3 : 3.0 / v1")
try:
    print(str(3.0 / v1))
except ValueError as e:
    print("ValueError :", e)
print("TEST 4 : v2 = Vector([0.0, 1.0, 2.0, 3.0])")
v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
print(str(v2))
print(v2.shape)
print("TEST 5 : v2 * 4")
print(str(v2 * 4))
print("TEST 6 : Vector(6)")
try:
    print(Vector(6).data)
    print(Vector(6).shape)
except TypeError as e:
    print("TypeError :", e)
print("TEST 7 : Vector((3, 6))")
try:
    print(Vector((3, 6)).data)
    print(Vector((3, 6)).shape)
except ValueError as e:
    print("ValueError :", e)
print("TEST 8 : v1 + v2")
try:
    print(v1 + v2)
except ValueError as e:
    print("ValueError :", e)
print("TEST 9 : v1 + v1 * 2")
print(str(v1 + v1 * 2))
print("TEST 10 : v1.T()")
print(" => BEFORE")
print(str(v1))
print(v1.shape)
print(" => AFTER")
print(str(v1.T()))
print(v1.T().shape)
print("TEST 11 : v2.T()")
print(" => BEFORE")
print(str(v2))
print(v2.shape)
print(" => AFTER")
print(str(v2.T()))
print(v2.T().shape)
print(type(v2.T()))
print("TEST 12 : v1.dot(v1)")
print(str(v1.dot(v1)))
print("TEST 13 : v2.dot(v2)")
print(str(v2.dot(v2)))
