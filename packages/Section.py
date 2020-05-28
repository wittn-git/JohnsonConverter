from packages.Utility import Font
from tkinter import filedialog, CENTER
from packages.Components import DLine, DButton, DLabel, DText, DMessage
from pathlib import Path
from packages.CommandHandler import CommandHandler

class Section:
    def __init__(self, number, title, root, limit):
        
        self.number = number
        self.title = title
        self.line_width = 3
        self.cell_width = 300
        self.x, self.y = number*self.cell_width, 210
        self.limit = limit
        self.elements = []
        self.root = root
        self.workfiles, self.destination_folder = [], None
        self.command = lambda: self.get_command()
        self.add_elements()

    def get_command(self):
        pages = None
        if self.pages_text != None:
            pages = self.pages_text.get_contents().strip()
        success = CommandHandler().get_command(self.number, self.workfiles, self.destination_folder, self.destination_file_text.get_contents().strip(), self.elements, pages)
        if success == True: self.workfiles, self.destination_folder = [], None

    def set_destination_folder(self):
        self.destination_folder = filedialog.askdirectory(initialdir = str(Path.home()))
        self.destination_folder_text.set_text(self.destination_folder)

    def add_workfile(self):
        self.filename = filedialog.askopenfilename(initialdir = str(Path.home()),title = "Select pdf",filetypes = (("pdf files","*.pdf"),))
        self.workfiles_text.add_text(self.filename, self.limit)  
        self.workfiles = self.workfiles_text.content  
    
    def clear_workfiles(self):
        self.workfiles_text.clear_content()
        self.workfiles = self.workfiles_text.content  

    def add_elements(self):
        self.line = DLine(self.x+self.cell_width, self.y, self.x+self.cell_width, 0, self.line_width, False, True)
       
        self.elements.append(DLabel(self.title, 26, self.x+self.line_width, self.y+3*self.line_width, self.cell_width-2*self.line_width, self.root))
        self.elements.append(DButton(self.x+self.cell_width*0.1, self.root.h-175, self.cell_width*0.8, 80, self.title, self.command, 20, self.root))
        self.elements.append(DButton(self.x+self.cell_width*0.7, self.y+70+110+100, self.cell_width*0.25, 35, 'Destination\ndirectory', self.set_destination_folder, 9, self.root))
        self.elements.append(DLabel('Destination\nfilename', 9, self.x+self.cell_width*0.7, self.y+70+110+100+45, self.cell_width*0.25, self.root))

        self.destination_file_text = DText(self.x+self.cell_width*0.05, self.y+70+110+100+45, self.cell_width*0.65, 35, False, False, self.root)
        self.destination_folder_text = DText(self.x+self.cell_width*0.05, self.y+70+110+100, self.cell_width*0.65, 35, True, False, self.root)
        self.pages_text = None

        if self.number == 0:
            self.workfiles_text = DText(self.x+self.cell_width*0.05, self.y+70, self.cell_width*0.9, 110, True, False, self.root)
            self.elements.append(DButton(self.x+self.cell_width*0.05, self.y+70+110, self.cell_width*0.9, 40, 'Add files', self.add_workfile, 12, self.root))
            self.elements.append(DButton(self.x+self.cell_width*0.05, self.y+70+110+40, self.cell_width*0.9, 40, 'Clear files', self.clear_workfiles, 12, self.root))
        
        if self.number == 1:
            self.workfiles_text = DText(self.x+self.cell_width*0.05, self.y+70, self.cell_width*0.65, 35, True, False, self.root)
            self.elements.append(DButton(self.x+self.cell_width*0.7, self.y+70, self.cell_width*0.25, 35, 'Add file', self.add_workfile, 9, self.root))
            self.elements.append(DButton(self.x+self.cell_width*0.7, self.y+70+35, self.cell_width*0.25, 35, 'Clear file', self.clear_workfiles, 9, self.root))
            self.pages_text = DText(self.x+self.cell_width*0.05, self.y+70+35+35+20, self.cell_width*0.9, 35, False, True, self.root)
            self.elements.append(DMessage('Enter the page numbers to be split at, all divided by commas (,).', 9, self.x+self.cell_width*0.05, self.y+70+35+35+20+35, self.cell_width*0.9, CENTER, self.root))
            self.elements.append(self.pages_text)

        self.elements.append(self.workfiles_text)
        self.elements.append(self.destination_folder_text)
        self.elements.append(self.destination_file_text)