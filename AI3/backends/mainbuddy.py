import random
import json
import torch
from Brain.Brain import NeuralNet
from Brain.Nerves import bag_of_words, tokenize
from Features.Task import NonInputExecution , InputExecution
# from Features.test2 import InputExecution1
import tkinter as tk
from tkinter.font import Font
from PIL import Image, ImageTk, ImageDraw
from tkinter import PhotoImage
import time
import threading
import queue


# Create the main window
root = tk.Tk()

# Remove window decorations
root.overrideredirect(True)

# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size to occupy the full screen
root.geometry(f"{screen_width}x{screen_height}")

# Set the background color to black
# root.configure(bg="#000000")
# Load your background image
file_path = "Database\\background.png"
background_image = tk.PhotoImage(file=file_path)

# Create a canvas to draw the circles and concentric borders
canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg="#000000", highlightthickness=0)
canvas.pack()

# Display the background image
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

# Calculate the scaling factor based on the original coordinates
original_width = 350 - 50
original_height = 350 - 50
desired_width = 315 - 85
desired_height = 315 - 85

width_scale = desired_width / original_width
height_scale = desired_height / original_height

# Calculate the coordinates to center the circles
center_x = screen_width // 2
center_y = screen_height // 2

big_circle_radius = (original_width / 2)
small_circle_radius = (desired_width / 2)

# Define the shades for big and small circles
shade_colors_big = ["#20ab49", "#22b14c", "#23b84f", "#24bf52", "#26c655"]
shade_colors_small = ["#09f36b", "#36f787", "#65f9a3", "#94fabf", "#c4fcdb"]

# Function to create concentric borders
def create_concentric_borders(x, y, inner_radius, outer_radius, outline_colors, border_width):
    for i, color in enumerate(outline_colors):
        canvas.create_oval(
            x - outer_radius - i * border_width,
            y - outer_radius - i * border_width,
            x + outer_radius + i * border_width,
            y + outer_radius + i * border_width,
            outline=color,
            width=border_width
        )
        canvas.create_oval(
            x - inner_radius + i * border_width,
            y - inner_radius + i * border_width,
            x + inner_radius - i * border_width,
            y + inner_radius - i * border_width,
            outline=color,
            width=border_width
        )

# Create concentric borders for the big circle
create_concentric_borders(center_x, center_y, big_circle_radius - 1, big_circle_radius, shade_colors_big, 1)

# Create concentric borders for the small circle
create_concentric_borders(center_x, center_y, small_circle_radius - 1, small_circle_radius, shade_colors_small, 2)

# Initialize animation variables
animation_running = False
animation_direction = 1
animation_speed = 2

# Create empty lists to store the shaded circle objects
shaded_big_circles = []
shaded_small_circles = []

# Define animation function
def animate_circles():
    global big_circle_radius, small_circle_radius, animation_direction, animation_speed

    if animation_running:
        big_circle_radius += animation_direction * animation_speed
        small_circle_radius -= animation_direction * animation_speed

        # Check if the animation should reverse
        if big_circle_radius >= (original_width / 2):
            animation_direction = -1
        elif big_circle_radius <= (desired_width / 2):
            animation_direction = 1

        # Update the circle sizes
        canvas.coords(big_circle, center_x - big_circle_radius, center_y - big_circle_radius,
                      center_x + big_circle_radius, center_y + big_circle_radius)
        canvas.coords(small_circle, center_x - small_circle_radius, center_y - small_circle_radius,
                      center_x + small_circle_radius, center_y + small_circle_radius)

        # Update the shaded circle sizes and positions
        for i, shaded_big_circle in enumerate(shaded_big_circles):
            canvas.coords(shaded_big_circle, center_x - big_circle_radius - i * 15,
                          center_y - big_circle_radius - i * 15,
                          center_x + big_circle_radius + i * 15,
                          center_y + big_circle_radius + i * 15)
        for i, shaded_small_circle in enumerate(shaded_small_circles):
            canvas.coords(shaded_small_circle, center_x - small_circle_radius - i * 15,
                          center_y - small_circle_radius - i * 15,
                          center_x + small_circle_radius + i * 15,
                          center_y + small_circle_radius + i * 15)

        # Schedule the next animation frame
        root.after(10, animate_circles)

