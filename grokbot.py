import requests
import json

API_KEY = "groq API here"
URL = "https://api.groq.com/openai/v1/chat/completions"

def chat():
    print("🤖 Welcome to GP AI (GROQ HTTP Version) 🤖")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye friend 😁")
            break

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }

        data = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {"role": "user", "content": user_input}
            ]
        }

        response = requests.post(URL, headers=headers, data=json.dumps(data))
        reply = response.json()["choices"][0]["message"]["content"]

        print("Chatbot:", reply, "\n")


if __name__ == "__main__":
    chat()
