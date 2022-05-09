import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from ScrapBooker import ScrapBooker
from ColorFilter import ColorFilter
# from PIL import Image

class ImageProcessor():

    def load(self, path):
        im = mpimg.imread(path)
        result = np.array(im)
        print("Dimensions :", np.shape(result)[0], "X", np.shape(result)[1])
        return result
    # def display(self, array):

    def display(self, array):
        imgplot = plt.imshow(array, interpolation='nearest')
        plt.show()

im = ImageProcessor()
image = im.load("42AI.png")
scrap = ScrapBooker()
image = scrap.crop(image, (110, 110), (50, 50))
image = scrap.thin(image, 2, 0)
image = scrap.juxtapose(image, 1, 1)
image = scrap.mosaic(image, (12, 11))
image2 = im.load("elon.png")
cf = ColorFilter()
# cf.invert(image2)
# cf.to_blue(image2)
# cf.to_red(image2)
# cf.to_green(image2)
cf.celluloid(image2, 5)
im.display(image2)
