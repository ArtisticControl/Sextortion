import streamlit as st
import smtplib
from email.mime.text import MIMEText

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


def send_email(subject, message_body, to_email):
    # Your email details
    SMTP_SERVER = 'smtp.youremailprovider.com' # e.g., for Gmail it's 'smtp.gmail.com'
    SMTP_PORT = 587  # or 465 for Gmail with SSL
    SENDER_EMAIL = 'your_email@gmail.com'
    SENDER_PASSWORD = 'your_password'

    msg = MIMEText(message_body)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Upgrade the connection to SSL/TLS
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, [to_email], msg.as_string())
        server.quit()
        return True
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return False

st.header("Contact Us")
st.write("""
    If you have any questions or suggestions, contact us.\n
    **Please provide your contact details:**
"""
)

name = st.text_input("*Name:*")
email = st.text_input("*Email:*")
message = st.text_area("*Message:*")

col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12 = st.columns(12)
submit = col1.button("Submit")

if submit:
    if "@" in email and "." in email:
        # Sending the email
        email_subject = "Contact Form Submission from " + name
        email_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        # Send the email to yourself or to a designated contact email
        if send_email(email_subject, email_body, "contact@yourdomain.com"):
            st.success("Thank you for your message!")
    else:
        st.error("Please provide a valid email address.")