# /Users/danielhuynh/Classes/CS410-DataEng/DataEngLabs/DataEngLabs/Lab4 - Data Transpotation/data/bc_trip259172515_230215.csv
# use the pandas.read_csv() method to read it into a DataFrame

import pandas as pd

# Load the dataset into a dataframe
file_path = '/Users/danielhuynh/Classes/CS410-DataEng/DataEngLabs/DataEngLabs/Lab4 - Data Transpotation/data/bc_trip259172515_230215.csv'
df = pd.read_csv(file_path)

# how many breadcrumbs are in the dataset
print(f"Number of breadcrumbs in the dataset: {len(df)}")

# Filtering

# Remove the EVENT_NO_STOP , GPS_ATELLITES, GPS_HDOP column
#df = df.drop(columns=['EVENT_NO_STOP'])

#df = df.drop(columns=['GPS_SATELLITES', 'GPS_HDOP'])

# Usecol to filter

# df = pd.read_csv(file_path, usecols=['EVENT_NO_TRIP', 'OPD_DATE', 'VEHICLE_ID', 'METERS','ACT_TIME', 'GPS_LONGITUDE', 'GPS_LATITUDE'])



# Decode


def timestampColumn(row):
    opd_date = pd.to_datetime(row['OPD_DATE'], format='%d%b%Y:%H:%M:%S', errors='coerce')
    timestamp = opd_date + pd.to_timedelta(row['ACT_TIME'], unit='s')
    return timestamp

df['TIMESTAMP'] = df.apply(timestampColumn, axis = 1)
df = df.drop(columns=['OPD_DATE', 'ACT_TIME'])
print(df.columns)

# 1. Calculate differences
df['dMETERS'] = df['METERS'].diff()
df['dTIMESTAMP'] = df['TIMESTAMP'].diff().dt.total_seconds()

# 3. Calculate SPEED (meters per second)
df['SPEED'] = df.apply(lambda row: row['dMETERS'] / row['dTIMESTAMP'] if row['dTIMESTAMP'] != 0 else 0, axis=1)

# 4. Remove the dMETERS and dTIMESTAMP columns
df = df.drop(columns=['dMETERS', 'dTIMESTAMP'])


print("Minimum speed:", df['SPEED'].min())
print("Maximum speed:", df['SPEED'].max())
print("Average speed:", df['SPEED'].mean())


print(df.head(10))
