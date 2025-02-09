
import pandas as pd

df = pd.read_csv('result.csv')
df.loc[:,'District'] = df['District'].str.replace(' District', '', regex = False)
df.loc[:,'Division'] = df['Division'].str.replace(' Division', '', regex = False)
df.to_csv('cleanedResultv1.csv', index=False)
print('done')