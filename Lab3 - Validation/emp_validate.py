import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/Users/danielhuynh/Classes/CS410-DataEng/DataEngLabs/DataEngLabs/Lab3 - Validation/employees.csv'  
df = pd.read_csv(file_path)

### Existence Assertion

# Assertion: Every record has a non-null name field
invalid_name_count = df['name'].isnull().sum() + (df['name'].astype(str).str.strip() == '').sum()

# Assertion: Every record has a non-null birthdate field
invalid_birthdate_count = df['birth_date'].isnull().sum() + (df['birth_date'].astype(str).str.strip() == '').sum()

# Print the results
print ("\n### Existence Assertion\nAsserting that every record has a non-null name field...\n")
time.sleep(1)
if invalid_name_count > 0:
    print("Assertion failed: Some records have a null or empty name field.")
    print(f"Number of records with a null or empty name field: {invalid_name_count}")
else:
    print("Assertion passed: All records have a non-null name field.")

time.sleep(1)

### Limit Assertion

# Assertion: Every employee was hired no earlier than 2015
df['hire_date'] = pd.to_datetime(df['hire_date'], errors='coerce')

invalid_hire_date_count = df[df['hire_date'] < pd.Timestamp('2015-01-01')].shape[0]

# Print the results
print ("\n### Limit Assertion\nAsserting that every employee was hired no earlier than 2015...\n")
time.sleep(1)
if invalid_hire_date_count > 0:
    print("Assertion failed: Some employees were hired before 2015.")
    print(f"Number of employees hired before 2015: {invalid_hire_date_count}")
else:
    print("Assertion passed: All employees were hired no earlier than 2015.")
time.sleep(1)

### Intra-Record Assertion

# Assertion: Each employee was born before they were hired
df['birth_date'] = pd.to_datetime(df['birth_date'], errors='coerce')

invalid_birthdates = df[df['birth_date'] >= df['hire_date']].shape[0]

# Print the results
print ("\n### Intra-Record Assertion\nAsserting that every employee was born before they were hired...\n")
time.sleep(1)
if invalid_birthdates > 0:
    print("Assertion failed: Some employees were hired before they were born.")
    print(f"Number of invalid birthdates: {invalid_birthdates}")
else:
    print("Assertion passed: All employees were born before being hired.")
time.sleep(1)

### Inter-Record Assertion

# Assertion: Each employee's manager is a known employee

invalid_manager_count = df[~df['reports_to'].isin(df['eid']) & df['reports_to'].notnull()].shape[0]

# Print the results
print ("\n### Inter-Record Assertion\nAsserting that each employee's manager is a known employee...\n")
time.sleep(1)
if invalid_manager_count > 0:
    print("Assertion failed: Some employees have managers that are not valid employees.")
    print(f"Number of invalid manager references: {invalid_manager_count}")
else:
    print("Assertion passed: All employees' managers are known employees.")
time.sleep(1)

### Summary Assertion

# Assertion: Each city has more than 1 employee
# Assuming 'city' field exists
city_counts = df['city'].value_counts()
invalid_city_count = (city_counts <= 1).sum()

# Print the results
print ("\n### Summary Assertion\nAsserting that each city has more than one employee...\n")
time.sleep(1)
if invalid_city_count > 0:
    print("Assertion failed: Some cities have one or zero employees.")
    print(f"Number of cities with <= 1 employee: {invalid_city_count}")
else:
    print("Assertion passed: All cities have more than one employee.")
time.sleep(1)

### Statistical Assertion

# Assertion: Salaries are normally distributed


# Take mean and median of salaries
salary_mean = df['salary'].mean()
salary_median = df['salary'].median()
pd.set_option('display.max_rows', None)

print(df['salary'])
# Plot the histogram, but limit the x-axis
plt.figure(figsize=(10,6))
plt.hist(df['salary'],bins=range(0, 200001, 10000), edgecolor='black')

# Formatting
plt.title('Salary Distribution (Grouped by $10,000)')
plt.xlabel('Salary Range ($)')
plt.ylabel('Number of Employees')
plt.xticks(range(0, 200001, 10000), rotation=45)  # x-axis ticks every $10k
plt.grid(True)

plt.show()
# Print the results
print ("\n### Statistical Assertion\nAsserting that salaries are roughly normally distributed...\n")
time.sleep(1)

if abs(salary_mean - salary_median) / salary_mean > 0.05:  # Allow small 5% deviation
    print("Assertion failed: Salaries may not be normally distributed (mean and median are too different).")
    print(f"Mean salary: {salary_mean:.2f}, Median salary: {salary_median:.2f}")
else:
    print("Assertion passed: Salaries appear to be roughly normally distributed.")
time.sleep(1)


### Final Record Count

# Count the number of records
with open(file_path, 'r') as f:
    num_records = sum(1 for line in f) - 1  # subtract 1 for the header
print(f"\nNumber of records: {num_records}\n")
