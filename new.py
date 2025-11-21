import google.generativeai as genai


genai.configure(api_key="AIzaSyCoYHOaso3igQUuB-IgIvWA4dOSXmUa4JE")


model = genai.GenerativeModel("gemini-2.0-flash")

def chat():
    print("🤖 Welcome to GP Ai 🤖")
    
    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye friend 😁")
            break

       
        response = model.generate_content(user_input)
        print("Chatbot:", response.text, "\n")

if __name__ == "__main__":
    chat()
