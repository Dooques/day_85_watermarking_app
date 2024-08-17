from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import *
from PIL import Image, ImageDraw, ImageFont, ImageTk


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
        label_size = 23
        button_size = 21

        # Canvas Settings
        self.canvas_frame = Frame(self.window)
        self.canvas = Canvas(self.window, bd=0, bg='black', highlightthickness=0, relief='ridge')
        self.canvas_temp = Canvas(self.window, bd=0, bg='black', highlightthickness=0, relief='ridge')
        self.canvas_temp.grid(column=1, columnspan=3, row=0, sticky='nesw')
        self.image = None
        self.tk_image = None
        self.path = None
        self.image_height = None
        self.image_width = None
        self.event_width = None
        self.event_height = None

        # Watermark Settings
        self.font_types = {'Arial': 'arial', 'Impact': 'impact', 'Times New Roman': 'times', 'Lucida Sans':
                           'l_10646', 'Courier New': 'cour'}
        self.selected_font = "arial"
        self.font_size = 40
        print(self.font_types)
        print(self.selected_font)
        self.rotation = 45
        self.transparency = 128
        self.repeating = True
        self.repetition_spread = None

        # Watermark Widgets

        # Instruction Label
        self.label = Label(self.settings_frame, text='Welcome to the watermarking app, please choose a file using the'
                                                     ' button below and type your watermark into the box',
                           width=50, compound='left',
                           wraplength=260)
        self.label.pack(pady=20)
        self.get_file_btn = Button(self.settings_frame, text='Get File',
                                   command=self.open_file,
                                   padding=5, width=button_size,
                                   compound='left')
        self.get_file_btn.pack()

        # Watermark Creation
        self.w_m_frame = Frame(self.settings_frame)
        self.w_m_label = Label(self.w_m_frame,
                               text='Watermark:',
                               justify='right',
                               width=label_size,
                               compound='left')
        self.w_m_label.pack()

        self.w_m_var = StringVar()
        self.w_m_entry = Entry(self.w_m_frame, width=label_size)
        self.w_m_entry['textvariable'] = self.w_m_var
        self.w_m_entry.pack()
        self.w_m_frame.pack(pady=20)

        # Fonts
        self.font_frame = Frame(self.settings_frame)

        # Font Menu
        self.option_var = StringVar()
        self.starting_key = list(self.font_types.keys())
        self.option_var.set(self.starting_key[0])
        self.font_menu = OptionMenu(self.font_frame,
                                    self.option_var,
                                    self.starting_key[0],
                                    *self.font_types,
                                    command=self.set_font)
        self.font_menu.pack(pady=10)

        # Font Size
        self.font_label = Label(self.font_frame, text=f'Font Size: {self.font_size}')
        self.font_label.pack()

        self.font_scale = Scale(self.font_frame,
                                command=self.set_font_size,
                                from_=20, to=400,
                                value=50)
        self.font_scale.pack(pady=10)
        self.font_frame.pack(pady=10)

        # Rotation
        self.rotation_frame = Frame(self.settings_frame)
        self.rotation_frame.pack(pady=10)
        self.rotation_label = Label(self.rotation_frame, text=f'Rotation: {self.rotation}')
        self.rotation_label.pack()
        self.rotation_scale = Scale(self.settings_frame,
                                    command=self.set_rotation,
                                    from_=0, to=180,
                                    value=45)
        self.rotation_scale.pack()

        # Transparency
        self.transparency_frame = Frame(self.settings_frame)
        self.transparency_label = Label(self.transparency_frame, text=f'Transparency: {self.transparency}')
        self.transparency_label.pack(pady=5)
        self.transparency_scale = Scale(self.transparency_frame,
                                        command=self.set_transparency,
                                        from_=0, to=255,
                                        value=128)
        self.transparency_scale.pack()
        self.transparency_frame.pack(pady=20)

        # Set repeats
        self.type_variable = IntVar()
        self.watermark_repeat = Radiobutton(self.settings_frame,
                                            text='Repeating Watermark',
                                            command=self.set_type,
                                            value=0,
                                            variable=self.type_variable)
        self.watermark_repeat.pack()
        self.watermark_single = Radiobutton(self.settings_frame,
                                            text='Single Watermark',
                                            command=self.set_type,
                                            value=1,
                                            variable=self.type_variable)
        self.watermark_single.pack()

        # Confirm
        self.w_m_confirm = Button(self.settings_frame,
                                  text='Confirm Watermark',
                                  command=self.check_type,
                                  padding=5, width=button_size,
                                  compound='left')
        self.w_m_confirm.pack(pady=10)

        # Save File
        self.save_to_file = Button(self.settings_frame,
                                   text='Save to File',
                                   command=self.save_to_file,
                                   padding=5, width=button_size)
        self.save_to_file.pack()

        self.canvas_frame.grid(column=1, row=0, sticky='nsew')
        self.settings_frame.grid(column=0, row=0, sticky='nsew')

    def save_to_file(self):
        types = [('JPG File', '*.jpg'),
                 ('All Files', '*.*')]
        file_path = filedialog.asksaveasfilename(title='Save Watermarked File',
                                                 defaultextension='*.jpg',
                                                 initialdir='.',
                                                 filetypes=types)
        print(file_path)
        if file_path.endswith(('tagData', 'jpg')):
            print('converting image')
            converted_image = self.image.convert('RGB')
            converted_image.save(file_path)
        else:
            messagebox.showerror(title='Saving Error',
                                 message='Please use a .jpg extension to save this file, other formats are not '
                                         'currently supported.')

    def check_type(self):
        if self.repeating:
            self.repeating_watermark()
        else:
            self.single_watermark()

    def set_type(self):
        type_ = self.type_variable.get()
        print(type_)
        if type_ == 0:
            self.repeating = True
        else:
            self.repeating = False

    def set_transparency(self, event):
        self.transparency = int(round(float(event), 0))
        self.transparency_label['text'] = f'Transparency: {self.transparency}'

    def set_rotation(self, event):
        self.rotation = int(round(float(event), 0))
        self.rotation_label['text'] = f'Rotation: {self.rotation}'
        print(f'rotation: {self.rotation}')

    def set_font(self, event):
        self.selected_font = self.font_types[event]
        print(f'font value: {self.font_types[event]}')

    def set_font_size(self, event):
        self.font_size = int(round(float(event), 0))
        self.font_label['text'] = f'Font Size: {self.font_size}'

    def open_file(self):
        selected_path = filedialog.askopenfile(mode='r')
        if selected_path:
            self.path = selected_path
        else:
            return None
        print(self.path)
        if self.path:
            self.process_file()

    def process_file(self):
        self.image = Image.open(self.path.name)
        self.canvas_temp.destroy()
        self.get_image()

    def get_image(self):
        if self.event_width:
            image = self.image.resize((self.image_width, self.image_height))
            self.tk_image = ImageTk.PhotoImage(image)
            self.canvas.create_image(self.event_width / 2, self.event_height / 2, image=self.tk_image, anchor='center')
        else:
            image = self.image
            self.tk_image = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, image=self.tk_image, anchor='nw')
        self.canvas.grid(column=1, columnspan=3, row=0, sticky='nesw')
        self.canvas.bind('<Configure>', self.resize_image)

    def check_length(self):
        upper = 35
        lower = 25
        length_list = []
        for item in self.w_m_var.get():
            if item.isupper():
                length_list.append(upper)
            else:
                length_list.append(lower)
        total_length = 0
        for item in length_list:
            total_length += item
        return total_length

    def resize_image(self, event):
        canvas_ratio = event.width / event.height
        image_ratio = self.image.size[0] / self.image.size[1]
        self.event_width = event.width
        self.event_height = event.height
        print('event_size: ', event.width, event.height)
        print('image_size: ', self.image.size[0], self.image.size[1])
        print(f'image_ratio: {image_ratio}')
        if canvas_ratio < image_ratio:
            self.image_width = int(event.width)
            self.image_height = int(self.image_width / image_ratio)
        else:
            self.image_height = int(event.height)
            self.image_width = int(self.image_height * image_ratio)
        print(f'New_size: {self.image_height, self.image_width}')
        image = self.image.resize((self.image_width, self.image_height))
        self.tk_image = ImageTk.PhotoImage(image)
        self.canvas.create_image(int(event.width / 2),
                                 int(event.height / 2),
                                 anchor='center',
                                 image=self.tk_image)

    def repeating_watermark(self):
        if self.image is None:
            messagebox.showerror(title='Image Error',
                                 message='No valid image found, please select an image file.')
            return None
        else:
            pass
        with Image.open(self.path.name).convert("RGBA") as base:
            w_mark = self.w_m_var.get()
            print(w_mark)
            if len(w_mark) < 1:
                messagebox.showerror('Watermark Error',
                                     'Please enter a valid watermark.')
                return None
            print(f'watermark: {w_mark}')
            txt_size = (base.size[0] * 2, base.size[1] * 2)
            txt = Image.new("RGBA", txt_size, (255, 255, 255, 0))

            print(round(self.font_size, 0))
            fnt_size = self.font_size
            font_selected = f"{self.selected_font}.ttf"
            print(font_selected)
            fnt = ImageFont.truetype(font=f'assets/{font_selected}', size=fnt_size)

            d = ImageDraw.Draw(txt)

            w_m_length = self.check_length()
            txt_cols = txt_size[0] // w_m_length
            txt_rows = txt_size[1] // fnt_size
            w_m_print = ""
            for y in range(0, txt_rows):
                for x in range(0, txt_cols):
                    w_m_print += w_mark + " "
                w_m_print += "\n\n"

            d.multiline_text((0, 0), w_m_print, font=fnt, fill=(255, 255, 255, self.transparency))
            txt = txt.rotate(self.rotation)
            txt = txt.crop((txt_size[0] * 0.25, txt_size[1] * 0.25,
                            txt_size[0] * 0.75, txt_size[1] * 0.75))

            self.image = Image.alpha_composite(base, txt)
            self.get_image()

    def single_watermark(self):
        if self.path is None:
            messagebox.showerror(title='Image Error',
                                 message='No valid image found, please select an image file.')
            return None
        else:
            pass
        with Image.open(self.path.name).convert("RGBA") as base:
            w_mark = self.w_m_var.get()
            print(w_mark)
            if len(w_mark) < 1:
                messagebox.showerror('Watermark Error',
                                     'Please enter a valid watermark.')
                return None
            print(f'watermark: {w_mark}')

            txt_box_size = (base.size[0], base.size[1])
            txt = Image.new("RGBA", txt_box_size, (255, 255, 255, 0))

            fnt_size = int(round(self.font_size, 0))
            print(round(self.font_size, 0))
            font_selected = f"{self.selected_font.lower()}.ttf"
            print(font_selected)
            fnt = ImageFont.truetype(font=f'assets/{font_selected}', size=fnt_size)

            d = ImageDraw.Draw(txt)

            text_pos = (base.size[0] * 0.6), (base.size[1] * 0.75)
            w_m_length = self.check_length()
            if text_pos[0] + w_m_length > base.size[0]:
                text_pos = (text_pos[0] - w_m_length, text_pos[1])
            print(f'image size: {base.size}')
            print(f'text pos: {text_pos}')

            d.text(xy=text_pos, text=w_mark, font=fnt,
                   fill=(255, 255, 255, self.transparency))
            self.image = Image.alpha_composite(base, txt)
            self.get_image()


Watermarker().window.mainloop()
