"""import numpy as np
import matplotlib.pyplot as plt
import folium
from pyproj import Proj, transform

def lla_to_web_mercator(lat, lon):
    # Define projections
    wgs84 = Proj(init='epsg:4326')  # WGS84 coordinate system
    web_mercator = Proj(init='epsg:3857')  # Web Mercator projection used by Google Maps
    # Convert coordinates from WGS84 to Web Mercator
    x, y = transform(wgs84, web_mercator, lon, lat, radians=False)
    return x, y

# Load data from file
file_path = "/Users/ravitejakunchanapalli/Downloads/RTKdemo_file.ASCII"
with open(file_path, 'r') as file:
    data = file.readlines()

# Initialize lists to store parsed data
latitudes = []
longitudes = []

# Parse data from file
for line in data:
    # Split the line into log header and fields
    log_header, fields = line.split(';')
    
    # Split the fields into individual data points
    fields = fields.split(',')
    
    # Extracting relevant data (latitude, longitude, and height)
    lat = float(fields[2])
    lon = float(fields[3])
    
    # Store the parsed data in lists
    latitudes.append(lat)
    longitudes.append(lon)

# Plot the Web Mercator coordinates
plt.figure(figsize=(10, 8))
plt.scatter(latitudes, longitudes, s=5, color='blue')
plt.title('Web Mercator Projection of LLA Coordinates')
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.grid(True)
plt.tight_layout()

# Save the plot as an image file
# plt.savefig('lla_to_web_mercator_plot.png')

# Create a folium map and add the LLA points
m = folium.Map(
    location=[np.mean(latitudes), np.mean(longitudes)], 
    zoom_start=13, 
    tiles='https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
    attr='Google'
)

for lat, lon in zip(latitudes, longitudes):
    folium.CircleMarker(
        location=[lat, lon],
        radius=1,
        color='blue',
        fill=True,
        fill_color='blue'
    ).add_to(m)

try:
    m.save('/Users/ravitejakunchanapalli/Downloads/lla_to_web_mercator_map999.html')
    print("Map saved successfully.")
except Exception as e:
    print("Error saving map:", e)


plt.show()

import numpy as np
import matplotlib.pyplot as plt
import folium
from pyproj import Proj, transform

def lla_to_web_mercator(lat, lon):
    # Define projections
    wgs84 = Proj(init='epsg:4326')  # WGS84 coordinate system
    web_mercator = Proj(init='epsg:3857')  # Web Mercator projection used by Google Maps
    # Convert coordinates from WGS84 to Web Mercator
    x, y = transform(wgs84, web_mercator, lon, lat, radians=False)
    return x, y

# Load data from file
file_path = "/Users/ravitejakunchanapalli/Downloads/RTKdemo_file.ASCII"
with open(file_path, 'r') as file:
    data = file.readlines()

# Initialize lists to store parsed data
latitudes = []
longitudes = []

# Parse data from file
for line in data:
    # Split the line into log header and fields
    log_header, fields = line.split(';')
    
    # Split the fields into individual data points
    fields = fields.split(',')
    
    # Extracting relevant data (latitude, longitude, and height)
    lat = float(fields[2])
    lon = float(fields[3])
    
    # Store the parsed data in lists
    latitudes.append(lat)
    longitudes.append(lon)

# Plot the Web Mercator coordinates
plt.figure(figsize=(10, 8))
plt.scatter(latitudes, longitudes, s=5, color='blue')
plt.title('Web Mercator Projection of LLA Coordinates')
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.grid(True)
plt.tight_layout()

# Save the plot as an image file
plt.savefig('lla_to_web_mercator_plot.png')

# Create a folium map and add the LLA points
m = folium.Map(
    location=[np.mean(latitudes), np.mean(longitudes)], 
    zoom_start=15,  # Adjust the zoom level here
    tiles='https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
    attr='Google'
)

for lat, lon in zip(latitudes, longitudes):
    folium.CircleMarker(
        location=[lat, lon],
        radius=1,
        color='blue',
        fill=True,
        fill_color='blue'
    ).add_to(m)

# Save the map as an HTML file
m.save('/Users/ravitejakunchanapalli/Downloads/lla_to_web_mercator_map8888.html')

plt.show()"""
import numpy as np
import matplotlib.pyplot as plt
import folium
from pyproj import Proj, transform

def lla_to_web_mercator(lat, lon):
    # Define projections
    wgs84 = Proj(init='epsg:4326')  # WGS84 coordinate system
    web_mercator = Proj(init='epsg:3857')  # Web Mercator projection used by Google Maps
    # Convert coordinates from WGS84 to Web Mercator
    x, y = transform(wgs84, web_mercator, lon, lat, radians=False)
    return x, y

# Load data from file
file_path = "/Users/ravitejakunchanapalli/Downloads/RTKdemo_file.ASCII"
with open(file_path, 'r') as file:
    data = file.readlines()

# Initialize lists to store parsed data
latitudes = []
longitudes = []

# Parse data from file
for line in data:
    # Split the line into log header and fields
    log_header, fields = line.split(';')
    
    # Split the fields into individual data points
    fields = fields.split(',')
    
    # Extracting relevant data (latitude, longitude, and height)
    lat = float(fields[2])
    lon = float(fields[3])
    
    # Store the parsed data in lists
    latitudes.append(lat)
    longitudes.append(lon)

# Plot the Web Mercator coordinates
plt.figure(figsize=(10, 8))
plt.scatter(latitudes, longitudes, s=5, color='blue')
plt.title('Web Mercator Projection of LLA Coordinates')
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.grid(True)
plt.tight_layout()

# Save the plot as an image file
plt.savefig('lla_to_web_mercator_plot.png')

# Create a folium map and add the LLA points
m = folium.Map(
    location=[np.mean(latitudes), np.mean(longitudes)], 
    zoom_start=18,  # Set the zoom level similar to Google Maps
    tiles='https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
    attr='Google'
)

for lat, lon in zip(latitudes, longitudes):
    folium.CircleMarker(
        location=[lat, lon],
        radius=1,
        color='blue',
        fill=True,
        fill_color='blue'
    ).add_to(m)

# Save the map as an HTML file
m.save('/Users/ravitejakunchanapalli/Downloads/lla_to_webnew.html')

plt.show()




