import pandas as pd
import openpyxl
import itertools
epitope = pd.read_excel('epitope.xlsx')  
#print(epitope)

cdr3b = pd.read_csv('1.txt', sep = '\t')
print(cdr3b)

all_combinations = pd.DataFrame(list(itertools.product(cdr3b['cdr3aa'], epitope['Peptide'])),
                                columns=['CDR3b', 'epitope'])
print(all_combinations)

all_combinations.to_csv('1Combine.csv', index = False)

df_train = pd.read_csv('data/splitData/withMHC/train/train.csv')
repeat_times = -(-len(all_combinations) // len(df_train))  # Ceiling division

# Repeat the MHC and HLA columns
repeated_mhc = (df_train['MHC'].tolist() * repeat_times)[:len(all_combinations)]
repeated_hla = (df_train['HLA'].tolist() * repeat_times)[:len(all_combinations)]

# Add the repeated MHC and HLA columns to the all_combinations DataFrame
all_combinations['HLA'] = repeated_hla
all_combinations['MHC'] = repeated_mhc
#all_combinations['HLA'] = repeated_hla
#print(all_combinations)
filtered_combinations = all_combinations[
    (all_combinations['CDR3b'].str.len() >= 8) & (all_combinations['CDR3b'].str.len() <= 19)
]

filtered_combinations_updated = filtered_combinations[
    (filtered_combinations['epitope'].str.len() >= 8) & (filtered_combinations['epitope'].str.len() <= 11)
]
all_combinations = filtered_combinations_updated
all_combinations.loc[:, 'CDR3b'] = all_combinations.loc[:, 'CDR3b'].str.replace('_', '')

# If you also want to replace '*', you would similarly use:
all_combinations.loc[:, 'CDR3b'] = all_combinations.loc[:, 'CDR3b'].str.replace('*', '')
#all_combinations['CDR3b'] = all_combinations['CDR3b'].str.replace('_', '')
#all_combinations['CDR3b'] = all_combinations['CDR3b'].str.replace('*', '')
all_combinations.to_csv('1Combine.csv', index = False)