import pandas as pd
import numpy as np

df = pd.read_csv (r'C:\Users\skratimenos\Downloads\Data_finance_liquor_sales_2016_2019.csv')

grp = df.groupby(['zip_code','item_description'])

df = grp['bottles_sold'].agg([np.sum])

df.to_csv(r'C:\Users\skratimenos\Downloads\Data_most_popular_item_sold_based_on_zip_code.csv')

print(df)
