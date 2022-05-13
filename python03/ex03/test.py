from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter


def test_each(file_name, weight):
    imp = ImageProcessor()
    arr = imp.load(file_name)
    cf = ColorFilter()
    # imp.display(arr)
    # imp.display(cf.invert(arr))
    # imp.display(cf.to_green(arr))
    # imp.display(cf.to_blue(arr))
    # imp.display(cf.to_red(arr))
    # imp.display(cf.to_celluloid(arr))
    imp.display(cf.to_grayscale(arr, 'm'))
    imp.display(cf.to_grayscale(arr, 'weighted', weight))


test_each("elon_canaGAN.png", [0, 0, 1])
test_each("logo.png", [0, 1, 0])
