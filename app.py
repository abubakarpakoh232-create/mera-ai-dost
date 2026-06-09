import streamlit as st
import google.generativeai as genai

# 1. API Key aur Model Setup
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

# 2. App ka Title
st.title("Mera AI Dost 🤖")
st.write("Abu Bakar ka AI Dost")

# 3. Chat History (Session State) Initialize karna
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Purani chat history ko screen par dikhana
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. User ka input handle karna (Poore code mein sirf EK BAAR)
if prompt := st.chat_input("Kya poochna hai?"):
    
    # User ka message screen par dikhana aur save karna
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Gemini Model ko call karke response lena
    response = model.generate_content(prompt) 

    # AI ka jawab screen par dikhana
    with st.chat_message("assistant"):
        st.markdown(response.text)
    
    # AI ka jawab history mein save karna
    st.session_state.messages.append({"role": "assistant", "content": response.text})
