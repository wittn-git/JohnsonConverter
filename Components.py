from tkinter import BOTH, Button, Canvas, LEFT, Label, PhotoImage, Tk
import tkinter
from PIL import Image, ImageTk
from Utility import Font

class DLabel:

    def __init__(self, text, font, x_positon, y_position, width, root):
        self.text = text
        self.font = font
        self.x_positon = x_positon
        self.y_position = y_position
        self.width = width
        self.root = root.root
        
    def get_properties(self):
        return [self.x_positon, self.y_position, self.width, None]

    def get_element(self):
        return Label(self.root, text=self.text, font = self.font.get_font(), justify=LEFT)

class DImageLabel:

    def __init__(self, image, x_positon, y_position, width, height, root):
        self.image = image
        self.x_positon = x_positon
        self.y_position = y_position
        self.width = width
        self.height = height
        self.root = root.root

    def get_properties(self):
        return [self.x_positon, self.y_position, None, None]
    
    def get_element(self):
        self.image = self.image.resize((self.width,self.height), Image.ANTIALIAS)
        self.image =  ImageTk.PhotoImage(self.image)
        label = Label(self.root, image=self.image)
        label.image = self.image
        return label

class DButton:

    def __init__(self, x_position, y_position, width, height, text, command, root):
        self.font = Font(20).get_font()
        self.x_positon = x_position
        self.y_position = y_position
        self.width = width
        self.height = height
        self.text = text
        self.command = command
        self.root = root.root
    
    def get_properties(self):
        return [self.x_positon, self.y_position, self.width, self.height]
    
    def get_element(self):
        return Button(self.root, text = self.text, command = self.command, font=self.font)

class DLine:

    def __init__(self, x1, y1, x2, y2, width, full_width, full_height):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.width = width
        self.full_width = full_width
        self.full_height = full_height

class DFrame:
    def __init__(self, title):
        self.root = tkinter.Tk()
        self.root.wm_title(title)
        self.w, self.h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry('%dx%d+0+0' % (self.w, self.h))

        self.canvas = Canvas(self.root)
        self.canvas.pack(fill=BOTH, expand=1)
        self.canvas.pack()

    def set_icon(self, icon):
        self.root.tk.call('wm', 'iconphoto', self.root._w, ImageTk.PhotoImage(icon))
    
    def add_line(self, line):
        if line.full_width == True: line.x2 = self.w
        if line.full_height == True: line.y2 = self.h
        self.canvas.create_line(line.x1, line.y1, line.x2, line.y2, width=line.width)
    
    def add_widget(self, element):
        widget = element.get_element()
        properties = element.get_properties()
        widget.pack()
        widget.place(x=properties[0], y=properties[1])
        if properties[2] != None: widget.place(width=properties[2])
        if properties[3] != None: widget.place(height=properties[3])
        
    def add_section(self, section):
        for element in section.elements:
            self.add_widget(element)
        
    def show(self):
        self.root.mainloop()