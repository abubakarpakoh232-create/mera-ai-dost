import streamlit as st
import google.generativeai as genai

# 1. Page Title aur Icon set karna (Sabse pehli line honi chahiye)
st.set_page_config(page_title="Mera AI Dost", page_icon="🤖")

# 2. Gemini API Key Configuration
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    st.error("API Key ka masla hai! Please Streamlit Secrets check karein.")

# 3. App ka Main Interface
st.title("Mera AI Dost 🤖")
st.write("Abu Bakar ka AI Dost")

# 4. Chat History (Session State) Setup
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. Purani Chat History ko Screen par Dikhana (None ke check ke sath)
for message in st.session_state.messages:
    if message.get("content") and str(message["content"]).strip() != "None":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# 6. User Input aur AI Response Logic
if prompt := st.chat_input("Kya poochna hai?"):
    
    # User ka message screen par dikhana aur history mein save karna
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # AI (Assistant) ka response generate karna
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            # Model se reply mangna
            response = model.generate_content(prompt)
            
            # Sahi tareeqe se text check aur extract karna
            if response and response.text:
                ai_response = response.text.strip()
            else:
                ai_response = "Maaf kijiyega, main is baat ka jawab nahi dhoond saka."
                
        except Exception as e:
            ai_response = f"Takneeki masla aa gaya hai. Error: {str(e)}"
        
        # AI ka jawab screen par render karna
        message_placeholder.markdown(ai_response)
        
    # AI ka jawab history mein save karna
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
