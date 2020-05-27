import tkinter.font as tkFont

class Font():
    def __init__(self, size):
        self.font = tkFont.Font(family="Times New Roman", size=size)

    def get_font(self):
        return self.font