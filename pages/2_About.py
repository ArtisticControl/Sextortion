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

# Bottom of Sidebar Configuration
st.sidebar.markdown("**Developed by:** [Dr Fernando Forattini](https://fernandoforattini.com)" + "\n**Supported by:**")
st.sidebar.image("https://github.com/ArtisticControl/Platform/blob/main/symeco_logo.png?raw=true", use_column_width=True)

#End of Sidebar Configuration ------

st.title("About our Project")

st.divider()

st.markdown(
    """
    This GovTech initiative engages in a comprehensive study aimed at mitigating the pernicious phenomenon of sextortion,
    while simultaneously advancing the efficacy of public service delivery. Executed through a collaborative effort, the project
    involves entities of academic and research excellence such as [Lero](https://lero.ie/),
    the [DCU Business School's](https://www.dcu.ie/dcubs/dcu-business-school), [Anti-corruption Research Centre](https://www.dcu.ie/arc)
    and [Corruption, Gender, and Sustainable Development (COGS)](https://www.dcu.ie/arc/cogs), helmed by Dr. Fernando Forattini,
    tutored by Prof. Regina Connolly, and Prof. Robert Gillanders. Financial backing for this endeavor is provided by the [SyMeCo Post-Doctoral Fellowship at Lero](https://symeco.lero.ie/).
"""
)
st.subheader("Participants")
st.markdown(
    """
    - **Dr. Fernando Forattini:** Main Researcher. \n
    - **Prof. Regina Connolly:** Tutor.\n
    - **Prof. Robert Gillanders:** Tutor. \n
    - **Lero:** An interdisciplinary research center with an emphasis on advanced software systems and societal ramifications.\n
    - **DCU Business School:** A critical partner contributing governance and managerial insights to the project. \n
    - **Anti-corruption Research Centre and Corruption, Gender, and Sustainable Development (COGS)**: DCU Business School's centers on Anti-Corruption.
"""
)

st.subheader("Objectives and Importance")
st.markdown("""
    Sextortion poses a severe threat to the integrity of public services and serves as an obstruction to gender equity. Its existence
    erodes public trust and hampers the optimal allocation and delivery of resources. This project endeavors to combat sextortion through
    empirical research and technological innovation, thereby contributing to ethical governance and inclusive public administration. 
"""
)

st.subheader("Platform Description")
st.markdown("The digital platform functions as the nexus for all project-related activities and resources. It serves multiple purposes:")
st.markdown(
    """
    \t- To grant stakeholders access to real-time updates and empirically collected data.\n
    - To integrate a secure whistleblowing mechanism, fortified by blockchain technology, into the governance infrastructure.\n
    - To enable scholarly discourse and stakeholder engagement through specialized forums and discussion avenues.\n
    This platform is designed for policymakers, academicians, sector-specific experts interested in the intersection of GovTech, ethics, and public administration, and general public.
"""
)