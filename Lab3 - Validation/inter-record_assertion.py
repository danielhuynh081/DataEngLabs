import pandas as pd

# Load the dataset
file_path = '/Users/danielhuynh/Classes/CS410-DataEng/DataEngLabs/DataEngLabs/Lab3 - Validation/employees.csv'  # change this to your actual file name
df = pd.read_csv(file_path)
valid_eids = set(df['eid'])

# Find records where 'reports_to' is NOT in the list of valid eids (and not null)
invalid_managers = df[~df['reports_to'].isin(valid_eids) & df['reports_to'].notnull()]

print(f"Number of records with an unknown manager: {len(invalid_managers)}")
