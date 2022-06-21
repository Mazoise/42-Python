import numpy as np


def add_intercept(x):
    """Adds a column of 1’s to the non-empty numpy.array x.
    Args:
        x: has to be an numpy.array, a vector or matrix.
    Returns:
        x as a numpy.array, a vector of shape m * 2.
        None if x is not a numpy.array.
        None if x is a empty numpy.array.
    Raises:
        This function should not raise any Exception.
    """
    if (type(x) != np.ndarray or len(x) == 0):
        return None
    try:
        return np.insert(x, 0, 1, axis=1).astype(float)
    except Exception:
        return None
