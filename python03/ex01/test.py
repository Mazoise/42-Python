from ImageProcessor import ImageProcessor


imp = ImageProcessor()
try:
    arr = imp.load("non_existing_file.png")
    print(arr)
except FileNotFoundError:
    print("File not found")

