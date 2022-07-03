import numpy as np


def vec_log_loss_(y, y_hat, eps=1e-15):
    """
    Compute the logistic loss value.
    Args:
        y: has to be an numpy.ndarray, a vector of shape m * 1.
        y_hat: has to be an numpy.ndarray, a vector of shape m * 1.
        eps: epsilon (default=1e-15)
    Returns:
        The logistic loss value as a float.
        None on any error.
    Raises:
        This function should not raise any Exception.
    """
    if (type(y) is not np.ndarray or type(y_hat) is not np.ndarray
       or len(y.shape) != 2 or len(y_hat.shape) != 2
       or y.shape[1] != 1 or y_hat.shape[1] != 1
       or y.shape[0] != y_hat.shape[0]):
        print("TypeError in log_loss")
        return None
    try:
        ones = np.ones((y.shape[0], 1))
        return (-(y.T.dot(np.log(y_hat + eps))
                + (ones - y).T.dot(np.log(ones - y_hat + eps)))
                / y.shape[0]).squeeze()
    except Exception as e:
        print("Error in log_loss", e)
        return None
