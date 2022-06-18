from copy import deepcopy as cp


class Matrix:

    def __init__(self, data):
        if (type(data) == tuple):
            try:
                assert all(type(x) == int and x > 0 for x in data),\
                        "Shape should only include positive integers"
                if len(data) > 2:
                    assert sum(x > 1 for x in data) <= 2,\
                           "Shape too large to be a matrix"
                self.shape = tuple(filter(lambda x: x > 1, data))
                if len(self.shape) == 1:
                    self.shape = (1, self.shape[0])
                self.data = [[0.0 for x in range(self.shape[1])]
                             for y in range(self.shape[0])]
            except AssertionError as e:
                print("Error :", e)
                return
        elif type(data) == list:
            self.data = data
            if type(data[0]) == list:
                self.shape = (len(data), len(data[0]))
            for i in data:
                if type(i) != list or len(i) != self.shape[1]:
                    raise TypeError("data must be a list of lists of floats")
                for j in i:
                    if type(j) != float:
                        raise TypeError("data must be a \
 list of lists of floats")
        else:
            raise TypeError("data must be a tuple or list")

    def __add__(self, rhs):
        from vector import Vector
        if ((type(rhs) == Matrix
            or type(rhs) == Vector)
           and self.shape == rhs.shape
           and type(rhs) == type(self)):
            ret = cp(self)
            for i, s in enumerate(rhs.data):
                if type(s) == float:
                    ret.data[i] += s
                else:
                    for j in range(len(s)):
                        ret.data[i][j] += s[j]
            return ret
        else:
            raise ValueError("Matrix must have the same shape")

    def __radd__(self, lhs):
        return self + lhs

    def __sub__(self, rhs):
        from vector import Vector
        if ((type(rhs) == Matrix
            or type(rhs) == Vector)
           and self.shape == rhs.shape
           and type(rhs) == type(self)):
            ret = cp(self)
            for i, s in enumerate(rhs.data):
                if type(s) == float:
                    ret.data[i] -= s
                else:
                    for j in range(len(s)):
                        ret.data[i][j] -= s[j]
            return ret
        else:
            raise ValueError("Matrix must have the same shape")

    def __rsub__(self, lhs):
        return self - lhs  # happens only if value error

    def __mul__(self, rhs):
        try:
            ret = cp(self)
            for i, s in enumerate(ret.data):
                if type(s) == float:
                    ret.data[i] *= rhs
                else:
                    for j in range(len(s)):
                        ret.data[i][j] *= rhs
            return ret
        except TypeError:
            print("Can't multiply matrix by non-scalar")

    def __rmul__(self, lhs):
        return self * lhs

    def __truediv__(self, rhs):
        try:
            ret = cp(self)
            for i, s in enumerate(ret.data):
                if type(s) == float:
                    ret.data[i] /= rhs
                else:
                    for j in range(len(s)):
                        ret.data[i][j] /= rhs
            return ret
        except TypeError:
            print("Can't divide matrix by non-scalar")

    def __rtruediv__(self, lhs):
        raise ValueError("A scalar cannot be divided by a Matrix")

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)

    def T(self):  # reverse shape of matrix
        from vector import Vector
        ret = []
        for i in range(self.shape[1]):
            ret.append([self.data[j][i] for j in range(self.shape[0])])
        if type(self) == Vector:
            return Vector(ret)
        else:
            return Matrix(ret)
