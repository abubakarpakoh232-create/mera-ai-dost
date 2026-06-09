# ===============================================
# Abu Bakar ka AI Dost - Streamlit + Gemini AI
# Version: 1.0 - 50 Line Version
# ===============================================

# Step 1: Zaruri libraries import karo
import streamlit as st
import google.generativeai as genai

# Step 2: Page ka Title aur Description set karo
st.title("Mera AI Dost 🤖")
st.write("Abu Bakar ka AI Dost - Sawal poocho jawab lo")

# Step 3: Gemini API ko configure karo
# API Key Streamlit Cloud ke Secrets se aayegi
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Step 4: Gemini ka Model select karo
# gemini-1.5-flash sabse tez aur free hai
model = genai.GenerativeModel('gemini-1.5-flash')

# Step 5: Chat ki History save karne ke liye
# Session state banate hain taake page reload pe chat na urde
if "messages" not in st.session_state:
    st.session_state.messages = []

# Step 6: Purane saare messages screen pe dikhao
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Step 7: User se naya input lo
if prompt := st.chat_input("Kya poochna hai?"):
   
    # User ka message chat me dikhao
    with st.chat_message("user"):
        st.markdown(prompt)
   
    # AI ka jawab generate karo aur dikhao
    with st.chat_message("assistant"):
        response = model.generate_content(prompt)
        st.markdown(response.text)
   
    # User ka message history me save karo
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })
   
    # AI ka message history me save karo
    st.session_state.messages.append({
        "role": "assistant",
        "content": response.text
    })

# ============== CODE KHATAM ==============
# Ab app deploy kar do Streamlit pe
