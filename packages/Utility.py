import tkinter.font as tkFont
from tkinter import messagebox

class Font():
    def __init__(self, size):
        self.font = tkFont.Font(family="Times New Roman", size=size)

    def get_font(self):
        return self.font

class MessageDialog:
    def show_error(self, message):
        messagebox.showerror('Error', message)
    
    def show_message(self, message):
        messagebox.showinfo('Success', message)