import os

class PDFFolder :

    def __init__(self, path_to_pdf_folder) :
        extension = ".pdf"
        file_list = []
        for file in os.listdir(path_to_pdf_folder) :
            if file.endswith(extension) :
                file_list.append(file)
                
        self.pdf_list = file_list
        self.name = os.path.basename(os.path.normpath(path_to_pdf_folder))
        self.directory = os.path.dirname(path_to_pdf_folder)
        self.number_of_pdf = len(self.pdf_list)

    def get_pdf_list(self) :
        return self.pdf_list
    
    def print_pdf_list(self) :
        print(self.get_pdf_list())

    def get_name(self) :
        return self.name
    
    def print_name(self) :
        print(self.get_name())
    
    def get_directory(self) :
        return self.directory
    
    def print_directory(self) :
        print(self.get_directory())

    def get_number_of_pdf(self) :
        return self.number_of_pdf
    
    def print_number_of_pdf(self) :
        print(self.get_number_of_pdf())


    def get_pdf_name(self, i) :
        return self.get_pdf_list()[i]