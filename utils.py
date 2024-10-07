import os
import pandas as pd

from pandas import DataFrame

from Config import Config

from object.PDFFolder import PDFFolder

from transform.SAB.SABDataFrame import SABDataFrame

def save_df_to_csv(provider, df : DataFrame) : 
    path_to_save_csv = os.path.join(Config().get_csv_path(), provider)
    csv_name = "output.csv"

    try :
        df.to_csv(os.path.join(path_to_save_csv, csv_name), index = False, sep = "|", decimal = ",")
        print("File saved !")
    except Exception as e :
        print("Error while saving the file : " + e)

def combine_provider_df(provider) :
    path_to_pdf_folder = os.path.join(Config().get_invoice_path(), provider)
    pdf_folder = PDFFolder(path_to_pdf_folder)
    pdf_list = pdf_folder.get_pdf_list()
    df_list = []

    for pdf in pdf_list :
        provider_dataframe = SABDataFrame(provider, pdf)
        provider_dataframe.transform()
        df_list.append(provider_dataframe.get_df())

    combined_df = pd.concat(df_list)
    return combined_df

def sort_columns(df : DataFrame, order) :
    df.sort_values(by = order, inplace = True)
    return df