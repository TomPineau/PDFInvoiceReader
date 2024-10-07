import os
import PyPDF2

class PDFText:

    def __init__(self, path_to_pdf) :
        with open(path_to_pdf, 'rb') as pdf:
            PDFReader = PyPDF2.PdfReader(pdf)
            text = ""
            for page in range(len(PDFReader.pages)):
                page_objet = PDFReader.pages[page]
                text += page_objet.extract_text()
        self.text = text.split('\n')
        self.name = os.path.basename(os.path.normpath(path_to_pdf))
        self.directory = os.path.dirname(path_to_pdf)
        

    def get_text(self) :
        return self.text
    
    def print_text(self) :
        for row in self.get_text() :
            print(row)

    def get_name(self) :
        return self.name
    
    def print_name(self) :
        print(self.get_name())
    
    def get_directory(self) :
        return self.directory
    
    def print_directory(self) :
        print(self.get_directory())