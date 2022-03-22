import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

df_csv = pd.read_csv('example')
print(df_csv)

df_csv.to_csv('My_output', index=False)

df_excel = pd.read_excel('Excel_Sample.xlsx', sheet_name='Sheet1')
print(df_excel)
df_excel.to_excel('Excel_Sample2.xlsx',sheet_name='NewSheet'  ,index=False)

# HTML
data = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')
data_df = data[0]
type(data)

# SQL
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')
df_csv.to_sql('my_table', engine)
sqldf = pd.read_sql('my_table', con=engine)
print(sqldf)