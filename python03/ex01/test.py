from ImageProcessor import ImageProcessor
import PIL

imp = ImageProcessor()
try:
    arr = imp.load("non_existing_file.png")
    print(arr)
except FileNotFoundError:
    print("File not found")

try:
    arr = imp.load("empty_file.png")
    print(arr)
except PIL.UnidentifiedImageError as e:
    print(e)

arr = imp.load("42AI.png")
print(arr)
imp.display(arr)
