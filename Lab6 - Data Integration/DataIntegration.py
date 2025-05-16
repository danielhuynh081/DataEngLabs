# Lab 6 - Data Integration: Combine COVID and Census data to analyze county-level patterns
# CS410 - Data Engineering w/ Bruce Irvin 
# Daniel Huynh, May 13th, 2025

# Import Libraries
import pandas as pd

# File Paths
confirmed_file = '/Users/danielhuynh/Classes/CS410-DataEng/DataEngLabs/DataEngLabs/Lab6 - Data Integration/Data-Tables/covid_confirmed_usafacts.csv'
deaths_file = '/Users/danielhuynh/Classes/CS410-DataEng/DataEngLabs/DataEngLabs/Lab6 - Data Integration/Data-Tables/covid_deaths_usafacts.csv'
county_file = '/Users/danielhuynh/Classes/CS410-DataEng/DataEngLabs/DataEngLabs/Lab6 - Data Integration/Data-Tables/acs2017_county_data.csv'

# Load CSV Files
cases_df = pd.read_csv(confirmed_file)
deaths_df = pd.read_csv(deaths_file)
census_df = pd.read_csv(county_file)

# Trim Dataframes
cases_df = cases_df[['County Name', 'State', '2023-07-23']]
deaths_df = deaths_df[['County Name', 'State', '2023-07-23']]
census_df = census_df[['County', 'State', 'TotalPop', 'IncomePerCap', 'Poverty', 'Unemployment']]

# Show Column headers
print("Cases DataFrame Columns:", cases_df.columns)
print("Deaths DataFrame Columns:", deaths_df.columns)
print("Census DataFrame Columns:", census_df.columns)

### Integration Challenge 1
# Strip Extra Spaces
cases_df['County Name'] = cases_df['County Name'].str.strip()
deaths_df['County Name'] = deaths_df['County Name'].str.strip()

# Check for Washington County in both Data Frames
print(cases_df[cases_df['County Name'] == 'Washington County'])
print(deaths_df[deaths_df['County Name'] == 'Washington County'])

# Check the amount of Washington County data in both Data Frames
print("Cases DataFrame Washington County Count:", len(cases_df[cases_df['County Name'] == 'Washington County']))
print("Deaths DataFrame Washington County Count:", len(deaths_df[deaths_df['County Name'] == 'Washington County']))

### Integration Challenge 2
# Revove Statewide Unallocated
cases_df = cases_df[cases_df['County Name'] != 'Statewide Unallocated']
deaths_df = deaths_df[deaths_df['County Name'] != 'Statewide Unallocated']

# Check deletion && Row Count 
print("Cases:",cases_df[cases_df['County Name'] == 'Statewide Unallocated'])
print("Deaths:",deaths_df[deaths_df['County Name'] == 'Statewide Unallocated'])
print("Cases DataFrame Row Count:", len(cases_df))
print("Deaths DataFrame Row Count:", len(deaths_df))


### Integration Challenge 3

# Use Public Code
us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "Virgin Islands, U.S.": "VI",
}
    
# invert the dictionary
abbrev_to_us_state = dict(map(reversed, us_state_to_abbrev.items()))

# Convert state abbreviations to full names in cases_df
cases_df['State'] = cases_df['State'].map(abbrev_to_us_state)

# Convert state abbreviations to full names in deaths_df
deaths_df['State'] = deaths_df['State'].map(abbrev_to_us_state)

print("Cases DataFrame State Abbreviations:\n", cases_df.head())

### Integration Challenge 4

# Create Key Collumn
cases_df['key'] = cases_df['County Name'] + ", " + cases_df['State']
deaths_df['key'] = deaths_df['County Name'] + ", " + deaths_df['State']
census_df['key'] = census_df['County'] + ", " + census_df['State']

# Set Index
cases_df = cases_df.set_index('key')
deaths_df = deaths_df.set_index('key')
census_df = census_df.set_index('key')

# Show Output
print("Cases DataFrame:\n", cases_df.head())

### Integration Challegenge 5

# Rename Columns
cases_df = cases_df.rename(columns={'2023-07-23': 'Cases'})
deaths_df = deaths_df.rename(columns={'2023-07-23': 'Deaths'})

# Print
print("New Columns:\n",cases_df.columns.values.tolist())

### Do The Integration

# Step 1: Rename the date column
cases_df = cases_df.rename(columns={'2023-07-23': 'Cases'})
deaths_df = deaths_df.rename(columns={'2023-07-23': 'Deaths'})

# Step 2: Set index to ["County Name, State"] for all
cases_df.index = cases_df["County Name"] + ", " + cases_df["State"]
deaths_df.index = deaths_df["County Name"] + ", " + deaths_df["State"]
census_df.index = census_df["County"] + ", " + census_df["State"]

# Step 3: Drop redundant columns to avoid column name conflicts
cases_df = cases_df.drop(columns=["County Name", "State"])
deaths_df = deaths_df.drop(columns=["County Name", "State"])
census_df = census_df.drop(columns=["County", "State"])

# Step 4: Join using .join() twice
join1 = cases_df.join(deaths_df)
join_df = join1.join(census_df)

# Step 5: Add per capita columns
join_df["CasesPerCap"] = join_df["Cases"] / join_df["TotalPop"]
join_df["DeathsPerCap"] = join_df["Deaths"] / join_df["TotalPop"]

# Step 6: Output
print("join_df:\n", join_df.head())
print("join_df row count:", join_df.shape[0])

###  Analyze

# Create a correlation matrix using .corr()
# Select only numeric columns
correlation_matrix = join_df.select_dtypes(include='number').corr()
print(correlation_matrix)


### Visualize

# Provided Code to visualize the correlation matrix
import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

plt.title('Correlation Matrix Heatmap')
plt.show()
