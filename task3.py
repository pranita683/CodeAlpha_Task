import nltk
from nltk.chat.util import Chat, reflections

# Define the chatbot's pattern-response pairs
pairs = [
    (r'Hi|Hello|Hey', ['Hello! How can I help you today?', 'Hi there! What can I do for you?']),
    (r'What is your name?', ['I am a chatbot created using NLTK.']),
    (r'How are you?', ['I am doing great, thanks for asking! How about you?']),
    (r'(.*) your name (.*)', ['My name is Chatbot.']),
    (r'(.*) help (.*)', ['I am here to help! What do you need assistance with?']),
    (r'Quit', ['Goodbye! Have a great day!']),
]

# Initialize the chatbot
def chatbot():
    print("Chatbot: Hello! Type 'Quit' to exit.")
    
    # Create a chatbot object
    chat = Chat(pairs, reflections)
    
    # Start the conversation
    while True:
        user_input = input("You: ")
        
        # Get the chatbot's response
        response = chat.respond(user_input)
        
        # If there's no response, ask again
        if not response:
            print("Chatbot: I'm not sure how to respond to that.")
        else:
            print(f"Chatbot: {response}")
        
        # Exit the loop if user types 'Quit'
        if user_input.lower() == 'quit':
            break

# Run the chatbot
if __name__ == "__main__":
    chatbot()
