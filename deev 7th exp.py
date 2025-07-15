import pandas as pd
import folium
import random

# STEP 2 & 3: Generate random data and create a DataFrame
data = {
    'Place': ['Location A', 'Location B', 'Location C', 'Location D', 'Location E'],
    'Latitude': [random.uniform(10.0, 20.0) for _ in range(5)],
    'Longitude': [random.uniform(75.0, 85.0) for _ in range(5)]
}
df = pd.DataFrame(data)

# STEP 4: Save the DataFrame to a CSV file
df.to_csv('map_data.csv', index=False)

# STEP 5: Load the generated CSV file
df = pd.read_csv('map_data.csv')

# STEP 6: Create a base map centered at average location
map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
my_map = folium.Map(location=map_center, zoom_start=6)

# STEP 7: Add data points to the map with mouse rollover popups
for _, row in df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=row['Place']
    ).add_to(my_map)

# STEP 8: Save the map as an HTML file
my_map.save('interactive_map.html')
