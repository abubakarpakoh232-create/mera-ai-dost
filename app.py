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
   
  # User ka input handle karne ka block
if prompt := st.chat_input("Kya poochna hai?"):
    
    # 1. User ka message screen par dikhana aur save karna
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. Gemini Model ko call karna
    response = model.generate_content(prompt) 

    # 3. AI ka jawab screen par dikhana
    with st.chat_message("assistant"):
        st.markdown(response.text)
    
    # 4. AI ka jawab history mein save karna
    st.session_state.messages.append({"role": "assistant", "content": response.text})
