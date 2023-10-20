import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

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

# Bottom of Sidebar Configuration
st.sidebar.markdown("**Developed by:** [Dr Fernando Forattini](https://fernandoforattini.com)" + "\n**Supported by:**")
st.sidebar.image("https://github.com/ArtisticControl/Platform/blob/main/symeco_logo.png?raw=true", use_column_width=True)

#End of Sidebar Configuration ------

st.markdown('### Brazilian Indicators Used by This Study')

def main():
    # Creating two columns for the menu
    col1, col2, col3 = st.columns((2, 5, 3))
    
    # Adding menu options in the two columns
    with col1:
        selected_date = st.date_input("Preferred Date:", None)
        
    with col2:
        data_type = st.selectbox("Preferred Type of Data:", ["New Cases", "Accumulated Cases", "Other Data"])
        # You can add any other controls or information you want in this column
    
    with col3:
        data_type = st.multiselect("Preferred Variables:", ["State", "Colum1", "Colum2",])
        # Placeholder for any future additions
        pass
    
    # Space
    st.divider()

    # Displaying the map below
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Violence Against Women")
        #st.map(braz_df, zoom=3.3, color= '#0044ff')
        df = pd.DataFrame(
            np.random.randn(500, 2) / [0.25, 0.3] + [-13, -50],
            columns=['lat', 'lon'])

        st.map(df, zoom=3, color='#728FCE')

        # Map Data Frame
        braz_df = pd.DataFrame({
            'latitude': [-15],
            'longitude': [-55]
        })


    #Histogram
    with col2:
        st.markdown("### Presence of 'Corruption' in Political Discourses (by Party)")
        df = px.data.iris()
        fig = px.scatter(
            df,
            x="sepal_width",
            y="sepal_length",
            color="sepal_length",
            color_continuous_scale="reds",
        )
        tab1, tab2 = st.tabs(["By Decade", "Multiple Tabs can be Added"])
        with tab1:
            st.plotly_chart(fig, theme="streamlit", use_container_width=True)
        with tab2:
            st.plotly_chart(fig, theme=None, use_container_width=True)

    # Another Row
    st.markdown("### Relation Between Female Life Expectancy, GDPperCap and Population (Per Country)")
    df = px.data.gapminder()

    fig = px.scatter(
        df.query("year==2007"),
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        hover_name="country",
        log_x=True,
        size_max=60,
    )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

if __name__ == "__main__":
    main()