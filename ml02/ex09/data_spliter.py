import numpy as np


def data_spliter(x, y, proportion):
    """Shuffles and splits the dataset (given by x and y) into a
       training and a test set, while respecting the given proportion
       of examples to be kept in the training set.
    Args:
        x: has to be an numpy.array, a matrix of dimension m * n.
        y: has to be an numpy.array, a vector of dimension m * 1.
        proportion: has to be a float, the proportion of the dataset
        that will be assigned to the training set.
    Return:
        (x_train, x_test, y_train, y_test) as a tuple of numpy.array
        None if x or y is an empty numpy.array.
        None if x and y do not share compatible dimensions.
        None if x, y or proportion is not of expected type.
    Raises:
        This function should not raise any Exception.
    """
    if (type(x) != np.ndarray or type(y) != np.ndarray
       or len(x) == 0 or len(y) == 0
       or type(proportion) != float or proportion < 0 or proportion > 1
       or x.shape[0] != y.shape[0]):
        print("TypeError in data_spliter")
        return None
    try:
        shuffled_values = np.concatenate((x, y), axis=1)
        np.random.shuffle(shuffled_values)
        x_train = shuffled_values[:int(x.shape[0] * proportion), : -1]
        x_test = shuffled_values[int(x.shape[0] * proportion):, : -1]
        y_train = shuffled_values[:int(y.shape[0] * proportion), -1]
        y_test = shuffled_values[int(y.shape[0] * proportion):, -1]
        return (x_train, x_test, y_train, y_test)
    except Exception as e:
        print("Error in data_spliter: ", e)
        return None
