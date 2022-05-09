import re
from typing import Type
from copy import deepcopy as cp


class Vector:

    def __init__(self, values):
        if type(values) == int or (type(values) == str and values.isdigit()):
            values = int(values)
            self.values = [[float(i)] for i in range(values)]
            self.shape = (values, 1)
        elif (type(values) == tuple and len(values) == 2
              and type(values[0]) == int
              and type(values[1]) == int):
            self.values = [[float(i)]
                           for i in range(values[0], values[1], 1
                           if values[0] < values[1] else -1)]
            self.shape = (len(self.values), 1)
        elif type(values) == list:
            try:
                for i in values:
                    if type(i) != float:
                        raise TypeError("Values must be floats")
                self.values = values
                self.shape = (1, len(self.values))
            except TypeError:
                try:
                    if len(values) > 0:
                        self.shape = (len(values), len(values[0]))
                    for i in values:
                        if type(i) != list or len(i) != self.shape[1]:
                            raise TypeError("Values must be lists of floats")
                        for j in i:
                            if type(j) != float:
                                raise TypeError("Values must be\
 lists of floats")
                    self.values = values
                except TypeError:
                    raise TypeError("Values must be int, range,\
 list of floats or list of lists of floats")
        else:
            raise TypeError("Values must be int, range,\
 list of floats or list of lists of floats")

    def __add__(self, rhs):
        if type(rhs) == Vector and self.shape == rhs.shape:
            ret = cp(self)
            for i, s in enumerate(rhs.values):
                if type(s) == float:
                    ret.values[i] += s
                else:
                    for j in range(len(s)):
                        ret.values[i][j] += s[j]
            return ret
        else:
            raise ValueError("Vectors must have the same shape")

    def __radd__(self, lhs):
        return self + lhs

    def __sub__(self, rhs):
        if type(rhs) == Vector and self.shape == rhs.shape:
            ret = cp(self)
            for i, s in enumerate(rhs.values):
                if type(s) == float:
                    ret.values[i] -= s
                else:
                    for j in range(len(s)):
                        ret.values[i][j] -= s[j]
            return ret
        else:
            raise ValueError("Vectors must have the same shape")

    def __rsub__(self, lhs):
        return self - lhs  # happens only if value error

    def __mul__(self, rhs):
        try:
            ret = cp(self)
            for i, s in enumerate(ret.values):
                if type(s) == float:
                    ret.values[i] *= rhs
                else:
                    for j in range(len(s)):
                        ret.values[i][j] *= rhs
            return ret
        except TypeError:
            print("Can't multiply vector by non-scalar")

    def __rmul__(self, lhs):
        return self * lhs

    def __truediv__(self, rhs):
        try:
            ret = cp(self)
            for i, s in enumerate(ret.values):
                if type(s) == float:
                    ret.values[i] /= rhs
                else:
                    for j in range(len(s)):
                        ret.values[i][j] /= rhs
            return ret
        except TypeError:
            print("Can't divide vector by non-scalar")

    def __rtruediv__(self, lhs):
        raise ValueError("A scalar cannot be divided by a Vector")

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return str(self.values)

    def dot(self, rhs):
        ret = 0
        if type(rhs) == Vector and self.shape == rhs.shape:
            for i in range(self.shape[1]):
                if type(self.values[i]) == float:
                    ret += self.values[i] * rhs.values[i]
                else:
                    for j in range(self.shape[0]):
                        ret += self.values[j][i] * rhs.values[j][i]
            return ret
        else:
            raise ValueError("Vectors must have the same shape")

    def T(self):  # reverse shape of vector
        ret = []
        for i in range(self.shape[1]):
            if self.shape[1] == 1:
                for j in range(self.shape[0]):
                    ret.append(self.values[j][i])
            else:
                if self.shape[0] == 1:
                    ret.append([self.values[i]])
                else:
                    ret.append([self.values[j][i]
                               for j in range(self.shape[0])])
        return Vector(ret)
