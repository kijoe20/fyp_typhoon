#read EAMR_1980_initial shapefile
EAMR_1980_initial = gpd.read_file(r'EAMR_1980_initial\EAMR_1980_initial.shp')
#2nd version
EAMR_1980_initial.crs = 'EPSG:4326'

# Create the map plot
fig = plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())

# Plot the GeoDataFrame with the points
EAMR_1980_initial.plot(ax=ax, markersize=2, color='blue', transform=ccrs.PlateCarree())

# Add coastlines, gridlines, and colorbar
ax.coastlines()
ax.gridlines(draw_labels=True)

# Set the plot title
plt.title('Initial Positions of Typhoon Genesis in EAMR(1980-2021)')

# Set the lim for the map
ax.set_xlim(105, 150)
ax.set_ylim(10, 50)

# Show the plot in Streamlit
st.pyplot(fig)