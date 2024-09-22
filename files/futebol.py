import pandas as pd

# Load your data into a DataFrame (replace 'futebol.csv' with your actual data file)
df = pd.read_csv('futebol.csv')

# Create the 'winner' column based on the conditions
df['winner'] = df.apply(lambda row: 0 if row['gols_mandante'] == row['gols_visitante'] else (1 if row['gols_mandante'] > row['gols_visitante'] else 2), axis=1)

# Drop the 'gols_mandante' and 'gols_visitante' columns
df.drop(columns=['gols_mandante', 'gols_visitante'], inplace=True)

# Create separate indices for each column
columns_to_index = ['estadio', 'arbitro', 'time_mandante', 'time_visitante', 'tecnico_mandante', 'tecnico_visitante']
indices = {}

for column in columns_to_index:
    unique_names = pd.Series(pd.unique(df[column]))
    name_to_index = {name: idx for idx, name in enumerate(unique_names)}
    indices[column] = name_to_index
    df[column].replace(name_to_index, inplace=True)

# Save the indices to separate files
for column, index in indices.items():
    index_df = pd.DataFrame(list(index.items()), columns=[column, 'index'])
    index_df.to_csv(f'{column}_index.csv', index=False)

# Save the modified DataFrame to a new CSV file
df.to_csv('futebol_modified.csv', index=False)

print("Indices have been saved to separate files and the modified DataFrame has been saved to 'futebol_modified.csv'.")
