from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import *
from PIL import Image, ImageDraw, ImageFont, ImageTk
from window import WindowFunctions


window_func = WindowFunctions()


class Watermarker:
    def __init__(self):
        self.image_path = ""

        # Tk Window Setup
        self.window = Tk()
        self.window.geometry('1080x768')
        self.window.title('Watermarking App')
        self.window.config(padx=20, pady=20)
        self.window.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')
        self.window.rowconfigure(0, weight=1, uniform='a')

        # Frame
        self.settings_frame = Frame(self.window)

        self.label = Label(text='Welcome to the watermarking application,\n'
                           'please type your watermark into the box\n'
                           'and choose a file using the button below', width=40, compound='left')
        self.label.grid(column=0, row=0, rowspan=2)

        self.w_mark_label = Label(self.settings_frame, text='Watermark:', justify='right', width=10, compound='left')
        self.w_mark_label.pack()

        self.w_mark_var = StringVar()
        self.w_mark_entry = Entry(self.settings_frame, width=20)
        self.w_mark_entry['textvariable'] = self.w_mark_var
        self.w_mark_entry.pack()

        self.get_file_btn = Button(self.settings_frame, text='Get File', command=self.get_image, padding=2, width=20,
                                   compound='left')
        self.get_file_btn.pack()

        self.canvas = Canvas(self.window, bd=0, highlightthickness=0, relief='ridge')
        self.image = None
        self.tk_image = None

        self.settings_frame.grid(column=0, row=0, sticky='nsew')

    def get_image(self):
        path = filedialog.askopenfile(mode='r')
        self.image = Image.open(path.name)
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, image=self.tk_image, anchor='nw')
        self.canvas.grid(column=1, columnspan=3, row=0, sticky='nesw')
        self.canvas.bind('<Configure>', self.resize_image)

    def resize_image(self, event):
        canvas_ratio = event.width / event.height
        image_ratio = self.image.size[0] / self.image.size[1]
        print('event_size: ', event.width, event.height)
        print('image_size: ', self.image.size[0], self.image.size[1])
        print(f'image_ratio: {image_ratio}')
        if canvas_ratio < image_ratio:
            width = int(event.width)
            height = int(width / image_ratio)
        else:
            height = int(event.height)
            width = int(height * image_ratio)
        print(f'New_size: {height, width}')
        self.image = self.image.resize((width, height))
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(int(event.width / 2),
                                 int(event.height / 2),
                                 anchor='center',
                                 image=self.tk_image)

    def create_text(self):
        path = self.image_path
        if path:
            path = path.name
        print(path)
        with Image.open(path).convert("RGBA") as base:
            w_mark = window_func.get_watermark()
            if w_mark is None:
                return None
            print(f'watermark: {w_mark}')
            txt_size = (base.size[0] * 2, base.size[1] * 2)
            txt = Image.new("RGBA", txt_size, (255, 255, 255, 0))
            fnt_size = 50
            fnt = ImageFont.truetype("arial.ttf", fnt_size)
            d = ImageDraw.Draw(txt)
            w_m_length = window_func.check_length(w_mark)
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


Watermarker().window.mainloop()
