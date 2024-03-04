import pandas as pd
import random

df = pd.read_csv('merged_data2.csv')

# Function to randomize pairs without repeating the same pair
def randomize_pairs(df):
    cdr3b = df['CDR3b'].tolist()
    epitopes = df['epitope'].tolist()
    
    # Ensure unique mapping by shuffling the lists until no pair matches the original #pairs
    while True:
        random.shuffle(epitopes)
        new_pairs = list(zip(cdr3b, epitopes))
        
        # Check if any of the new pairs are the same as the original pairs
        if not any(new_pair in list(zip(df['CDR3b'], df['epitope'])) for new_pair in new_pairs):
            break

    # Create a new DataFrame with the new unique mappings
    new_df = pd.DataFrame(new_pairs, columns=['CDR3b', 'epitope'])
    return new_df
new_df = randomize_pairs(df)
new_df.to_csv('random.csv')
# Assuming 'original_df' is your original dataframe
# new_df = randomize_pairs(original_df)
