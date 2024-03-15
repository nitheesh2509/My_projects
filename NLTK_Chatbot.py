import random
import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is ChatBot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm good, thanks for asking.",]
    ],
    [
        r"sorry (.*)",
        ["It's alright, no problem.", "No worries.",]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye, have a great day!"]
    ],
    [
        r"(.*)",
        ["Sorry, I didn't understand that. Can you please rephrase?",]
    ]
]

chatbot = Chat(pairs, reflections)

def chat_with_bot():
    print("Hello! I'm a chatbot. How can I assist you today?")
    print("Type 'quit' to exit.")

    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Bot:", response)

        if user_input.lower() == 'quit':
            break

if __name__ == "__main__":
    chat_with_bot()
