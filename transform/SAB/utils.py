import numpy as np
import pandas as pd
import re

from pandas import DataFrame

def lower_df(df) :
    df.columns = df.columns.str.lower()
    df = df.apply(lambda x: x.str.lower())
    return df

def replace_df(df) :
    df.columns = df.columns.str.replace("\n", "")
    df = df.replace("\n", "", regex = True)
    df = df.replace({"nan" : np.nan})
    return df

def get_filtered_columns_df(df, column_tuples) :
    column_indexes = []

    for column_details in column_tuples :
        column_name = column_details[0]
        value_list = column_details[1]
        column_index = get_column_index_from_value(df, value_list)
        if len(column_index) == 0 :
            print("Error : No index found for column : " + column_name)
            return
        elif len(column_index) > 1 :
            print("Error : Multiple indexes", column_index, "were found for column : " + column_name)
            return
        else :
            column_indexes.append(column_index[0])

    df = df.iloc[:, column_indexes]
    return df

def get_column_index_from_value(df, value_list) :
    column_index = []
    n, p = np.shape(df)

    for i in range(p) :
        column = df.iloc[:, i]
        column_name = column.name
        column = column.tolist()
        column.append(column_name)

        for elt in column :
            if not pd.isna(elt) :
                if all(value in elt for value in value_list) :
                    column_index.append(i)
                    break

    return column_index

def fill_downwards(df) :
    df = df.ffill()
    return df

def clean_zipper(df) :
    pattern = r"[A-Z]{3}\d{4}"
    filter = ["zip", "zic", "zit"]
    df = duplicate_rows_by_references(df, 'ZIPPER', pattern, filter)
    df["ZIPPER"] = df["ZIPPER"].apply(lambda x: x.upper())
    return df

def duplicate_rows_by_references(df : DataFrame, column, pattern, filter) :
    zipper = "ZIPPER"

    def extract_references(text, filter) :
        references = re.findall(pattern, text, re.IGNORECASE)
        return [ref for ref in references if any(ref.startswith(prefix) for prefix in filter)]
    
    df[zipper] = df[zipper].apply(lambda x: extract_references(x, filter))
    df = df.explode(zipper)
    df = df.dropna(subset = [zipper]).reset_index(drop = True)

    return df

def clean_size(df) :
    size_column = df["SIZE"]
    size_column = size_column.apply(lambda x: x.split("cm")[0])
    size_column = pd.to_numeric(size_column, errors = 'coerce')
    df["SIZE"] = size_column
    df = remove_null_size(df)
    return df

def remove_null_size(df) :
    size_column = df["SIZE"]
    df = df[size_column.notnull()]
    return df

def clean_price(df) :
    price_column = df["PRICE"]
    price_column = pd.to_numeric(price_column, errors = 'coerce')
    df["PRICE"] = price_column
    df = remove_null_price(df)
    return df

def remove_null_price(df) :
    price_column = df["PRICE"]
    df = df[price_column.notnull()]
    return df

def add_date_column(df, date) :
    df["DATE"] = date
    return df