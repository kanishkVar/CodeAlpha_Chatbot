

def get_response(user_input):
    """Return a reply based on simple rules. Returns None when the user says bye."""
    text = user_input.strip().lower()

    if text in ("hello", "hi", "hey"):
        return "Hi!"
    elif text in ("how are you", "how are you?", "how r u"):
        return "I'm fine, thanks!"
    elif text in ("what is your name", "what's your name", "your name"):
        return "I'm CodeBot, a simple rule-based chatbot."
    elif text in ("what can you do", "help"):
        return "I can chat with you. Try: hello, how are you, what is your name, or bye."
    elif text in ("thanks", "thank you"):
        return "You're welcome!"
    elif text in ("bye", "goodbye", "exit", "quit"):
        return None
    elif text == "":
        return "Please type something."
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I can do."


def main():
    print("=== CodeBot: Basic Chatbot ===")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        reply = get_response(user_input)

        if reply is None:
            print("Bot: Goodbye!")
            break

        print("Bot:", reply)


if __name__ == "__main__":
    main()
