import pandas as pd

df_epitope = pd.read_csv('EpitopeTest.csv')
df_cdr3b = pd.read_csv('CDR3BTest.csv')

merged_df = pd.merge(df_epitope, df_cdr3b, on='PDB ID', how='inner')

merged_df.to_csv('merged_data3.csv', index=False)
