import random
from datetime import datetime
def responses(userinput):
    userinput = userinput.lower()

    greetings = ["hello", "hey", "hi"]
    farewells = ["bye", "goodbye","see u later","have a nice day","talk to u later"]
    thanks = ["thanks!", "thank you!","thanks","thank you"]
    
    if any(word in userinput for word in greetings):
        return random.choice(["Hey there!","Hi! How can I help u today?","Hello! Nice to meet u"])
    
    elif any(phrase in userinput for phrase in ["how are u?", "how are u", "how are you"]):
        return random.choice(["I'm doing great! Thanks for asking","All good here! How about u?","Running smoothly as always "])
    
    elif any(phrase in userinput for phrase in ["who are u", "who are you"]):
        return "Hi,im a rule-based chatbot created for codsoft project."
    
    elif "what is today's date?" in userinput:
        today = datetime.now().strftime("%d %B %Y")
        return f"Today's date is {today}."

    elif "what is the current time?" in userinput:
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."

    elif any(op in userinput for op in ["+", "-", "*", "/"]):
        try:
            result = eval(userinput)
            return f"The answer is {result}."
        except:
            return "i could not understand the question.."

    elif any(word in userinput for word in thanks):
        return random.choice([
            "You're welcome!",
            "Anytime! Happy to help.",
            "Glad I could help."
        ])
    
    elif any(word in userinput for word in farewells):
        return "Goodbye! Have a great day!"
    
    else:
        return random.choice([
            "sorry, I didnt quite get that.",
            "im unable to answer that as my prompts are only limited to my predefined rules",
            "I'm still learning. Try something else from the prompts!"
        ])

def run_chatbot():
    print("Hi! im a rule-based chatbot. I will try my best to answer your questions from the predefined prompts i've been given.")
    print("You can try:")
    print("Greeting me by saying hi,hello or hey")
    print("Asking how i am")
    print("Asking who i am")
    print("What todays date is")
    print("What the time is currently")
    print("bidding me farewell")
    print("saying 'bye' to exit\n")
    
    while True:
        userinput = input("You: ")
        response = responses(userinput)
        print("Chatbot: ", response)
        
        if userinput.lower() in ["bye", "goodbye","see u later","have a nice day","talk to u later"]:
            break
run_chatbot()