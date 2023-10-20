import pandas as pd
import streamlit as st
import folium
import pandas as pd
import plost
from streamlit_folium import folium_static

# Set the page configuration
st.set_page_config(
    layout="wide",
    page_title="GovSafe: Sextortion Mitigation WebApp",
    page_icon="https://github.com/ArtisticControl/Platform/blob/main/favicon.png?raw=true",
    initial_sidebar_state="expanded"
)

# Load the CSS from the external stylesheet
with open("css/style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

gdi = pd.read_csv("data/gdi/gdi.csv")
max_gdi = gdi["Gender Development Index (2021)"].max()
seattle_weather = pd.read_csv('data/seattle-weather.csv', parse_dates=['date']) #scraps

# Row A: two columns
col1, col2 = st.columns((5.2, 4.8))
# Column 1 = Map
with col1:
    st.markdown("### Useful Maps")
    bins_list = sorted(set([0.4, 0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1, 1.02, max_gdi]))
    political_countries = ("data/countries.geojson")
            
    # Map
    m = folium.Map(location=(30, 10), zoom_start=1.5, tiles="cartodb positron")
    folium.Choropleth(
        geo_data=political_countries,
        data=gdi,
        columns=["Country", "Gender Development Index (2021)"],
        key_on="feature.properties.name",
        bins=bins_list,
        fill_color="RdYlBu",
        fill_opacity=0.8,
        line_opacity=0.3,
        nan_fill_color="white",
        legend_name="Gender Development Index (2021)",
        name="Countries by Gender Development Index(2021)"
    ).add_to(m)
    folium.LayerControl().add_to(m)

    folium_static(m)
    
with col2:
    time_hist_color = 'gdi'
            
    st.markdown('### Historical Data Comparison')
    plost.time_hist(
        data=seattle_weather,
        date='date',
        x_unit='week',
        y_unit='day',
        color=time_hist_color,
        aggregate='median',
        legend=None,
        height=270,
        use_container_width=True
    )
    
    # Infor Below Heatmap
    country = st.selectbox("*For Specific Data, Select a Country:*", gdi['Country'].unique())
    
    # Slider for Year
    year = st.slider("*And Select a Year:*", 1990, 2021)

    # Filter data based on user selections
    filtered_gdi = gdi[gdi['Country'] == country]
    gdi_value = filtered_gdi[f'Gender Development Index ({year})'].values[0]
    # Display GDI value for the selected country
    st.write(f"For **{country}** in **{year}**, the GDI score was **{gdi_value}**.")

#Row B: Two Columns Plus Line Chart
st.markdown('### Line chart')

col1, col2=st.columns((4,6))
with col1:
    plot_data = st.multiselect('*Select data*', ['gender violence', 'gdi', 'cpi', 'female education'], ['gdi', 'cpi'])
    
with col2:
    plot_height = st.slider('*Select plot height*', 200, 350, 250)

st.line_chart(seattle_weather, x = 'date', y = plot_data, height = plot_height)

# Bottom of Sidebar Configuration
st.sidebar.markdown("**Developed by:** [Dr Fernando Forattini](https://fernandoforattini.com)" + "\n**Supported by:**")
st.sidebar.image("https://github.com/ArtisticControl/Platform/blob/main/symeco_logo.png?raw=true", use_column_width=True)