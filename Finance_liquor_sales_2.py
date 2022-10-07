import pandas as pd
import numpy as np

df = pd.read_csv (r'C:\Users\skratimenos\Downloads\Data_finance_liquor_sales_2016_2019.csv')
# df = pd.read_csv (r'C:\Users\skratimenos\Downloads\Data_finance_liquor_sales_ALL.csv')

grp = df.groupby('store_number')
df = grp['sale_dollars'].agg([np.sum])/df['sale_dollars'].sum()

df.sort_values(by=['sum'])
df.to_csv(r'C:\Users\skratimenos\Downloads\Data_percentage_of_sales_per_store2.csv')

print(df)
