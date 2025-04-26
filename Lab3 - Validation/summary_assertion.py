import pandas as pd

# Load the dataset
file_path = '/Users/danielhuynh/Classes/CS410-DataEng/DataEngLabs/DataEngLabs/Lab3 - Validation/employees.csv'  # change this to your actual file name
df = pd.read_csv(file_path)
# Group by 'city' and count employees
city_counts = df['city'].value_counts()

# Find cities with only 1 employee
cities_with_one_employee = city_counts[city_counts ==1]

print(f"Number of cities with only one employee: {len(cities_with_one_employee)}")
print("Cities with only one employee:")
print(cities_with_one_employee)