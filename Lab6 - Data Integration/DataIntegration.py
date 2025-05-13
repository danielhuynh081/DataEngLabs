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
