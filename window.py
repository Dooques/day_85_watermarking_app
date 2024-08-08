from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import *
from PIL import Image, ImageDraw, ImageFont, ImageTk


class WindowFunctions:
    def __init__(self):
        pass

    def check_length(self, w_mark):
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

    def get_watermark(self):
        watermark = w_mark_var.get()
        print(len(watermark))
        if len(watermark) == 0:
            messagebox.showinfo(title='Watermark Error',
                                message='No watermark found.')
            return None
        print(f'watermark got: {watermark}')
        return watermark

    def create_label(self):
        label = Label(image=self.get_image())
        return label

