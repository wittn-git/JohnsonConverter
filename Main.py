from Utility import Font
from Components import *
from Section import Section
from PIL import Image
    
frame = DFrame('JohnsonConverter')
icon = Image.open('icon.gif')
frame.set_icon(icon)
h = 200

elements = []

elements.append(DLabel('JohnsonConverter', Font(44), 10, 10, None, frame))
elements.append(DLabel('''This application is a tool to merge, split and do other stuff 
with PDF-Documents, for people, who live in the last century and 
do not know how to use the internet properly. Enjoy!''',
                Font(18), 50, 90, None, frame))
elements.append(DImageLabel(icon, 470, 20, 45, 60, frame))

for element in elements:
    frame.add_widget(element)

sections = []
sections.append(Section(0, 'Merge files', None, frame))
for section in sections:
    frame.add_section(section)

lines = []
lines.append(DLine(0, 210, 0, 210, 3, True, False))
for section in sections:
    lines.append(section.line)
for line in lines:
    frame.add_line(line)

frame.show()
#self.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select pdf",filetypes = (("pdf files","*.pdf")))