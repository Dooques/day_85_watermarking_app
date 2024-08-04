from PIL import Image, ImageDraw, ImageFont
from tkinter import *
from tkinter import ttk


def create_text(w_mark):
    with Image.open("assets/jazzy.jpg").convert("RGBA") as base:
        txt_size = (base.size[0] * 2, base.size[1] * 2)
        txt = Image.new("RGBA", txt_size, (255, 255, 255, 0))
        fnt_size = 50
        fnt = ImageFont.truetype("arial.ttf", fnt_size)
        d = ImageDraw.Draw(txt)
        w_m_length = check_length(w_mark)
        txt_cols = txt_size[0] // w_m_length
        txt_rows = txt_size[1] // fnt_size
        w_m_print = ""
        for y in range(0, txt_rows):
            for x in range(0, txt_cols):
                w_m_print += w_mark + " "
            w_m_print += "\n\n"
        d.multiline_text((0, 0), w_m_print, font=fnt, fill=(255, 255, 255, 128))
        txt = txt.rotate(45)
        txt = txt.crop((txt_size[0] * 0.25, txt_size[1] * 0.25,
                        txt_size[0] * 0.75, txt_size[1] * 0.75))
        out = Image.alpha_composite(base, txt)
        return out


def check_length(w_mark):
    upper = 35
    lower = 25
    length_list = []
    for item in w_mark:
        if item.isupper():
            length_list.append(upper)
        else:
            length_list.append(lower)
    total_length = 0
    for item in length_list:
        total_length += item
    return total_length


tk = Tk()
tk.title('Watermarking App')
tk.configure(width=1080, height=720)
tk.frame()
label = Label(text='This is a label')
label.pack()
btn = Button(text='Button')
btn.pack()
check_button = Checkbutton(text='Check')
check_button.pack()

tk.mainloop()


# watermark = 'dooques'
# watermarked_image = create_text(watermark)
# watermarked_image.show()
