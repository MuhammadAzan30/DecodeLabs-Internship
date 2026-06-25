print("Welcome to DecodeBot!")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I am fine. Thanks for asking!")

    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user == "your name":
        print("Bot: My name is DecodeBot.")

    elif user == "help":
        print("Bot: Try saying hello, asking about AI, or type bye to exit.")

    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
