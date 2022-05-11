import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


class ImageProcessor():

    def load(self, path):
        im = Image.open(path)
        result = np.array(im)
        print("Loading image of dimensions :",
              np.shape(result)[0], "x",
              np.shape(result)[1])
        return result

    def display(self, array):
        imgplot = plt.imshow(array)
        plt.show()
