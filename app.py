# ===============================================
# Abu Bakar ka AI Dost - Streamlit + Gemini AI
# Version: 1.2 - All-in-One Safe Auto Version
# ===============================================

import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(page_title="Mera AI Dost 🤖", page_icon="🤖")
st.title("Mera AI Dost 🤖")
st.write("Abu Bakar ka AI Dost - Sawal poocho jawab lo")

# API Key Setup (Auto-Detect)
# Ye code khud hi check karega ke key kahan majood hai
api_key = None

if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
else:
    # Agar secrets kaam na karein to aap ki di hui key backup ke tor par chalegi
    

# Gemini ko configure karein
if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("API Key nahi mili! Pehle key set karein.")

# Model setup
model = genai.GenerativeModel('gemini-1.5-flash')

# Chat History Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Purane messages screen par dikhane ke liye
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input aur Response generation
if prompt := st.chat_input("Kya poochna hai?"):
    
    # User ka message dikhao
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # AI ka jawab generate karo
    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            
            # History mein save karein
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            
        except Exception as e:
            st.error(f"Maazrat! API Key ka koi masla lag raha hai. Error: {e}")

# ============== CODE KHATAM ==============
