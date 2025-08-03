
def chatbot_response(user_input):
    responses = {
        "hi": "Hello!",
        "how are you": "I'm just a bot, but I'm good.",
        "bye": "Goodbye!",
        "what is your name": "I'm a chatbot written in Python.",
    }
    return responses.get(user_input.lower(), "I don't understand that.")

def main():
    print("💬 Simple Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Bye!")
            break
        response = chatbot_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()