import camelot
import pandas
import pandas as pd
from pypdf import PdfReader
import pdfplumber
import csv

with pdfplumber.open('copy.pdf') as pdf:
    all_tables = []
    for page in pdf.pages:
        table = page.extract_table()
        if table:
            all_tables.append(table)
print(len(all_tables))

def get_data(tables):
    df = pd.DataFrame(tables[1:], columns=tables[0])

    #olumns_to_extract = ['Name' ,'Population20','2022' ]
    #df_filtered = df[columns_to_extract]
    df_filtered = df
    #df_filtered['Division'] = None
    df_filtered.insert(0,'Division', '')
    #df_filtered['District'] = None
    df_filtered.insert(1,'District', '')

    current_division = None
    current_district = None

    for idx, row in df_filtered.iterrows():
        if isinstance(row['Name'], str):
            if 'Division' in row['Name']:
                current_division = row['Name']
                df_filtered.at[idx, 'Division'] = current_division
                df_filtered.at[idx, 'District'] = None
            elif 'District' in row['Name']:
                current_district = row['Name']
                df_filtered.at[idx, 'District'] = current_district
                df_filtered.at[idx, 'Division'] = current_division
            else:
                df_filtered.at[idx, 'District'] = current_district
                df_filtered.at[idx, 'Division'] = current_division
    return df_filtered
main = pd.DataFrame()
for i in range(18):
    single_table = all_tables[i]
    d = get_data(single_table)
    main = pd.concat([main, d],ignore_index=True)
#df_filtered = df_filtered[['Division', 'District'] + [col for col in df_filtered.columns if col not in ['Division', 'District']]]
#df_filtered.drop(df_filtered.columns[[9]],axis= 1, inplace=True)
df_f = main
df_f = df_f[~df_f['Name'].str.contains("Division|District", na=False)]
#df_f['Division'] = df_f['Division'].fillna(method = 'ffill')
substrings = ['(Q1)', '(Q2)', '(Q3)', '(Q4)', '(Q5)']
for substring in substrings:
    df_f.loc[:,'2022'] = df_f['2022'].str.replace(substring, '', regex = False)


df_f.to_csv('result.csv', index = False)
print('Done')