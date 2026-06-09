import streamlit as st
import google.generativeai as genai

# 1. API Key aur Model Setup
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Model ko system instruction ke sath setup kar rahe hain taake response short aur sahi aaye
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="Aap ek madadgaar AI dost hain jiska naam 'Mera AI Dost' hai."
)

# 2. App ka Title aur Header
st.title("Mera AI Dost 🤖")
st.write("Abu Bakar ka AI Dost")

# 3. Chat History (Session State) Initialize karna
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Purani chat history ko screen par dikhana (Agar usme 'None' na ho)
for message in st.session_state.messages:
    if message["content"] is not None and message["content"] != "None":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# 5. User ka input handle karna
if prompt := st.chat_input("Kya poochna hai?"):
    
    # User ka message screen par dikhana aur save karna
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        # Gemini Model ko call karke response lena
        response = model.generate_content(prompt) 
        
        # Sahi tarike se text extract karna aur check karna
        if response and hasattr(response, 'text') and response.text:
            ai_response = response.text
        else:
            ai_response = "Maaf kijiyega, main is waqt jawab nahi de saka. Dobara koshish karein."
            
    except Exception as e:
        ai_response = f"API Call mein error aaya hai: {str(e)}"
    
    # AI ka jawab screen par dikhana
    with st.chat_message("assistant"):
        st.markdown(ai_response)
    
    # AI ka jawab history mein save karna (Ab 'None' kabhi nahi aayega)
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
