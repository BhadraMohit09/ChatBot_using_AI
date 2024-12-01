# Import necessary modules
import nltk
import re
from nltk.chat.util import Chat, reflections

# Download NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Define patterns and responses
pairs = [
    [r"my name is (.*)", ["Hello %1, how can I assist you today?",]],
    [r"hi|hey|hello", ["Hello, how can I help you?", "Hey there! What can I do for you?", "Hi! How can I assist you today?"]],
    [r"what is your name?", ["I am a chatbot created to assist you. You can call me Chatbot.",]],
    [r"how are you?", ["I'm a bot, so I don't have feelings, but I'm here to help you!",]],
    [r"can you help me with (.*)", ["Sure, I can help you with %1. Please provide more details.",]],
    [r"sorry (.*)", ["It's okay. How can I assist you?",]],
    [r"thank you|thanks", ["You're welcome!", "No problem!", "Happy to help!"]],
    [r"quit", ["Bye! Have a great day!", "Goodbye!"]],
    [r"(.*)", ["I'm sorry, I don't understand that. Can you rephrase?", "Could you please elaborate on that?"]],
    [r"what can you do?", ["I can assist you with a variety of tasks, such as answering questions, providing information, and helping with tasks. Just let me know!",]],
    [r"where are you from?", ["I'm from the digital world, created to assist you whenever needed!",]],
    [r"tell me a joke", ["Why don't skeletons fight each other? Because they don't have the guts!", "What do you call cheese that isn't yours? Nacho cheese!"]],
    [r"how does (.*) work?", ["%1 works through a complex set of rules and processes. Can you tell me more about what you want to understand?",]],
    [r"help me with (.*)", ["Sure, let me assist you with %1. What specifically would you like to know?",]],
    [r"i need information about (.*)", ["I can provide details about %1. Could you please be more specific about what you're looking for?",]],
    [r"what is (.*)", ["%1 is something that varies in definition depending on the context. Could you provide more details?",]],
    [r"do you know (.*)", ["I have some knowledge about %1. Please tell me what you'd like to know!",]],
    [r"who is (.*)", ["%1 might refer to a person or character. Could you clarify so I can provide accurate information?",]],
    [r"tell me about (.*)", ["Here's what I know about %1. Could you specify if you need more details?",]],
    [r"how can i (.*)", ["You can %1 by following these steps. Let me know if you'd like detailed instructions.",]],
    [r"i am feeling (.*)", ["Why are you feeling %1? I'm here to help if you want to share more.",]],
    [r"what is the time?", ["I'm not aware of the exact time, but you can check your device's clock!",]],
    [r"can you suggest (.*)", ["I can suggest %1 based on your preferences. Could you provide more context?",]],
    [r"do you have emotions?", ["No, I'm a chatbot. I simulate responses to help you!",]],
    [r"who created you?", ["I was created by developers at OpenAI to assist and interact with users like you.",]],
    [r"i am bored", ["How about learning something new or doing a fun activity? I can give you ideas!", "Boredom is a chance for creativity! Want some recommendations?",]],
    [r"can you recommend (.*)", ["I can recommend %1 based on your needs. Can you provide more details?",]],
    [r"how old are you?", ["I don't age! I'm here for you no matter the time.",]],
    [r"what is love?", ["Love is a complex mix of emotions, actions, and expressions. What aspect are you curious about?",]],
    [r"why is (.*)", ["There could be several reasons why %1. Could you explain more?",]],
    [r"do you speak (.*)?", ["I can understand and communicate in many languages, including %1. Feel free to test me!",]],
    [r"how do i (.*)", ["You can %1 by following these steps. Let me know if you'd like detailed guidance.",]],
    [r"what is your purpose?", ["My purpose is to assist, provide information, and make your experience enjoyable.",]],
    [r"what is the meaning of life?", ["The meaning of life can vary for everyone. Some say it's 42! What do you think?",]],
    [r"why do you (.*)", ["I %1 to help and provide accurate responses. Is there something you'd like to clarify?",]]
]


# Define the chatbot class
class RuleBasedChatbot:
    def __init__(self, pairs):
        self.chat = Chat(pairs, reflections)
        
    def respond(self, user_input):
        return self.chat.respond(user_input)

# Initialize the chatbot
chatbot = RuleBasedChatbot(pairs)

# Function to chat with the bot
def chat_with_bot():
    print("Hi, I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.title() == 'quit':
            print("Chatbot: Bye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

# Start chatting with the bot
chat_with_bot()