from hashlib import new
import numpy as np


class ColorFilter:

    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        try:
            ret = np.copy(array)
            for line in ret:
                for pixel in line:
                    for i in range(3):
                        pixel[i] = 255 - pixel[i]
            return ret
        except Exception:
            return None

    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        try:
            new_shape = (np.shape(array)[0], np.shape(array)[1], 2)
            zero_array = np.zeros(new_shape, dtype=int)
            return(np.dstack((zero_array, array[:, :, 2:])))
        except Exception:
            return None

    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        try:
            ret = np.copy(array)
            for line in ret:
                for pixel in line:
                    pixel[0] = 0
                    pixel[2] = 0
            return ret
        except Exception:
            return None

    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        try:
            ret = np.copy(array)
            ret = ret - self.to_blue(array) - self.to_green(array)
            if np.shape(array)[2] == 4:
                ret[:, :, 3] = array[:, :, 3]
            return ret
        except Exception:
            return None

    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
            celluloid filter is also known as cel-shading or toon-shading.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        try:
            ret = np.copy(array)
            trucs = np.linspace(0, 255, num=4, endpoint=False)
            for line in ret:
                for pixel in line:
                    for i in range(3):
                        for m in trucs[::-1]:
                            if pixel[i] > m:
                                pixel[i] = m
                                break
            return ret
        except Exception:
            return None

    def to_grayscale(self, array, filter, weight=None):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = ’mean’/’m’: performs the mean of RBG channels.
        For filter = ’weight’/’w’: performs a weighted mean of RBG channels.
        Args:
            array: numpy.ndarray corresponding to the image.
            filter: string with accepted values in [’m’,’mean’,’w’,’weight’]
            weights: [args] list of 3 floats where the sum equals to 1,
                corresponding to the weights of each RBG channels.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        """
        try:
            ret = np.copy(array[:, :, 0])
            if filter is 'm' or filter is 'mean':
                for i, line in enumerate(array):
                    for j, pixel in enumerate(line):
                        ret[i][j] = sum(pixel[0:3]) / 3
                ret = np.dstack((ret, ret, ret))
                return (ret if np.shape(array)[2] == 3
                        else np.dstack((ret, array[:, :, 3])))
            elif filter is 'w' or filter is 'weight' or filter is 'weighted':
                if sum(weight) > 1.00000000001 or sum(weight) < 0.999999999:
                    return None
                for i, line in enumerate(array):
                    for j, pixel in enumerate(line):
                        ret[i][j] = sum(pix * coeff for pix, coeff
                                        in zip(pixel, weight))
                ret = np.dstack((ret, ret, ret))
                return (ret if np.shape(array)[2] == 3
                        else np.dstack((ret, array[:, :, 3])))
            else:
                return None
        except TypeError:
            return None
