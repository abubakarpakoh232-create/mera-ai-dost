import streamlit as st
from google import genai

st.set_page_config(page_title="Mera AI Dost", page_icon="🤖")

st.title("Mera AI Dost 🤖")

# API key Streamlit secrets se lena
client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])

user_input = st.text_input("Apna message likho:")

if user_input:
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=user_input
        )

        st.write("🤖 AI:", response.text)

    except Exception as e:
        st.error(f"Error aaya: {e}")
