import random
from datetime import datetime
import re

user_name = None

def preprocess_input(user_input):
    user_input = user_input.lower()
    user_input = re.sub(r'[^\w\s]', '', user_input)
    return user_input

def get_greeting_response():
    greetings = [
        "Hello! How can I help you today?",
        "Hi there! What can I do for you?",
        "Hey! How are you? Need any help?",
        "Hello! I'm here to assist you. What do you need?"
    ]
    return random.choice(greetings)

def get_weather_response():
    weather_responses = [
        "It's sunny today!",
        "Looks like it might rain later.",
        "It's quite cloudy right now.",
        "The weather is perfect for a walk!",
        "It's a bit chilly outside, don't forget your jacket!",
        "Expect some thunderstorms later in the evening."
    ]
    return random.choice(weather_responses)

def get_time_response():
    now = datetime.now()
    return f"The curent time is {now.strftime('%H:%M:%S')}."

def get_default_response():
    default_responses = [
        "I'm not sure I understand. Could you please rephrase?",
        "Sorry, I don't have an answer for that.",
        "Can you tell me more?",
        "I'm here to help, but I'm not sure about that.",
        "That's interesting! Tell me more."
    ]
    return random.choice(default_responses)

def ask_for_name():
    return "I don’t think we’ve met. What’s your name?"

def respond_with_name():
    global user_name
    return f"Nice to meet you, {user_name}!"

def respond_to_small_talk():
    small_talk_responses = [
        "I'm just a bunch of code, but I'm feeling graet!",
        "I'm always here to chat with you!",
        "Chatting with you makes my dae!",
        "I'm here to make your day better!"
    ]
    return random.choice(small_talk_responses)

def chatbot():
    global user_name
    print("Hello! I am a simple chatbot. How can I help you today?")
    print("Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        processed_input = preprocess_input(user_input)
        
        if processed_input == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        if any(greet in processed_input for greet in ['hello', 'hi', 'hey']):
            if user_name:
                print(f"Chatbot: {get_greeting_response()} {user_name}!")
            else:
                print(f"Chatbot: {get_greeting_response()}")
        
        elif "weather" in processed_input:
            print(f"Chatbot: {get_weather_response()}")
        
        elif "time" in processed_input:
            print(f"Chatbot: {get_time_response()}")
        
        elif "name" in processed_input:
            if user_name:
                print(f"Chatbot: Your name is {user_name}, right?")
            else:
                print("Chatbot: I am your friendly chatbot. What's your name?")
                user_name = input("You: ")
                print(f"Chatbot: {respond_with_name()}")
        
        elif "help" in processed_input:
            print("Chatbot: I can tell you about the weather, time, or just chat with you. What would you like to know?")
        
        elif "thanks" in processed_input or "thank you" in processed_input:
            print("Chatbot: You're welcome! I'm here to help.")
        
        elif any(small_talk in processed_input for small_talk in ['how are you', 'what\'s up', 'how\'s it going']):
            print(f"Chatbot: {respond_to_small_talk()}")
        
        elif "joke" in processed_input:
            jokes = [
                "Why don’t scientists trust atoms? Because they make up everything!",
                "Why did the math book look sad? Because it had too many problems.",
                "What do you call fake spaghetti? An impasta!"
            ]
            print(f"Chatbot: {random.choice(jokes)}")
        
        else:
            print(f"Chatbot: {get_default_response()}")

chatbot()
