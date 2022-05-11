import numpy as np


class ScrapBooker():

    def crop(self, array, dimensions, position):
        """
        Crops the image as a rectangle via dim arguments
        (being the new height and width of the image)
        from the coordinates given by position arguments.
        Args:
            array: numpy.ndarray
            dim: tuple of 2 integers.
            position: tuple of 2 integers.
        Returns:
            new_arr: the cropped numpy.ndarray.
            None otherwise
            (combinaison of parameters not incompatible).
        Raises:
            This function should not raise any Exception.
        """
        try:
            assert (type(dimensions) == tuple and len(dimensions) == 2
                    and type(dimensions[0]) == int
                    and type(dimensions[1]) == int
                    and type(position) == tuple and len(position) == 2
                    and type(position[0]) == int
                    and type(position[1]) == int
                    and type(array) == np.ndarray)
            return (array[position[0]:dimensions[0]
                    + position[0], position[1]:dimensions[1] + position[1]])
        except Exception:
            return None

    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis
        (0: vertical, 1: horizontal)
        Args:
            array: numpy.ndarray.
            n: non null positive integer lower than the number of
            row/column of the array
            (depending of axis value).
            axis: positive non null integer.
        Returns:
            new_arr: thined numpy.ndarray.
            None otherwise (combinaison of parameters not incompatible).
        Raises:
            This function should not raise any Exception.
        """
        try:
            return np.delete(array, np.arange(n - 1,
                                              array.shape[axis], n), axis)
        except Exception:
            return None

    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
            array: numpy.ndarray.
            n: positive non null integer.
            axis: integer of value 0 or 1.
        Returns:
            new_arr: juxtaposed numpy.ndarray.
            None otherwise (combination of parameters not incompatible).
        Raises:
            This function should not raise any Exception.
        """
        try:
            return np.concatenate([array] * n, axis)
        except Exception:
            return None

    def mosaic(self, array, dimensions):
        """
        Makes a grid with multiple copies of the array.
        The dim argument specifies
        the number of repetition along each dimensions.
        Args:
            array: numpy.ndarray.
            dim: tuple of 2 integers.
        Returns:
            new_arr: mosaic numpy.ndarray.
            None otherwise (combinaison of parameters not incompatible).
        Raises:
            This function should not raise any Exception.
        """
        try:
            return np.tile(array, (dimensions[0], dimensions[1], 1))
        except Exception:
            return None
