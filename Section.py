from Utility import Font
from tkinter import filedialog
from Components import DLine, DButton, DLabel

class Section:
    def __init__(self, number, title, command, root):
        
        self.number = number
        self.title = title
        self.line_width = 3
        self.cell_width = 300
        self.command = command
        self.destination_folder, self.destination_filename = None, None
        self.x, self.y = number*self.cell_width, 210
        self.elements = []
        self.root = root
        self.add_elements()
    
    def set_destination_folder(self):
        self.destination_folder = filedialog.askdirectory(initialdir = "/")

    def add_elements(self):
        self.line = DLine(self.x+self.cell_width, self.y, self.x+self.cell_width, 0, self.line_width, False, True)
        self.elements.append(DLabel(self.title, Font(26), self.x+self.line_width, self.y+3*self.line_width, self.cell_width-2*self.line_width, self.root))
        self.elements.append(DButton(self.x+self.cell_width*0.1, self.root.h-175, self.cell_width*0.8, 80, self.title, self.command, self.root))
   # def add_section(self, section):
        #self.add_label(section.title, Font(26), x+section.line_width, y+3*section.line_width, section.cell_width-2*section.line_width)
        #self.add_button(x+section.cell_width*0.1, self.h-175, section.cell_width*0.8, 80, section.title, section.command)
