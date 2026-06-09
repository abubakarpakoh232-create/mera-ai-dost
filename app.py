import streamlit as st
import google.generativeai as genai

# 1. Page Configuration (Sabse upar hona zaroori hai)
st.set_page_config(page_title="Mera AI Dost", page_icon="🤖")

# 2. Gemini API Key aur Model Setup
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    st.error("API Key ka masla hai! Please Streamlit Secrets check karein.")

# 3. App Headers
st.title("Mera AI Dost 🤖")
st.write("Abu Bakar ka AI Dost")

# 4. Chat History (Session State) Initialize karna
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. Purani chat history ko FILTER karke screen par dikhana (Taake 'None' kabhi nazar na aaye)
for message in st.session_state.messages:
    # Agar content khali hai ya usme "None" likha hai, toh usko screen par mat dikhao
    if message.get("content") and str(message["content"]).strip() != "None" and str(message["content"]).strip() != "":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# 6. User ka input handle karna
if prompt := st.chat_input("Kya poochna hai?"):
    
    # User ka message screen par dikhana aur history mein daalna
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Assistant ka reply generate aur display karna
    with st.chat_message("assistant"):
        message_placeholder = st.empty() # Loading state
        
        try:
            # Model se response lena
            response = model.generate_content(prompt)
            
            # Check karna ke response valid text hai
            if response and hasattr(response, 'text') and response.text.strip():
                ai_response = response.text.strip()
                message_placeholder.markdown(ai_response)
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
            else:
                error_msg = "Maaf kijiyega, main samajh nahi saka. Dobara likhein."
                message_placeholder.markdown(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})
                
        except Exception as e:
            error_msg = f"Takneeki masla hai. (Error: {str(e)})"
            message_placeholder.markdown(error_msg)
            st.session_state.messages.append({"role": "assistant", "content": error_msg})
