import pandas as pd
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trucking_app.settings')
django.setup()

from schedules.models import TruckSchedule

# Load Excel file
file_path = r"C:\Users\lucas\Desktop\Apps for Work\trucking_app_v2\data\ICN_Master_File.xlsx"
df = pd.read_excel(file_path)

# Standardize column names (replace spaces with underscores and lowercase)
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(' ', '_', regex=False)
)

# Convert all columns to string and strip whitespace (column-by-column)
for col in df.columns:
    df[col] = df[col].astype(str).str.strip()

# Define time fields
time_fields = [
    'load_start_time',
    'load_complete_time',
    'depart_time',
    'arrive_time',
    'unload_time'
]

# Convert each time field into a valid HH:MM string (dropping seconds)
for field in time_fields:
    # Attempt to parse the column as datetimes; unparseable values become NaT
    dt_series = pd.to_datetime(df[field], errors='coerce')
    # Extract the time component (python time objects) or NaT
    time_series = dt_series.dt.time
    # Replace NaT with None so that .strftime() doesn't throw an error
    time_series = time_series.where(time_series.notna(), None)
    # Convert each time object to "HH:MM" or "00:00" if None
    df[field] = time_series.apply(
        lambda t: t.strftime('%H:%M') if t is not None else "00:00"
    )

# Insert data into the database
for _, row in df.iterrows():
    TruckSchedule.objects.create(
        origin=row['from'],
        destination=row['to'],
        transit_time=row['transit_time'],
        load_day=row['load_day'],
        load_start_time=row['load_start_time'] if row['load_start_time'] not in ["nan", ""] else None,
        load_complete_time=row['load_complete_time'] if row['load_complete_time'] not in ["nan", ""] else None,
        depart_day=row['depart_day'],
        depart_time=row['depart_time'] if row['depart_time'] not in ["nan", ""] else None,
        arrive_day=row['arrive_day'],
        arrive_time=row['arrive_time'] if row['arrive_time'] not in ["nan", ""] else None,
        unload_day=row['unload_day'],
        unload_time=row['unload_time'] if row['unload_time'] not in ["nan", ""] else None
    )

print("✅ Trucking schedule reimported successfully with correct times!")
