import numpy as np


def zscore(x):
    """Computes the normalized version of a non-empty numpy.array
       using the z-score standardization.
    Args:
        x: has to be an numpy.array, a vector.
    Return:
        x’ as a numpy.array.
        None if x is a non-empty numpy.array or not a numpy.array.
        None if x is not of the expected type.
    Raises:
        This function shouldn’t raise any Exception.
    """
    if (type(x) != np.ndarray or len(x) == 0):
        print("TypeError in zscore")
        return None
    try:
        print(np.std(x))
        print(np.mean(x))
        return (x - np.mean(x)) / np.std(x)
    except Exception as e:
        print("Error in zscore: ", e)
        return None
