from PIL import Image

im = Image.open('assets/jazzy.jpg')
print(im.format, im.size, im.mode)
