# Import libraries
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import cartopy.crs as ccrs
import streamlit as st
import pandas as pd
import plotly.express as px

#set page config
st.set_page_config(page_title="Typhoon Genesis", page_icon="🌀", layout="wide", initial_sidebar_state="expanded")
tab1, tab2, tab3 = st.tabs(["1️⃣ Initial positions of TC genesis", "2️⃣ Monthly Percentage of TC Genesis", "3️⃣ can create more tabs"])

# Set the title of the page
tab1.subheader("Initial Positions of Typhoon Genesis in EAMR(1980-2021)")
tab1.markdown("This map shows the  Initial positions of TC genesis over the Western North Pacific region (WNP) in 1980-2021. In this study, the location of the East Asis Monsoon Region (EAMR) is defined as 10°–50°N, 105°–150°E as shown on the map. ")

# Load the GeoDataFrame
EAMR_1980_initial = gpd.read_file(r'EAMR_1980_initial\EAMR_1980_initial.shp')
EAMR_1980_initial.crs = 'EPSG:4326'

# Create an interactive map plot using Plotly
fig_map = px.scatter_geo(EAMR_1980_initial,
                         lat=EAMR_1980_initial.geometry.y,
                         lon=EAMR_1980_initial.geometry.x,
                         title='Initial Positions of Typhoon Genesis in EAMR (1980-2021)',
                         labels={'geometry': 'Initial Positions'},
                         projection='natural earth', 
                         center={'lat': 30, 'lon': 127.5},  # Center the map around the region
                         fitbounds='locations'
                        )

# Update the layout to make the map plot bigger
fig_map.update_layout(
    width=1000,  # Set the width of the plot
    height=600   # Set the height of the plot
)

# Show the interactive map plot in Streamlit
tab1.plotly_chart(fig_map, key='initial_positions')


# Set the title of the page
tab2.subheader("Monthly Percentage of TC Genesis")
tab2.markdown("This bar plot shows the monthly percentage of TC genesis over the years in the Western North Pacific region (WNP).")

# Convert 'ISO_TIME' column to datetime format
EAMR_1980_initial['ISO_TIME'] = pd.to_datetime(EAMR_1980_initial['ISO_TIME'])

# Extract month from 'ISO_TIME' column
EAMR_1980_initial['Month'] = EAMR_1980_initial['ISO_TIME'].dt.month

# Count the occurrences of TC genesis for each month
monthly_count = EAMR_1980_initial['Month'].value_counts().sort_index()

# Calculate the percentage of TC genesis for each month
total_genesis = monthly_count.sum()
monthly_percentage = (monthly_count / total_genesis) * 100

# Create a DataFrame for Plotly
monthly_percentage_df = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Percentage': monthly_percentage
})

# Create an interactive bar plot using Plotly
monthly_bar = px.bar(monthly_percentage_df, x='Month', y='Percentage', 
             labels={'Percentage': 'Percentage of TC Genesis (%)'},
             title='Monthly Percentage of TC Genesis over the Years')

# Show the interactive plot in Streamlit
tab2.plotly_chart(monthly_bar, key='monthly_percentage')

tab3.markdown("# Hello, this is tab 3")