from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *

# # Creating widgets within a frame grid
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
#
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()
#
# # Changing widget variables
# root = Tk()
# frm = ttk.Frame(root, padding=10)
#
# # Checking the functions of a widget
# btn = ttk.Button(frm)
# print(btn.configure().keys() - set(frm.configure().keys()))
# print(set(dir(btn)) - set(dir(frm)))
#
# # Setting values at time of object creation
# btn = Button(fg='red', bg='blue', text='Quit', command=root.destroy)
#
# # Changing individual values after object creation
# btn['fg'] = 'blue'
# btn['bg'] = 'red'
#
# # Changing Multiple values after creation
# btn.config(fg='white', bg='blue')
#
# # The packer is a geometry method that places widget objects inside a container
# btn.pack()
# btn.pack(side='left')
# btn.pack(expand=1)
# btn.pack(fill='x')
#
# print(btn.config())
# root.mainloop()


# Creating a class that controls application functions
# class App(Frame):
#     def __init__(self, master):
#         # App inherits functions from Frame
#         super().__init__(master)
#         self.pack()
#
#         # Create Entry object
#         self.entry_item = Entry()
#         self.entry_item.pack()
#
#         # Create the application variable
#         self.contents = StringVar()
#         # Set the value
#         self.contents.set("this is a variable")
#         # Tell the entry widget to watch this variable
#         self.entry_item['textvariable'] = self.contents
#
#         # Define a callback for when the user hits return
#         # It prints the current value of the variable
#         self.entry_item.bind('<Key-Return>', self.print_contents)
#
#     def print_contents(self, event):
#         print('Hi. The current entry content is: ', self.contents.get())
#
#
# root = Tk()
# myapp = App(root)
# myapp.mainloop()


# Controlling the Window Manager (Deprecated on Documentation?)
# I am using a method of controlling the window from the 100 Days of Python course.
# def turn_red(event):
#     event.widget['activeforeground'] = 'red'


# # create the application
# myapp = Tk()
# myapp.frame()
#
# # here are method calls to the window manager class
# myapp.title("My Do-Nothing Application")
# myapp.configure(width=1000, height=400)
# btn = Button(text='turn_red')
# btn.bind('<Enter>', turn_red)
# btn.pack(expand=True)
#
# # start the program
# myapp.mainloop()


# # Sample widgets
# sample_tk = Tk()
# sample_tk.title('Sample Widgets')
# sample_tk.configure(width=1080, height=720, padx=10, pady=10)
# sample_tk.frame()
#
# btn = Button(text='Button', padding=5)
# btn.pack()
#
# check_button = Checkbutton(text='Check', padding=5)
# check_button.pack()
#
# entry = Entry()
# entry.pack()
#
# frame = Frame()
# frame.pack()
#
# label = Label(text='This is a label', padding=5)
# label.pack()
#
# lbl_frame = LabelFrame(text='Label Frame')
# lbl_frame.pack()
#
# menu_b = Menubutton(text='Menu Button', padding=5)
# menu_b.pack()
#
# paned_window = PanedWindow()
# paned_window.pack()
#
# radio_btn = Radiobutton(text='Radio Button')
# radio_btn_2 = Radiobutton(text='2nd Button')
# radio_btn.pack()
# radio_btn_2.pack()
#
# label_scale = Label(text='Scale')
# label_scale.pack()
# scale = Scale()
# scale.pack()
#
# scroll_label = Label(text='Scroll')
# scroll = Scrollbar()
# scroll.pack()
#
# combobox = ttk.Combobox()
# combobox.pack()
#
# notebook = ttk.Notebook()
# notebook.pack()
#
#
# sample_tk.mainloop()


