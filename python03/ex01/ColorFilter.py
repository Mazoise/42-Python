import numpy as np

class ColorFilter:

    def invert(self, array):
        for line in array:
            for pixel in line:
                for l in range(3):
                    pixel[l] = 1.0 - pixel[l]
    def to_blue(self, array):
        for line in array:
            for pixel in line:
                pixel[0] = 0.0
                pixel[1] = 0.0
    def to_green(self, array):
        for line in array:
            for pixel in line:
                pixel[0] = 0.0
                pixel[2] = 0.0
    def to_red(self, array):
        for line in array:
            for pixel in line:
                pixel[1] = 0.0
                pixel[2] = 0.0
    def celluloid(self, array, dev):
        trucs = np.linspace(0.0, 1.0, num=dev, endpoint=False)
        for line in array:
            for pixel in line:
                for l in range(3):
                    for m in trucs[::-1]:
                        if pixel[l] > m:
                            pixel[l] = m
                            break
