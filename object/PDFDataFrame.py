import os
import pdfplumber
import pandas as pd
import numpy as np

from pandas import DataFrame

class PDFDataFrame :

    def __init__(self, path_to_pdf) :
        tables = []
        with pdfplumber.open(path_to_pdf) as pdf:
            for page in pdf.pages:
                page_tables = page.extract_tables()
                for table in page_tables:
                    tables.append(pd.DataFrame(table, dtype = str))
        dataframe = pd.concat(tables, ignore_index = True)
        dataframe = dataframe.astype(str)
        dataframe = dataframe.replace({"None" : np.nan})
        dataframe.columns = dataframe.iloc[0]
        dataframe = dataframe.drop(dataframe.index[0])
        self.df : DataFrame = dataframe # type : <class 'pandas.core.frame.DataFrame'>
        self.name = os.path.basename(os.path.normpath(path_to_pdf))
        self.directory = os.path.dirname(path_to_pdf)

    def get_df(self) :
        return self.df
    
    def print_df(self) :
        print(self.get_df())

    def get_name(self) :
        return self.name
    
    def print_name(self) :
        print(self.get_name())

    def get_directory(self) :
        return self.directory
    
    def print_directory(self) :
        print(self.get_directory())