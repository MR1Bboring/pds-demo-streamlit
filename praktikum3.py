import streamlit as st
import folium
from streamlit_folium import st_folium

# title
st.title("contoh integrasi folium +streamlit")

#titik peta indonesia
center_lat = -2.5489
center_lon = 118.0149
m = folium.Map(location=[center_lat, center_lon], zoom_start=5)

#tampilkan di streamlit
st_folium(m, width=700, height=500)