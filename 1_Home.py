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

st.title("Sextortion in Public Service Delivery and the Role of GovTech (Mock-Up)")

st.divider()

st.markdown(
    """
    In today's global reality, marred by political-economic crisis and growing inequality, corruption is a pressing concern.
    It detrimentally impacts economic growth, hinder essential services, subverts the rule of law, and compromise human rights.
    Corruption erodes public trust in democratic institutions, disproportionately affecting marginalized communities and
    perpetuating social disparities. Within corruption, lies a underexplored form: **sextortion**, a darker variant involving
    the abuse of power for sexual favors. \n
    *Sextortion inflicts severe physical and psychological harm, fosters government distrust, disproportionately affecting women
    and vulnerable individuals. Despite advancements in anti-corruption efforts, enduring challenges persist due to the absence
    of solutions rooted in historical and sociological insights capable of addressing the varied nature of corruption.* \n
    In response to these pressing issues, this webapp emerges as an innovative platform designed to bridge the gap between scholarly
    research and actionable interventions against sextortion. This initiative, which is the culmination of years of scholarly investigation,
    aims to facilitate academic research, data-informed policymaking and elevate advocacy campaigns. By synthesizing extensive research
    outcomes, legal frameworks, and real-time analyses into an interactive, user-centric interface, this platform provides a robust foundation
    for diverse stakeholders to engage in targeted, evidence-based strategies to combat corruption and sextortion.\n The platform's features,
    including dynamic mapping and analyses, legal and policy insights, and stakeholder communication mechanisms, serve as instrumental resources
    for understanding and tackling the multifaceted challenge of sextortion.\n
    Thus, this platform does not merely serve as an academic repository; *it embodies a transformative infrastructure that contributes to the
    dismantling of corruption, fostering an increasingly equitable societal landscape*.

"""
)

st.text("")
