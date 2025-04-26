import os

file_path = '/Users/danielhuynh/Classes/CS410-DataEng/DataEngLabs/DataEngLabs/Lab3 - Validation/employees.csv'  # change this to your actual file name
size_in_bytes = os.path.getsize(file_path)
print(f"File size: {size_in_bytes} bytes")

with open(file_path, 'r') as f:
    num_records = sum(1 for line in f) - 1  # subtract 1 if there's a header
    print(f"Number of records: {num_records}")