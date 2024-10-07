from pandas import DataFrame


def remove_duplicates(df : DataFrame) :
    df = df.drop_duplicates().reset_index(drop = True)
    return df

def permute_columns(df : DataFrame, order) :
    df = df[df.columns[order]]
    return df