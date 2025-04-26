import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
file_path = '/Users/danielhuynh/Classes/CS410-DataEng/DataEngLabs/DataEngLabs/Lab3 - Validation/employees.csv'  # change this to your actual file name
df = pd.read_csv(file_path)
# Group by 'city' and count employees


# Drop null or non-numeric salaries (just in case)
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
valid_salaries = df['salary'].dropna()

# Plot histogram with a KDE (smoothed line)
plt.figure(figsize=(10,6))
sns.histplot(valid_salaries, kde=True, bins=30)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.savefig("salary_histogram.png")  # Save for screenshot submission
plt.show()