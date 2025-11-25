import pandas as pd

# Load data from CSV
csv_file_path = 'sample_data.csv'
df_csv = pd.read_csv(csv_file_path)

# Display the DataFrame
print("CSV Data:")
print(df_csv)

# Basic data manipulation: Filter by age
filtered_data = df_csv[df_csv['Age'] > 30]
print("\nFiltered Data (Age > 30):")
print(filtered_data)
