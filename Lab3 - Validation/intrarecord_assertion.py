import pandas as pd

# Load the dataset
file_path = '/Users/danielhuynh/Classes/CS410-DataEng/DataEngLabs/DataEngLabs/Lab3 - Validation/employees.csv'  # change this to your actual file name
df = pd.read_csv(file_path)
# Make sure birth_date and hire_date are datetime objects
df['birth_date'] = pd.to_datetime(df['birth_date'], errors='coerce')
df['hire_date'] = pd.to_datetime(df['hire_date'], errors='coerce')

# Check if any hire_date is before birth_date (invalid)
invalid_birth_vs_hire = df[df['hire_date'] < df['birth_date']]

print(f"Number of records where employee was hired before being born: {len(invalid_birth_vs_hire)}")
