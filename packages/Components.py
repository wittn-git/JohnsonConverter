from tkinter import BOTH, Button, Canvas, LEFT, Label, PhotoImage, Tk, DISABLED, Text, END, Message
import tkinter
from PIL import Image, ImageTk
from packages.Utility import Font, MessageDialog
import sys

class DLabel:

    def __init__(self, text, fontsize, x_position, y_position, width, root):
        self.text = text
        self.font = Font(fontsize)
        self.x_positon = x_position
        self.y_position = y_position
        self.width = width
        self.root = root.root
        
    def get_properties(self):
        return [self.x_positon, self.y_position, self.width, None]

    def get_element(self):
        return Label(self.root, text=self.text, font = self.font.get_font(), justify=LEFT)

class DMessage:

    def __init__(self, text, fontsize, x_position, y_position, width, alignment, root):
        self.text = text
        self.font = Font(fontsize)
        self.x_positon = x_position
        self.y_position = y_position
        self.width = width
        self.alignment = alignment
        self.root = root.root
        
    def get_properties(self):
        return [self.x_positon, self.y_position, None, None]

    def get_element(self):
        return Message(self.root, text=self.text, font = self.font.get_font(), justify=self.alignment, width=self.width)

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

    def __init__(self, x_position, y_position, width, height, text, command, fontsize, root):
        self.font = Font(fontsize)
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
        return Button(self.root, text = self.text, command = self.command, font=self.font.get_font())

class DText:

    def __init__(self, x_position, y_position, width, height, disabled, multiline, root):
        self.font = Font(16)
        self.x_positon = x_position
        self.y_position = y_position
        self.width = width
        self.height = height
        self.root = root.root
        self.content = []
        self.disabled = disabled

        self.text = Text(self.root, font = self.font.get_font())
        if disabled == True: self.text.config(state=DISABLED)
        if multiline == False: 
            self.text.config(wrap='none')

    def get_properties(self):
        return [self.x_positon, self.y_position, self.width, self.height]
    
    def add_text(self, text, limit):
        try:
            if(limit == len(self.content)): 
                raise NameError("Limit of files has been reached. Clear files to add files again.", True)
            elif text not in self.content:
                self.content.append(text)
                self.set_text('\n'.join(self.content))
        except Exception as e:
            MessageDialog().show_error(e.args[0])
    
    def set_text(self, text):
        self.text.config(state='normal')
        self.text.delete('1.0',END)
        self.text.insert('1.0', text)
        self.text.update_idletasks()
        self.text.config(state=DISABLED)

    def clear_content(self):
        self.text.config(state='normal')
        self.text.delete('1.0',END)
        self.text.update_idletasks()
        if self.disabled == True: self.text.config(state=DISABLED)
        self.content = []
    
    def get_contents(self):
        return self.text.get('1.0',END)
        
    def get_element(self):
        return self.text

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
        self.root.state('zoomed')

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