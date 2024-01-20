import random
import json
import torch
from Brain.Brain import NeuralNet
from Brain.Nerves import bag_of_words, tokenize
from Features.Task import NonInputExecution , InputExecution
# from Features.test2 import InputExecution1
import threading
from gui import *
import signal

stop_flag = False
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open('Brain/intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "Brain/data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)  
model.eval()    

bot_name = "Buddy"

from Body.Listen import Connect 
from Body.Speak import Speak
# Default responses
default_responses = [
    "Do you have some work for me?",
    "How can I assist you today?",
    "Is there anything else I can help you with?",
    "I'm here to help. What do you need?",
    "What can I do for you now?"
]
# Create a flag to control the pause state
pause_flag = False
# Function to handle the pause command
def handle_pause(query):
    global pause_flag
    query_str = ' '.join(query)  # Join the list of words into a single string
    if "stop" in query_str.lower() or "minute" in query_str.lower() :
        Speak("Okay sir, I'm pausing for a moment.")
        toggle_animation()
        pause_flag = True
        while pause_flag:
            sentence = Connect()
            if "wake up" in sentence.lower():
                # Speak("I'm awake now!")
                pause_flag = False
                toggle_animation()  
        Speak("I'm back sir!")



def Main():
    global animation_running
    #listening by using sentence variable
    toggle_animation()
    sentence = Connect()
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        # Flag to determine if the task was executed
        toggle_animation()
        task_executed = False
        # Handle "myself" intent separately
        if tag == "myself":
            intent = [intent for intent in intents["intents"] if intent["tag"] == tag][0]
            reply = random.choice(intent['responses'])
            Speak(reply)
            task_executed = True

        # Handle other intents
        else:
            for intent in intents["intents"]:
                if tag == "shutdown":
                    print(intents["intents"][0]['responses'])
                    reply = (random.choice(intents["intents"][0]['responses']))
                    Speak(reply)
                    stop_flag = True  # Signal the buddy_thread to stop
                    end_gui()  # Close the GUI
                    exit()
                    

                    
                if tag == intent["tag"]:
                    reply = (random.choice(intent['responses']))
                    print(f"tag : {tag}")
                    if "time" in reply:
                        NonInputExecution(reply)
                        task_executed = True
                    elif "date" in reply:
                        NonInputExecution(reply)
                        task_executed = True
                    elif "day" in reply:
                        NonInputExecution(reply)
                        task_executed = True
                    elif "wishme" in reply:
                        NonInputExecution(reply)
                        task_executed = True
                    elif "notepad" in reply and "udtxt" not in sentence:  # Check for exact match:
                        NonInputExecution(reply)
                        task_executed = True
                    elif "udtxt" in reply:  # Only check for "updatetxt" tag, no need to check "notepad" here
                        NonInputExecution(reply)
                        task_executed = True
                    elif "clnp" in reply:
                        NonInputExecution(reply)
                        task_executed = True
                    elif "closechrome" in reply:
                        NonInputExecution(reply)
                        task_executed = True
                    elif "minimizechrome" in reply:
                        NonInputExecution(reply)
                        task_executed = True
                    elif "screenshot" in reply and "closess" not in sentence:
                        NonInputExecution(reply)
                        task_executed = True
                    elif "closess" in reply:
                        NonInputExecution(reply)
                        task_executed = True
                    elif "picture" in reply:
                        NonInputExecution(reply)
                        task_executed = True
                    elif "weather" in reply:
                        NonInputExecution(reply)
                        task_executed = True
                    elif "microsoftppt" in reply:
                        NonInputExecution(reply)
                        task_executed = True
                    elif "closemipp" in reply:
                        NonInputExecution(reply)
                        task_executed = True
                    # elif "break" in reply:
                    #     NonInputExecution(reply)
                    #     task_executed = True
                    elif "wikipedia" in reply:
                        InputExecution(tag, sentence)
                        task_executed = True
                    elif "wikipedia2" in reply:
                        InputExecution(tag, sentence)
                        task_executed = True
                    elif "google" in reply:
                        InputExecution(tag, sentence)
                        task_executed = True
                    elif "summary" in reply:
                        InputExecution(tag, sentence)
                        task_executed = True
                    elif "calculator" in reply:
                        InputExecution(tag, sentence)
                        task_executed = True
                    elif "break" in reply:
                        handle_pause(sentence)
                        task_executed = True
                    elif "whatsapp" in reply:
                        InputExecution(tag, sentence)
                        task_executed = True
                    elif "Identity2" in reply:
                        InputExecution(tag, sentence)
                        task_executed = True
                    elif "youtube" in reply:
                        InputExecution(tag, sentence)
                        task_executed = True
                    elif "scroll" in reply:
                        InputExecution(tag, sentence)
                        task_executed = True
                    elif "dictionary" in reply:
                        InputExecution(tag, sentence)
                        task_executed = True
                    else:
                        Speak(reply)

        # After handling the task, speak a default response if a task was executed
        if task_executed:
            Speak(random.choice(default_responses))
    else:
        toggle_animation()
        Speak("sorry sir, I didn't get that.")   
        
def handle_termination_signal(signum, frame):
    # Stop the buddy_thread
    buddy_thread.stop()  # You should define a method to stop your buddy_thread gracefully
    
    # End the GUI
    end_gui()

    # Exit the program
    exit()

# Register the signal handler for the termination signal (Ctrl+C)
signal.signal(signal.SIGINT, handle_termination_signal)

# Buddy functionality
def buddy_thread_func():
    from Features.Task import WishMe
    # Start the Buddy functionality here
    global animation_running, stop_flag
    # Start the animation
    toggle_animation()
    WishMe()
    while not stop_flag:  # Check the flag to see if the thread should stop:
        Main()

# Bind the toggle_animation function in the main thread
root.after(100, start_gui) 

# Start the Buddy functionality in another thread
buddy_thread = threading.Thread(target=buddy_thread_func, daemon=True)
buddy_thread.start()

# Start the GUI in the main thread
root.mainloop()