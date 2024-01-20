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
# root.overrideredirect(True)

root.title("Buddy")
root.config(bg="#000000")



# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size to occupy the full screen
root.geometry(f"{screen_width}x{screen_height}")

# Set the background color to black
# root.configure(bg="#000000")
# Load your background image
file_path = "Database\\GUIimages\\test.png"
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
shade_colors_big = ["#00FEFC", "#000000", "#00FEFC", "#000000", "#00FEFC"]
shade_colors_small = ["#00FEFC", "#000000", "#00FEFC", "#000000", "#00FEFC"]

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
    outline="#00FEFC",
    width=10,
    fill=""
)

# Create smaller circle with neon-like color
small_circle = canvas.create_oval(
    center_x - small_circle_radius,
    center_y - small_circle_radius,
    center_x + small_circle_radius,
    center_y + small_circle_radius,
    outline="#00FEFC",
    width=10,
    fill=""
)

# Create shaded big circles
for _ in range(5):
    shaded_big_circle = canvas.create_oval(0, 0, 0, 0, outline="#00FEFC", width=10, fill="#000000")
    shaded_big_circles.append(shaded_big_circle)

# Create shaded small circles
for _ in range(5):
    shaded_small_circle = canvas.create_oval(0, 0, 0, 0, outline="#00FEFC", width=10, fill="#000000")
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

def end_gui():
    # End the GUI
    root.destroy()
    
