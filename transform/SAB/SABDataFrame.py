import os
import re
import pandas as pd

from pandas import DataFrame

from dateutil.parser import parse

from Config import Config

from object.PDFDataFrame import PDFDataFrame
from object.PDFText import PDFText

from transform.utils import remove_duplicates, permute_columns

from transform.SAB.utils import lower_df, replace_df, get_filtered_columns_df, fill_downwards, clean_size, clean_price, add_date_column, clean_zipper

class SABDataFrame :


    def __init__(self, provider, pdf) :
        path_to_pdf_folder = os.path.join(Config().get_invoice_path(), provider)
        path_to_pdf = os.path.join(path_to_pdf_folder, pdf)

        self.name = pdf
        self.pdf_dataframe = PDFDataFrame(path_to_pdf)
        self.pdf_text = PDFText(path_to_pdf)
        self.df : DataFrame = self.get_df()
        self.text = self.get_text()
        self.column_names = ("ZIPPER", "SIZE", "PRICE")
        self.value_list = (["customer", "zipper"], ["size", "(", ")"], ["price"])
        self.date = self.get_date()

    def transform(self) :
        df : DataFrame = self.get_df() # get the df from the object
        date = self.get_date() # get the date from the object

        df = lower_df(df) # lowering all values
        df = replace_df(df) # replacing some values
        print(self.get_name(), df)
        df = get_filtered_columns_df(df, zip(self.get_column_names(), self.get_value_list())) # filtering on selected columns
        df.columns = self.get_column_names() # renaming columns
        df = fill_downwards(df) # forward fill
        df = clean_zipper(df) # extract and filter on zip, zic or zit only
        df = clean_size(df) # format size column
        df = clean_price(df) # format price column
        df = add_date_column(df, date) # add date column
        df = permute_columns(df, [0, 1, 3, 2]) # permute columns
        
        df = remove_duplicates(df) # remove all duplicates

        self.set_df(df) # set the sab df


    def print_df(self) :
        print(self.get_df())

    def print_text(self) :
        print(self.get_text())

    def print_date(self) :
        print(self.get_date())
    
    def get_df(self) :
        return self.get_pdf_dataframe().get_df()
    
    def get_text(self) :
        return self.get_pdf_text().get_text()
    
    def set_df(self, new_df : DataFrame):
        self.pdf_dataframe.df = new_df

    def get_pdf_folder(self):
        return self.pdf_folder

    def set_pdf_folder(self, value):
        self.pdf_folder = value
    
    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_pdf_dataframe(self):
        return self.pdf_dataframe

    def set_pdf_dataframe(self, value):
        self.pdf_dataframe = value

    def get_pdf_text(self):
        return self.pdf_text

    def set_pdf_text(self, value):
        self.pdf_text = value

    def get_column_names(self):
        return self.column_names

    def set_column_names(self, value):
        self.column_names = value

    def get_value_list(self):
        return self.value_list

    def set_value_list(self, value):
        self.value_list = value

    def get_date(self):
        date = None
        text = self.get_text()

        for elt in text :
            try :
                try:
                    float(elt)
                    pass
                except ValueError:
                    date = parse(elt).strftime("%Y-%m-%d")
                    break
            except (ValueError, TypeError) :
                pattern = r"\d{1,2}-\w{3}-\d{2}"
                match = re.search(pattern, elt)
                if match:
                    date = parse(match.group()).strftime("%Y-%m-%d")
                pass
        
        return date

    def set_date(self, value):
        self.date = value
