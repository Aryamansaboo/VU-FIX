import pandas as pd

# Load the sheets
df_markov = pd.read_excel('Drishya_Dataset.xlsx', sheet_name='Markov Matrix for next alarm ')

# Extract the Markov Matrix from the dataset
# Rows 25 to 29 (index 24 to 28) and columns C to G (index 2 to 6) in the raw sheet correspond to the actual stochastic probabilities
# Columns: Others, Level, Flow, Pressure, Temperature

markov_data = df_markov.iloc[24:29, 2:7].copy()
markov_data.columns = ['Others', 'Level', 'Flow', 'Pressure', 'Temperature']
markov_data.index = ['Others', 'Level', 'Flow', 'Pressure', 'Temperature']
markov_data = markov_data.astype(float)

print("--- Transition Probability Matrix ---")
print(markov_data)
