import random

# Define responses for the chatbot
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thank you!", "I'm good, thanks for asking.", "I'm great!"],
    "what's your name": ["I'm just a humble chatbot.", "I don't have a name, but you can call me Chatbot."],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "default": ["I'm not sure how to respond to that.", "Could you please rephrase that?", "I don't understand."],
}

# Function to handle user input and generate response
def respond(input_text):
    input_text = input_text.lower()
    for key in responses:
        if key in input_text:
            return random.choice(responses[key])
    return random.choice(responses["default"])

# Main function to run the chatbot
def main():
    print("Welcome to the Basic Chatbot!")
    print("Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(respond(user_input))
            break
        else:
            print("Chatbot:", respond(user_input))

if __name__ == "__main__":
    main()
