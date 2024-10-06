
#import libraries
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import cartopy.crs as ccrs
import streamlit as st

# Load land data
@st.cache_data
def load_land_data():
    return gpd.read_file(r'ne_50m_land/ne_50m_land.shp')

land = load_land_data()

# Streamlit slider for longitude range
lon_range = st.slider("Select Longitude Range", min_value=80, max_value=180, value=(105, 150))
lat_range = st.slider("Select Latitude Range", min_value=-10, max_value=60, value=(10, 50))

# Define the bounding box based on user input
bbox = [(lon_range[0], lat_range[0]), (lon_range[1], lat_range[0]), 
        (lon_range[1], lat_range[1]), (lon_range[0], lat_range[1])]
region_polygon = Polygon(bbox)

# Intersect the land geometry with the desired region
clipped_land = land.geometry.intersection(region_polygon)

# Create a new GeoDataFrame with the clipped geometry
EAMR_land = gpd.GeoDataFrame(geometry=clipped_land, crs=land.crs)

# Set CRS
EAMR_land.crs = ccrs.PlateCarree()

# Streamlit app layout
st.title("Land Data Visualization")

# Plot the clipped land data
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': ccrs.PlateCarree()})
EAMR_land.plot(ax=ax, color='lightgreen', edgecolor='black')

# Set the title and labels
ax.set_title("Clipped Land Data ", fontsize=16)
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")

# Display the plot in Streamlit
st.pyplot(fig)