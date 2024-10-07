from utils import combine_provider_df, save_df_to_csv, sort_columns

def pdf_to_csv(provider) :
    df = combine_provider_df(provider)
    order = ["ZIPPER", "SIZE", "DATE"]
    sort_columns(df, order)
    save_df_to_csv(provider, df)