import streamlit as st

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

# End of Sidebar Configuration


# Bottom of Sidebar Configuration
st.sidebar.markdown("**Developed by:** [Dr Fernando Forattini](https://fernandoforattini.com)" + "\n**Supported by:**")
st.sidebar.image("https://github.com/ArtisticControl/Platform/blob/main/symeco_logo.png?raw=true", use_column_width=True)