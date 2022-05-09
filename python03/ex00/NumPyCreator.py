import numpy as np
from random import random
import warnings

class NumPyCreator:

    def from_list(self, lst):
        try:
            assert type(lst) == list
            warnings.filterwarnings("error", category=np.VisibleDeprecationWarning)
            return np.array(lst)
        except:
            return None

    def from_tuple(self, tpl):
        try:
            assert type(tpl) == tuple
            warnings.filterwarnings("error", category=np.VisibleDeprecationWarning)
            return np.array([i for i in tpl])
        except:
            return None

    def from_iterable(self, itr):
        try:
            it = iter(itr)
            warnings.filterwarnings("error", category=np.VisibleDeprecationWarning)
            return np.array([i for i in it])
        except:
            return None

    def from_shape(self, shape, value=0):
        try:
            warnings.filterwarnings("error", category=np.VisibleDeprecationWarning)
            return np.full(shape, value)
        except:
            return None

    def random(self, shape):
        try:
            warnings.filterwarnings("error", category=np.VisibleDeprecationWarning)
            return np.array([random() for i in range(shape[0] * shape[1])]).reshape(shape)
        except:
            return None

    def identity(self, n):
        try:
            warnings.filterwarnings("error", category=np.VisibleDeprecationWarning)
            return np.identity(n)
        except:
            return None
