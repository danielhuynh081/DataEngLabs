import pandas as pd

# Load the dataset
file_path = '/Users/danielhuynh/Classes/CS410-DataEng/DataEngLabs/DataEngLabs/Lab3 - Validation/employees.csv'  # change this to your actual file name
df = pd.read_csv(file_path)

# Convert 'hire_date' to datetime, ignore invalid formats
df['hire_date'] = pd.to_datetime(df['hire_date'], errors='coerce')

# Count how many employees were hired before 2015
hired_before_2015_count = df[df['hire_date'] < pd.Timestamp('2015-01-01')].shape[0]

print(f"Number of employees hired before 2015: {hired_before_2015_count}")


# Count how many employees were hired after 2020
hired_after_2020_count = df[df['hire_date'] > pd.Timestamp('2020-12-31')].shape[0]

print(f"Number of employees hired after 2020: {hired_after_2020_count}")



