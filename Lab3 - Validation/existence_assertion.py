import pandas as pd

# Load the dataset
file_path = '/Users/danielhuynh/Classes/CS410-DataEng/DataEngLabs/DataEngLabs/Lab3 - Validation/employees.csv'  # change this to your actual file name
df = pd.read_csv(file_path)

# Count rows where 'name' is null or empty
invalid_name_count = df['name'].isnull().sum() + (df['name'].astype(str).str.strip() == '').sum()
invalid_birthdate_count = df['birth_date'].isnull().sum() + (df['birth_date'].astype(str).str.strip() == '').sum()

print(f"Number of records with a null or empty name field: {invalid_name_count}")
print(f"Number of records with a null or empty birthdate field: {invalid_birthdate_count}")



with open(file_path, 'r') as f:
    num_records = sum(1 for line in f) - 1  # subtract 1 if there's a header
    print(f"Number of records: {num_records}")