from PyPDF2 import PdfFileMerger
from packages.Utility import Message
from packages.Components import DText

class CommandHandler:
    
    def get_command(self, command_number, workfiles, destination_directory, destination_file, elements):
        try:
            if destination_directory == None: Message().show_error('No valid destination directory entered.')
            if not destination_file.endswith('.pdf'): destination_file += '.pdf'

            switcher = {
                0: self.merge(workfiles, destination_directory, destination_file)
            }
            
            for element in elements:
                if isinstance(element, DText): element.clear_content()
            
        except ValueError as e:
            pass

    def merge(self, workfiles, destination_directory, destination_file):
        if len(workfiles) < 2: Message().show_error("Enter at least two file to merge.")
        pdf_merger = PdfFileMerger()
        for path in workfiles:
            pdf_merger.append(path)
        
        with open('{}//{}'.format(destination_directory, destination_file), 'wb') as fileobj:
          pdf_merger.write(fileobj)