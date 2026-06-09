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
st.session_state.messages.append({"role": "user", "content": prompt})   
# Pehle Gemini model ko call karke response generate karein
    response = model.generate_content(prompt)

    # Line 25: Assistant ka chat box kholna
    with st.chat_message("assistant"):
        # Line 26: AI ka jawab screen par dikhana
        st.markdown(response.text)
    
    # Line 27: AI ka jawab history (session_state) mein save karna
    st.session_state.messages.append({"role": "assistant", "content": response.text})

