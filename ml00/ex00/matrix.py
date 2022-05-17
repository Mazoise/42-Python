from copy import deepcopy as cp


class Matrix:

    def __init__(self, data):
        if (type(data) == tuple):
            try:
                assert all(type(x) == int and x > 0 for x in data), "Shape should only include positive integers"
                if len(data) > 2:
                    assert sum(x > 1 for x in data) <= 2, "Shape too large to be a matrix"
                    data = (filter(x > 1 for x in data))
                    print(data)
            except AssertionError as e:
                print("Error :", e)
                return
        elif type(data) == list:
            try:
                for i in data:
                    if type(i) != float:
                        raise TypeError("data must be floats")
                self.data = data
                self.shape = (1, len(self.data))
            except TypeError:
                try:
                    if len(data) > 0:
                        self.shape = (len(data), len(data[0]))
                    for i in data:
                        if type(i) != list or len(i) != self.shape[1]:
                            raise TypeError("data must be lists of floats")
                        for j in i:
                            if type(j) != float:
                                raise TypeError("data must be\
 lists of floats")
                    self.data = data
                except TypeError:
                    raise TypeError("data must be int, range,\
 list of floats or list of lists of floats")
        else:
            raise TypeError("data must be int, range,\
 list of floats or list of lists of floats")

    # def __add__(self, rhs):
    #     if type(rhs) == Vector and self.shape == rhs.shape:
    #         ret = cp(self)
    #         for i, s in enumerate(rhs.data):
    #             if type(s) == float:
    #                 ret.data[i] += s
    #             else:
    #                 for j in range(len(s)):
    #                     ret.data[i][j] += s[j]
    #         return ret
    #     else:
    #         raise ValueError("Vectors must have the same shape")

    # def __radd__(self, lhs):
    #     return self + lhs

    # def __sub__(self, rhs):
    #     if type(rhs) == Vector and self.shape == rhs.shape:
    #         ret = cp(self)
    #         for i, s in enumerate(rhs.data):
    #             if type(s) == float:
    #                 ret.data[i] -= s
    #             else:
    #                 for j in range(len(s)):
    #                     ret.data[i][j] -= s[j]
    #         return ret
    #     else:
    #         raise ValueError("Vectors must have the same shape")

    # def __rsub__(self, lhs):
    #     return self - lhs  # happens only if value error

    # def __mul__(self, rhs):
    #     try:
    #         ret = cp(self)
    #         for i, s in enumerate(ret.data):
    #             if type(s) == float:
    #                 ret.data[i] *= rhs
    #             else:
    #                 for j in range(len(s)):
    #                     ret.data[i][j] *= rhs
    #         return ret
    #     except TypeError:
    #         print("Can't multiply vector by non-scalar")

    # def __rmul__(self, lhs):
    #     return self * lhs

    # def __truediv__(self, rhs):
    #     try:
    #         ret = cp(self)
    #         for i, s in enumerate(ret.data):
    #             if type(s) == float:
    #                 ret.data[i] /= rhs
    #             else:
    #                 for j in range(len(s)):
    #                     ret.data[i][j] /= rhs
    #         return ret
    #     except TypeError:
    #         print("Can't divide vector by non-scalar")

    # def __rtruediv__(self, lhs):
    #     raise ValueError("A scalar cannot be divided by a Vector")

    # def __str__(self):
    #     return str(self.data)

    # def __repr__(self):
    #     return str(self.data)

    # def dot(self, rhs):
    #     ret = 0
    #     if type(rhs) == Vector and self.shape == rhs.shape:
    #         for i in range(self.shape[1]):
    #             if type(self.data[i]) == float:
    #                 ret += self.data[i] * rhs.data[i]
    #             else:
    #                 for j in range(self.shape[0]):
    #                     ret += self.data[j][i] * rhs.data[j][i]
    #         return ret
    #     else:
    #         raise ValueError("Vectors must have the same shape")

    # def T(self):  # reverse shape of vector
    #     ret = []
    #     for i in range(self.shape[1]):
    #         if self.shape[1] == 1:
    #             for j in range(self.shape[0]):
    #                 ret.append(self.data[j][i])
    #         else:
    #             if self.shape[0] == 1:
    #                 ret.append([self.data[i]])
    #             else:
    #                 ret.append([self.data[j][i]
    #                            for j in range(self.shape[0])])
    #     return Vector(ret)
