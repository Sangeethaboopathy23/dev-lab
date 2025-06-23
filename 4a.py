import pandas as pd

data = {
    'Week Start': ['2025-05-25', '2025-06-01', '2025-06-08',
                   '2025-05-25', '2025-06-01', '2025-06-08',
                   '2025-05-25', '2025-06-01', '2025-06-08'],
    'City': ['Chennai', 'Chennai', 'Chennai',
             'Mumbai', 'Mumbai', 'Mumbai',
             'Delhi', 'Delhi', 'Delhi'],
    'Max Temp': [38.2, 38.6, 39.0,
                 33.0, 33.7, 34.0,
                 37.5, 38.2, 39.0],
    'Min Temp': [27.1, 28.2, 28.5,
                 25.0, 25.5, 26.0,
                 24.5, 25.6, 26.0],
    'Avg Temp': [32.7, 33.4, 33.8,
                 29.0, 29.6, 30.0,
                 31.0, 31.9, 32.5]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

df['Week Start'] = pd.to_datetime(df['Week Start'])
df['Month'] = df['Week Start'].dt.month

sum_by_city_month = df.groupby(['City', 'Month'])[['Max Temp', 'Min Temp', 'Avg Temp']].sum().reset_index()

print("\nSum of Temperatures by City and Month:")
print(sum_by_city_month)

pivot_max = sum_by_city_month.pivot(index='City', columns='Month', values='Max Temp')
pivot_min = sum_by_city_month.pivot(index='City', columns='Month', values='Min Temp')
pivot_avg = sum_by_city_month.pivot(index='City', columns='Month', values='Avg Temp')

print("\nMonth-wise Sum of Max Temperature:")
print(pivot_max)

print("\nMonth-wise Sum of Min Temperature:")
print(pivot_min)

print("\nMonth-wise Sum of Avg Temperature:")
print(pivot_avg)
# Sum all temperature types to get a total temperature per city per month
sum_by_city_month['Total Temp'] = sum_by_city_month['Max Temp'] + sum_by_city_month['Min Temp'] + sum_by_city_month['Avg Temp']

# Sum total temperature across all months for each city
total_temp_by_city = sum_by_city_month.groupby('City')['Total Temp'].sum().reset_index()

# Find city with the highest total temperature
max_temp_city = total_temp_by_city.loc[total_temp_by_city['Total Temp'].idxmax()]

print(f"City with the highest total temperature: {max_temp_city['City']} with total temperature {max_temp_city['Total Temp']:.2f}")
