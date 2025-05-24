import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from io import StringIO  # added for future-proofing read_html

# === SET YOUR FILE PATH ===
html_path = "/Users/danielhuynh/Classes/CS410-DataEng/DataEngLabs/DataEngLabs/Lab7 - Data Bias/Data/trimet_stopevents_2022-12-07.html"  # <- replace this if needed

# === PARSE HTML ===
with open(html_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

headings = soup.find_all("h2")
tables = soup.find_all("table")
all_dfs = []

# === PARSE TABLES WITH HEADINGS ===
for heading, table in zip(headings, tables):
    heading_text = heading.get_text()
    if "PDX_TRIP" in heading_text:
        trip_id = heading_text.split("PDX_TRIP")[-1].strip().replace(":", "")
        df = pd.read_html(StringIO(str(table)))[0]  # <- wrap in StringIO to avoid FutureWarning
        df["trip_id"] = trip_id
        all_dfs.append(df)

# === CONCATENATE ALL TABLES ===
df = pd.concat(all_dfs, ignore_index=True)
df.columns = [col.lower().strip() for col in df.columns]

# === CREATE stops_df ===
stops_df = df[["trip_id", "vehicle_number", "arrive_time", "location_id", "ons", "offs"]].copy()

# Convert arrive_time to datetime
base_date = datetime(2022, 12, 7)
stops_df["tstamp"] = stops_df["arrive_time"].apply(lambda x: base_date + timedelta(seconds=int(x)))

# Reorder columns
stops_df = stops_df[["trip_id", "vehicle_number", "tstamp", "location_id", "ons", "offs"]]

# === VERIFICATIONS ===
print("\n✅ Data Summary:")
print(f"Total stop events: {len(stops_df)} (should be 93,912)")
print(f"Unique vehicles: {stops_df['vehicle_number'].nunique()}")
print(f"Unique stop locations: {stops_df['location_id'].nunique()}")
print(f"Min tstamp: {stops_df['tstamp'].min()}")
print(f"Max tstamp: {stops_df['tstamp'].max()}")

boarded = stops_df[stops_df["ons"] >= 1]
print(f"Stop events with ≥1 boarding: {len(boarded)}")
print(f"Percentage with boarding: {100 * len(boarded)/len(stops_df):.2f}%")

# === VALIDATION ===

# For location 6913
loc_6913 = stops_df[stops_df["location_id"] == 6913]
num_stops_6913 = len(loc_6913)
unique_buses_6913 = loc_6913["vehicle_number"].nunique()
boarded_6913 = loc_6913[loc_6913["ons"] >= 1]
percent_boarded_6913 = 100 * len(boarded_6913) / num_stops_6913

# For vehicle 4062
veh_4062 = stops_df[stops_df["vehicle_number"] == 4062]
num_stops_4062 = len(veh_4062)
total_boarded_4062 = veh_4062["ons"].sum()
total_deboarded_4062 = veh_4062["offs"].sum()
boarded_stops_4062 = veh_4062[veh_4062["ons"] >= 1]
percent_boarded_4062 = 100 * len(boarded_stops_4062) / num_stops_4062

# === OUTPUT RESULTS ===
print("\n📍 Location 6913:")
print(f"Total stops: {num_stops_6913}")
print(f"Unique buses: {unique_buses_6913}")
print(f"Percentage of stops with ≥1 boarding: {percent_boarded_6913:.2f}%")

print("\n🚌 Vehicle 4062:")
print(f"Total stops: {num_stops_4062}")
print(f"Total passengers boarded: {total_boarded_4062}")
print(f"Total passengers deboarded: {total_deboarded_4062}")
print(f"Percentage of stops with ≥1 boarding: {percent_boarded_4062:.2f}%")

stops_df.to_csv("stops_df.csv", index=False)