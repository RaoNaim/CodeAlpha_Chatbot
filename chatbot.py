import datetime
import random

print("Hello! I am CodeAlpha Chatbot.")
print("Ask me anything. Type 'exit' to stop.\n")

fallback_responses = [
    "That's interesting. Tell me more!",
    "I see. What else would you like to know?",
    "Nice question. Can you explain a bit more?",
    "Let's talk about something interesting.",
    "I like chatting with you. Ask me another question!",
    "Hmm, that's a good thought.",
    "Can you ask that in another way?",
    "I'm learning new things every day!",
]

while True:
    user = input("You: ").lower()

    if "hello" in user or "hi" in user or "hey" in user:
        print("Bot: Hello! How can I help you today?")

    elif "how are you" in user:
        print("Bot: I'm doing great and ready to chat!")

    elif "your name" in user:
        print("Bot: I am CodeAlpha Chatbot.")

    elif "who created you" in user:
        print("Bot: I was created for a Cloud Computing internship project.")

    elif "time" in user:
        print("Bot: Current time is", datetime.datetime.now().strftime("%H:%M:%S"))

    elif "date" in user:
        print("Bot: Today's date is", datetime.date.today())

    elif "joke" in user:
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs!")

    elif "weather" in user:
        print("Bot: I cannot check live weather yet, but I hope it's a nice day where you are!")

    elif "study" in user or "learn" in user:
        print("Bot: Learning something new every day is the best way to grow.")

    elif "technology" in user or "ai" in user:
        print("Bot: AI and cloud computing are transforming the world.")

    elif "exit" in user or "bye" in user:
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot:", random.choice(fallback_responses))