import os, sys
from PIL import Image

file_name = 'buildings.jpg'
# Loading file from Assets folder
with Image.open(f'assets/{file_name}') as img:
    img.load()
    print(img)
    print(type(img))
    print(img.format)
    print(img.size)
    print(img.mode)
    print(isinstance(img, Image.Image))
    # img.show()
    cropped_img = img.crop((683, 285, 1205, 760))
    print(cropped_img.size)
    # cropped_img.show()
    # low_res_img = cropped_img.resize(
    #     (cropped_img.width // 4, cropped_img.height // 4)
    # )
    low_res_img = cropped_img.reduce(4)
    # low_res_img.show()
    print('img_thumbnail')
    img.thumbnail((200,200))
    print(img.size)
    cropped_img.save('assets/cropped_image.jpg')
