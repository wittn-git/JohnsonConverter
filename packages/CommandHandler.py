from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
from packages.Utility import MessageDialog
from packages.Components import DText

class CommandHandler:
    
    def get_command(self, command_number, workfiles, destination_directory, destination_file, elements, pages):
        try:
            if destination_directory == None: raise NameError('No valid destination directory entered.')
            if not destination_file.endswith('.pdf'): destination_file += '.pdf'

            switcher = {
                0: lambda: self.merge(workfiles, destination_directory, destination_file),
                1: lambda: self.split(workfiles, destination_directory, destination_file, pages)
            }
            
            command = switcher.get(command_number)
            command()

            for element in elements:
                if isinstance(element, DText): element.clear_content()
            return True
            
        except Exception as e:
            MessageDialog().show_error(e.args[0])
            return False

    def merge(self, workfiles, destination_directory, destination_file):
        if len(workfiles) < 2: raise NameError('Enter at least two file to merge.')
        pdf_merger = PdfFileMerger()
        for path in workfiles:
            pdf_merger.append(path)
        
        with open('{}//{}'.format(destination_directory, destination_file), 'wb') as fileobj:
          pdf_merger.write(fileobj)
        
        MessageDialog().show_message('Documents were merged successfully.')
    
    def split(self, workfiles, destination_directory, destination_file, pages):
       
        if len(workfiles) != 1:
            raise NameError("Enter one file to split.")

        inputpdf = PdfFileReader(open(workfiles[0], "rb"))

        try:
            pages = pages.replace(' ', '').replace('\n', '').split(',')
            pages = [int(i)-1 for i in pages]
            pages.sort()
            if 0 not in pages: pages.insert(0, 0)
            if inputpdf.numPages not in pages: pages.append(inputpdf.numPages)
            if any(n < 0 for n in pages): raise ValueError('Error')
        except Exception:
            raise NameError('One or more page numbers entered were not valid.')

        if any(n > inputpdf.numPages for n in pages): raise NameError('One or more page numbers exeed the size if the document.')
        
        for i in range(len(pages)-1):
            outputpdf = PdfFileWriter()
            for j in range(pages[i], pages[i+1]):
                outputpdf.addPage(inputpdf.getPage(j))
            with open('{}//{}{}.pdf'.format(destination_directory, destination_file[:-4], i), "wb") as fileobj:
                outputpdf.write(fileobj)
        
        MessageDialog().show_message('Document was split successfully.')