# Create bigger circle with neon-like color
big_circle = canvas.create_oval(
    center_x - big_circle_radius,
    center_y - big_circle_radius,
    center_x + big_circle_radius,
    center_y + big_circle_radius,
    outline="#22B14C",
    width=10,
    fill=""
)

# Create smaller circle with neon-like color
small_circle = canvas.create_oval(
    center_x - small_circle_radius,
    center_y - small_circle_radius,
    center_x + small_circle_radius,
    center_y + small_circle_radius,
    outline="#7DFAB1",
    width=10,
    fill=""
)

# Create shaded big circles
for _ in range(5):
    shaded_big_circle = canvas.create_oval(0, 0, 0, 0, outline="#20ab49", width=10, fill="#000000")
    shaded_big_circles.append(shaded_big_circle)

# Create shaded small circles
for _ in range(5):
    shaded_small_circle = canvas.create_oval(0, 0, 0, 0, outline="#09f36b", width=10, fill="#000000")
    shaded_small_circles.append(shaded_small_circle)

# Write "BUDDY" in the center with Orbitron font
font_color = "#FFFFFF"
font_size = 30
font_id = canvas.create_text(center_x, center_y, text="BUDDY", font=("Orbitron", font_size), fill=font_color)

# Function to start and stop the animation
def toggle_animation():
    global animation_running
    if not animation_running:
        animation_running = True
        animate_circles()
        canvas.itemconfig(font_id, fill="#8ed8f4")  # Change font color to #8ed8f4 when animation starts
        
        # Hide the shaded circles when animation starts
        for shaded_big_circle in shaded_big_circles:
            canvas.itemconfig(shaded_big_circle, state=tk.HIDDEN)
        for shaded_small_circle in shaded_small_circles:
            canvas.itemconfig(shaded_small_circle, state=tk.HIDDEN)
    else:
        animation_running = False
        canvas.itemconfig(font_id, fill=font_color)  # Change font color back to white when animation stops
        
        # Show the shaded circles when animation stops
        for shaded_big_circle in shaded_big_circles:
            canvas.itemconfig(shaded_big_circle, state=tk.NORMAL)
        for shaded_small_circle in shaded_small_circles:
            canvas.itemconfig(shaded_small_circle, state=tk.NORMAL)

# Create a queue for communication between threads
gui_queue = queue.Queue()

# def bind_toggle_animation():
#     # Bind the animation toggle function to a keypress event (e.g., spacebar)
#     root.bind("<space>", lambda event: toggle_animation())

def start_gui():
    # Main loop to display the GUI
    root.mainloop()

def gui_thread_func():
    # Start the GUI in a separate thread
    start_gui()


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
    if "pause" in query_str.lower():
        Speak("Okay sir, I'm pausing for a moment.")
        pause_flag = True
        while pause_flag:
            sentence = Connect()
            if "wake up" in sentence.lower():
                # Speak("I'm awake now!")
                pause_flag = False
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
                    else:
                        Speak(reply)

        # After handling the task, speak a default response if a task was executed
        if task_executed:
            Speak(random.choice(default_responses))
        
        
        




# Buddy functionality
def buddy_thread_func():
    from Features.Task import WishMe
    # Start the Buddy functionality here
    global animation_running
    # Start the animation
    toggle_animation()
    WishMe()
    while True:
        Main()

# Bind the toggle_animation function in the main thread
root.after(100, start_gui) 

# Start the Buddy functionality in another thread
buddy_thread = threading.Thread(target=buddy_thread_func)
buddy_thread.start()

# Start the GUI in the main thread
root.mainloop()