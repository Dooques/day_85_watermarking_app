from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import *
from PIL import Image, ImageDraw, ImageFont


def create_text():
    path = open_file().name
    print(path)
    with Image.open(path).convert("RGBA") as base:
        w_mark = get_watermark()
        if w_mark is None:
            return None
        print(f'watermark: {w_mark}')
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
        out.show()


# def get_image():


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


def open_file():
    path = filedialog.askopenfile(mode='r')
    return path


def get_watermark():
    watermark = w_mark_var.get()
    print(len(watermark))
    if len(watermark) == 0:
        messagebox.showinfo(title='Watermark Error',
                            message='No watermark found.')
        return None
    print(f'watermark got: {watermark}')
    return watermark


# window_x = 1080
# window_y = 720
#
# print(int(window_x * 0.5), int(window_y * 0.75))

window = Tk()
window.title('Watermarking App')
window.geometry()
window.config(padx=20, pady=20)

label = Label(text='Welcome to the watermarking application,\n'
                   'please type your watermark into the box\n'
                   'and choose a file using the button below', width=40)
label.grid(column=0, row=0, rowspan=2)
w_mark_label = Label(text='Watermark:', justify='right', width=10)
w_mark_label.grid(column=1, row=0)
w_mark_var = StringVar()
w_mark_entry = Entry(width=20)
w_mark_entry['textvariable'] = w_mark_var
w_mark_entry.grid(column=2, row=0, pady=2)
get_file_btn = Button(text='Get File', command=create_text, padding=2, width=20)
get_file_btn.grid(column=2, row=1)
#
# canvas = Canvas(width=int(window_x * 0.5), height=int(window_y * 0.5))
# image = Image.open('assets/jazzy.jpg')
# ph_img = PhotoImage('assets/jazzy.png')
# canvas.create_image(int(window_x * 0.25), int(window_y * 0.25), image=ph_img)
# canvas.grid(column=3, row=0, rowspan=2)

window.mainloop()
