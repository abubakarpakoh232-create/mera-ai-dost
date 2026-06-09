import streamlit as st
import google.generativeai as genai

# 1. Page Configuration (Sabse upar hona zaroori hai)
st.set_page_config(page_title="Mera AI Dost", page_icon="🤖", layout="centered")

# 2. Gemini API Key Configuration
try:
    # Secrets se key uthana
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    
    # Bilkul standard aur stable model call karna
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    st.error("API Key missing hai ya Streamlit Secrets mein sahi se nahi likhi gayi!")

# 3. Interface Headers
st.title("Mera AI Dost 🤖")
st.write("Abu Bakar ka AI Dost")

# 4. Chat History (Session State) Initialize karna
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. Purani chat history ko filter karke screen par dikhana
for message in st.session_state.messages:
    if message.get("content") and str(message["content"]).strip() != "None":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# 6. Chat Input aur Response Logic
if prompt := st.chat_input("Kya poochna hai?"):
    
    # User ka message screen par dikhana aur history mein save karna
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # AI ka response generate karna
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            # Model se reply generate karwana
            response = model.generate_content(prompt)
            
            # Agar response mil jaye toh use text mein convert karna
            if response and hasattr(response, 'text') and response.text.strip():
                ai_response = response.text.strip()
            else:
                ai_response = "Maaf kijiyega, main samajh nahi saka. Dubara koshish karein."
                
        except Exception as e:
            # Agar API block ho ya koi aur masla ho
            ai_response = f"Takneeki masla (Shayad API Key sahi kaam nahi kar rahi). Error: {str(e)}"
        
        # Jawab ko screen par dikhana
        message_placeholder.markdown(ai_response)
        
    # Jawab ko history mein save karna
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
