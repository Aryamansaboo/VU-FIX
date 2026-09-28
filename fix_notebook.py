import json

file_path = 'Drishya_AI_Labs_Project.ipynb'

with open(file_path, 'r') as f:
    notebook = json.load(f)

for cell in notebook['cells']:
    if cell['cell_type'] == 'code':
        source = "".join(cell['source'])
        if "markov_data = df_markov.iloc[" in source or "markov_data = df.iloc[" in source:
            print("Found the target cell.")
            # Update the source code
            new_source = """# Extract the Markov Matrix from the dataset
# Rows 25 to 29 (index 24 to 28) and columns C to G (index 2 to 6) in the raw sheet correspond to the actual stochastic probabilities
# Columns: Others, Level, Flow, Pressure, Temperature

markov_data = df_markov.iloc[24:29, 2:7].copy()
markov_data.columns = ['Others', 'Level', 'Flow', 'Pressure', 'Temperature']
markov_data.index = ['Others', 'Level', 'Flow', 'Pressure', 'Temperature']
markov_data = markov_data.astype(float)

print("--- Transition Probability Matrix ---")
display(markov_data)"""
            cell['source'] = [line + '\n' for line in new_source.split('\n')]
            # Fix the last line to not have a trailing newline if it shouldn't
            cell['source'][-1] = cell['source'][-1].rstrip('\n')
            
            print("Updated the target cell.")

with open(file_path, 'w') as f:
    json.dump(notebook, f, indent=1)

print("Notebook saved successfully!")
