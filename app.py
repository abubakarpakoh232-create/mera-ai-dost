import streamlit as st
import google.generativeai as genai

st.title("Mera AI Dost 🤖")
st.write("Abu Bakar ka AI Dost")

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Kya poochna hai?"):
    with st.chat_message("user"):
        st.markdown(prompt)
   
    with st.chat_message("assistant"):
        response = model.generate_content(prompt)
        st.markdown(response.text)
st.session_state.messages.append("role" "user", content prompt   

   st.session_state.messages.append("role": assistan
