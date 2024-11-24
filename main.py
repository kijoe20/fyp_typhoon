#import libraries
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import cartopy.crs as ccrs
import streamlit as st

#set page config
st.set_page_config(page_title="Typhoon Genesis", page_icon="🌀", layout="wide", initial_sidebar_state="expanded")
st.caption("Final Year Project: Typhoon Genesis Analysis")
st.title("Typhoon Genesis Analysis in East Asia Monsoon Region (EAMR)")
with st.sidebar:
    st.markdown("## Typhoon Genesis Analysis")

