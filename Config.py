import os

class Config :

    def __init__(self) :
        self.project_path = os.path.dirname(__file__)
        self.invoice_path = os.path.join(self.project_path, "invoice")
        self.object_path = os.path.join(self.project_path, "object")
        self.transform_path = os.path.join(self.project_path, "transform")
        self.csv_path = os.path.join(self.project_path, "csv")
    


    def get_project_path(self):
        return self.project_path

    def set_project_path(self, value):
        self.project_path = value

    def get_invoice_path(self):
        return self.invoice_path

    def set_invoice_path(self, value):
        self.invoice_path = value

    def get_object_path(self):
        return self.object_path

    def set_object_path(self, value):
        self.object_path = value

    def get_transform_path(self):
        return self.transform_path

    def set_transform_path(self, value):
        self.transform_path = value

    def get_csv_path(self):
        return self.csv_path

    def set_csv_path(self, value):
        self.csv_path = value
