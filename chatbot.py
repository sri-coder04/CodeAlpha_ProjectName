import random
import time

# Replies
greetings = [
    "Hello! I'm here for you.",
    "Hi! Tell me how you feel.",
    "Hey! Hope you're doing well."
]

happy_reply = [
    "That's wonderful to hear!",
    "Keep smiling and shining!",
    "Happiness looks good on you."
]

sad_reply = [
    "I'm sorry you feel sad.",
    "Tough times never last forever.",
    "Everything will become better slowly."
]

stress_reply = [
    "Take a small break and relax.",
    "You are stronger than your stress.",
    "Don't forget to take care of yourself."
]

angry_reply = [
    "Try taking deep breaths.",
    "It's okay to feel angry sometimes.",
    "Stay calm. Things will improve."
]

lonely_reply = [
    "You are never completely alone.",
    "Talk with someone you trust.",
    "I am here to chat with you."
]

motivation_reply = [
    "Believe in yourself!",
    "You can achieve great things.",
    "Never give up on your dreams."
]

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the computer cold? Because it left its Windows open!"
]

# Chatbot Function
def chatbot(user_input):

    text = user_input.lower()

    # Greeting
    if "hi" in text or "hello" in text or "hey" in text:
        return random.choice(greetings)

    # Sad feeling
    elif "sad" in text or "cry" in text or "upset" in text:
        return random.choice(sad_reply)

    # Stress feeling
    elif "stress" in text or "tired" in text or "pressure" in text:
        return random.choice(stress_reply)

    # Angry feeling
    elif "angry" in text or "mad" in text:
        return random.choice(angry_reply)

    # Lonely feeling
    elif "alone" in text or "lonely" in text:
        return random.choice(lonely_reply)

    # Happy feeling
    elif "happy" in text or "excited" in text:
        return random.choice(happy_reply)

    # Motivation
    elif "motivate" in text or "motivation" in text:
        return random.choice(motivation_reply)

    # Joke
    elif "joke" in text:
        return random.choice(jokes)

    # Time
    elif "time" in text:
        current_time = time.strftime("%I:%M %p")
        return "Current time is " + current_time

    # Date
    elif "date" in text:
        current_date = time.strftime("%d-%m-%Y")
        return "Today's date is " + current_date

    # Name
    elif "your name" in text:
        return "My name is Alpha Emotional Bot."

    # Help
    elif "help" in text:
        return (
            "You can share your feelings like happy, sad, stress, "
            "lonely, angry or ask for jokes, time and motivation."
        )

    # Exit
    elif "bye" in text or "exit" in text:
        return "Goodbye! Stay positive and take care."

    # Default
    else:
        return (
            "I may not fully understand, but I'm always here to listen."
        )


# Main Program
print("======================================")
print("      ALPHA EMOTIONAL CHATBOT")
print("======================================")
print("You can share your feelings with me.")
print("Type 'bye' to exit.\n")

while True:

    user_message = input("You : ")

    response = chatbot(user_message)

    print("Bot :", response)

    # Exit condition
    if "bye" in user_message.lower() or "exit" in user_message.lower():
        break

print("\nChat ended successfully.")
print("======================================")
