import pandas as pd

# Load your data
data = pd.read_csv('gdi.csv')

# Load the latitude and longitude dataset
latlong_data = pd.read_csv('lat_long.csv', encoding='ISO-8859-1')

# Merge the data based on country names
merged_data = pd.merge(data, latlong_data, on='Country', how='left')

# This will merge based on the 'Country' column, and countries that do not exist in one of the datasets will still be included 
# in the merged dataset but with NaN values in columns from the dataset where they are missing.

# Save the merged data for future use (optional)
merged_data.to_csv('merged_data.csv', index=False)
