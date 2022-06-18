import re
from typing import Type
from copy import deepcopy as cp
from matrix import Matrix


class Vector(Matrix):

    def __init__(self, data):
        super(Vector, self).__init__(data)
        if self.shape[0] != 1 and self.shape[1] != 1:
            raise ValueError("Vector must have only 1 dimension")

    def dot(self, rhs):
        ret = 0
        if type(rhs) == Vector and self.shape == rhs.shape:
            for i in range(self.shape[1]):
                for j in range(self.shape[0]):
                    ret += self.data[j][i] * rhs.data[j][i]
            return ret
        else:
            raise ValueError("Vectors must have the same shape")
