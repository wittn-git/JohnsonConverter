from packages.Components import *
from packages.Section import Section
from PIL import Image
import sys

image_path = ''
if sys.platform.startswith('linux'): image_path = '/opt/JohnsonConverter/images'
elif sys.platform.startswith('win'): image_path = 'C://Program Files//JohnsonConverter//images'

frame = DFrame('JohnsonConverter')

try:
    icon = Image.open('{}/{}'.format(image_path, 'icon.gif'))
except:
    pass
frame.set_icon(icon)

elements = []

elements.append(DLabel('JohnsonConverter', 44, 10, 10, None, frame))
elements.append(DLabel('''This application is a tool to merge, split and do other stuff 
with PDF-Documents, for people, who live in the last century and 
do not know how to use the internet properly. Enjoy!''',
                18, 50, 90, None, frame))
try:
    elements.append(DImageLabel(icon, 470, 20, 45, 60, frame))
except:
    pass

for element in elements:
    frame.add_widget(element)

sections = []
sections.append(Section(0, 'Merge files', frame))
for section in sections:
    frame.add_section(section)

lines = []
lines.append(DLine(0, 210, 0, 210, 3, True, False))
for section in sections:
    lines.append(section.line)
for line in lines:
    frame.add_line(line)

coming_soon = DLabel('Coming soon...', 16, 300*len(sections)+6, 210+3, None, frame)
frame.add_widget(coming_soon)

frame.show()