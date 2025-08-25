import geopandas as gpd
import matplotlib.pyplot as plt

world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

plt.figure(figsize=(12, 6))
world.plot(color="lightblue", edgecolor="black")
plt.title("World Map - Countries")
plt.show()

plt.figure(figsize=(12, 6))
world.plot(column="continent", legend=True, cmap="tab20", edgecolor="black")
plt.title("World Map Colored by Continent")
plt.show()

india = world[world["name"] == "India"]

plt.figure(figsize=(6, 8))
india.plot(color="orange", edgecolor="black")
plt.title("India Map")
plt.show()

try:
    india_states = gpd.read_file("india_states.shp")
    plt.figure(figsize=(8, 10))
    india_states.plot(column="state_name", cmap="tab20", legend=False, edgecolor="black")
    plt.title("Map of Indian States")
    plt.show()
except:
    print("india_states.shp not found")

try:
    india_districts = gpd.read_file("india_districts.shp")
    plt.figure(figsize=(8, 10))
    india_districts.plot(column="district", cmap="tab20c", legend=False, edgecolor="black")
    plt.title("Map of Indian Districts")
    plt.show()
except:
    print("india_districts.shp not found")
