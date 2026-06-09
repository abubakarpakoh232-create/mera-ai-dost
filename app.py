import os
from google import genai

# API key environment variable se
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY set nahi hai")
    exit()

client = genai.Client(api_key=api_key)

print("🤖 Gemini Chat Ready (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bye 👋")
        break

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input
        )

        print("AI:", response.text)

    except Exception as e:
        print("Error:", e)
