import pandas as pd


def log_scrape(*, file, web_link, deck_len):
    file.write("scraped " + str(deck_len) + " from: " + str(web_link) + "\n")

# Write data to pickle file using pandas.
def store_file(*, pickled_df, scraped_list):
    pickled_df = pd.DataFrame(scraped_list, columns=['Card_Names'])
    df2 = pd.DataFrame(scraped_list, columns=['Card_Names'])
    df_to_save = pd.concat([pickled_df, df2], axis=0)
    df_to_save.to_pickle(r"C:\Users\dmcfa\Desktop\cedh_webscrape1.pk1")
    print(df_to_save.tail(4))
    print(str(df_to_save.shape[0]) + ' Rows in Pickle file.')
