import os, sys
from PIL import Image, ImageDraw, ImageFont, PSDraw

file_name = 'jazzy.png'
# with Image.open(f'assets/{file_name}') as img:
#     img.load()
#     converted_img = img.transpose(Image.Transpose.ROTATE_90)
#     # converted_img.show()
#     rotated_img = img.rotate(45, expand=True)
#     rotated_img.show()

# with Image.open(f'assets/{file_name}') as img:
#     img.load()
    # cmyk_img = img.convert('CMYK')
    # gray_img = img.convert("L")
    # # gray_img.show()
    # print(img.getbands())
    # print(cmyk_img.getbands())
    # print(gray_img.getbands())
    # red, green, blue = img.split()
    # zeroed_band = red.point(lambda _: 0)
    # red_merge = Image.merge(
    #     "RGB", (red, zeroed_band, zeroed_band)
    # )
    # green_merge = Image.merge(
    #     "RGB", (zeroed_band, green, zeroed_band)
    # )
    # blue_merge = Image.merge(
    #     "RGB", (red, zeroed_band, blue)
    # )
    # blue_merge.show()
    # blue_merge.save('assets/jazzy_purple.jpg')

with Image.open(f'assets/{file_name}') as img:
    img.load()
    title = "hopper"
    box = (1 * 72, 2 * 72, 7 * 72, 10 * 72)  # in points

    ps = PSDraw.PSDraw()  # default is sys.stdout or sys.stdout.buffer
    ps.begin_document(title)

    # draw the image (75 dpi)
    ps.image(box, img, 75)
    ps.rectangle(box)

    # draw title
    ps.setfont("HelveticaNarrow-Bold", 36)
    ps.text((3 * 72, 4 * 72), title)

    ps.end_document()


