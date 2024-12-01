# Import necessary modules
import nltk
import re
from nltk.chat.util import Chat, reflections

# Download NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Define patterns and responses
pairs = [
    [r"my name is (.*)", ["Nice to meet you, %1! How can I help today?", "Hello %1! What can I do for you?"]],
    [r"hi|hey|hello", ["Hi there! How's it going?", "Hello! What brings you here today?", "Hey! Need some assistance?"]],
    [r"what is your name?", ["I'm your friendly chatbot, here to help!", "You can call me Chatbot."]],
    [r"how are you?", ["I'm just a program, but I'm feeling ready to assist you!", "I'm doing well. How can I help you today?"]],
    [r"can you help me with (.*)", ["Absolutely! What specifically about %1 do you need help with?", "Sure! I can assist with %1. Let me know what you’re stuck on."]],
    [r"sorry (.*)", ["No worries! How can I assist you?", "It's all good. Let's move forward!"]],
    [r"thank you|thanks", ["You're most welcome!", "Happy to help anytime!", "No problem at all!"]],
    [r"quit", ["It was nice chatting with you. Take care!", "Goodbye! Have a great day ahead!"]],
    [r"tell me a joke", ["Why don’t scientists trust atoms? Because they make up everything!", 
                         "Why was the math book sad? It had too many problems!"]],
    [r"i am feeling (.*)", ["Why are you feeling %1? Want to talk about it?", "Feeling %1 can be tough. Can I help?"]],
    [r"what can you do?", ["I can help with questions, suggest ideas, or even share a joke! Let me know what you need.", 
                           "I’m here to assist you with information, tips, or even just some friendly chat."]],
    [r"where are you from?", ["I live in the cloud—ready to help wherever you are!", 
                              "I’m a digital assistant created to make your life easier."]],
    [r"who created you?", ["I was created by the amazing developers at OpenAI.", 
                           "My creators at OpenAI built me to assist and interact with people like you."]],
    [r"i am bored", ["Let’s fix that! Want to hear a joke, learn something new, or get some recommendations?", 
                     "Boredom is the perfect time to try something new! Need ideas?"]],
    [r"can you recommend (.*)", ["Sure! For %1, I suggest exploring options like ...", 
                                 "Definitely! Based on %1, here are some ideas..."]],
    [r"how does (.*) work?", ["%1 works based on principles like ... Could you share more details?", 
                              "That’s a great question! %1 involves processes like ... Let me know if you’d like specifics."]],
    [r"tell me about (.*)", ["Here’s what I know about %1. Could you clarify further?", 
                             "%1 is fascinating! What aspect of it interests you?"]],
    [r"i need information about (.*)", ["Sure! %1 is an interesting topic. Could you specify what details you need?", 
                                        "I'd love to help with %1! Could you narrow it down a bit?"]],
    [r"do you know (.*)", ["I might! Tell me more about %1 and I’ll do my best to help.", 
                           "%1 sounds familiar. Could you provide some context?"]],
    [r"how can i (.*)", ["To %1, you can start by ... Want more details?", 
                         "You can %1 by following these steps: ... Need me to elaborate?"]],
    [r"what is love?", ["Love is a beautiful mix of emotions and actions. What’s your perspective?", 
                        "Many describe love as a deep affection. Do you have a specific question about it?"]],
    [r"what is the meaning of life?", ["The meaning of life can vary for everyone. Some say it's 42!", 
                                       "That’s the ultimate question! What does it mean to you?"]],
    [r"do you speak (.*)?", ["Yes, I can communicate in %1 to some extent. Want to try?", 
                             "I can handle %1. Feel free to test me!"]],
    [r"how do i (.*)", ["You can %1 by following some key steps. Let me guide you!", 
                        "To %1, consider doing the following: ... Need more info?"]],
    [r"why is (.*)", ["That’s a deep question! Let’s explore why %1 together.", 
                      "There could be many reasons why %1. What’s your take?"]],
    [r"do you have emotions?", ["I simulate emotions to make conversations engaging, but I don’t feel them.", 
                                "Not real ones, but I can mimic emotions to interact with you effectively."]],
    [r"(.*)", ["Interesting... Could you elaborate?", 
               "That’s something I’d like to understand better. Could you clarify?"]]
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
