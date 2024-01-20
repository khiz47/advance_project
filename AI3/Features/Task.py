# Import necessary libraries at the beginning of your script
import datetime
import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1 , 'Body')
sys.path.insert(1, 'Database')
from Speak import Speak
from Listen import Connect
import json
from sumy.parsers.plaintext import PlaintextParser
import os
import subprocess
import pygetwindow as gw
import psutil
import pyttsx3
import re
import spacy
import math  # Import the math module
import sympy as sp  # Import the SymPy library
import time
import threading
from gui import *
import pyautogui
import cv2
import pygetwindow as gw
import requests
import geocoder
# import nltk
from PyDictionary import PyDictionary
 
# Ensure that NLTK is downloaded for sentence tokenization
# nltk.download('punkt')

#Non input functions

def Time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    Speak(f"Sir, the time is {time}")

def Date():
    date = datetime.datetime.now().strftime("%d/%m/%Y")
    Speak(f"Sir, the date is {date}")

def Day():
    day = datetime.datetime.now().strftime("%A")
    Speak(f"Sir, the day is {day}")

def WishMe():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        Speak("Good Morning sir!")
    elif hour >= 12 and hour < 18:
        Speak("Good Afternoon sir!")
    elif hour >= 18 and hour < 24:
        Speak("Good Evening sir!")
    else:
        Speak("Good Night sir!")
    Speak("Buddy at your service. Please tell me how can I help you today?")

def Notepad():
    Speak("Opening Notepad")

    # Prompt the user for a file name
    Speak("Please specify a file name.")
    file_name = Connect()  # Use voice input to capture the file name

    # Speak the file name for confirmation
    Speak(f"File name set to '{file_name}'. What would you like to write in Notepad?")

    # Initialize content as an empty string
    content = ""

    while True:
        # Continuously listen for user input
        user_input = Connect()

        # Handle backspace to remove words
        if "backspace" in user_input.lower():
            if content:
                content = " ".join(content.split()[:-1])  # Remove the last word
                Speak("Word removed.")
            else:
                Speak("There are no words to remove.")
        else:
            # Add the user input to the content
            content += user_input + "\n"

        # Check if the user wants to save the file
        if "save the file" in user_input.lower():
            break

    # Define the paths for saving the file on the desktop and in the database folder
    desktop_path = "C:\\Users\\qures\\OneDrive\\Desktop\\khizer\\AI3\\Features\\"
    database_path = "C:\\Users\\qures\\OneDrive\\Desktop\\khizer\\AI3\\Database\\Notepad\\"

    # Create the full paths for saving and moving the file
    file_path_on_desktop = os.path.join(desktop_path, file_name + ".txt")
    file_path_in_database = os.path.join(database_path, file_name + ".txt")

    if os.path.exists(file_path_in_database):
        Speak(f"A file with the name '{file_name}' already exists in the database. Do you want to overwrite it?")
        user_input = Connect().lower()
        if "yes" in user_input or "overwrite" in user_input:
            os.remove(file_path_in_database)  # Delete the existing file in the database folder

    # Write the user's content to the file on the desktop
    with open(file_path_on_desktop, "w") as f:
        f.write(content)

    # Rename and move the file to the database folder
    os.rename(file_path_on_desktop, file_path_in_database)

    # Notify the user about the file location and open it
    Speak(f"File '{file_name}.txt' saved. Opening the file.")
    os.startfile(file_path_in_database)

def Notepadud():
    # Define the path to the directory where text files are stored
    database_path = "C:\\Users\\qures\\OneDrive\\Desktop\\khizer\\AI3\\Database\\Notepad\\"

    Speak("Please specify the name of the text file you want to update, delete, or copy.")

    # List all text files in the Notepad folder, excluding copies
    text_files = [file for file in os.listdir(database_path) if file.endswith(".txt")]

    # Create a set to store the base names (without "_copyX" suffix)
    base_names = set()

    for file in text_files:
        base_name = file.split(".txt")[0]  # Get the base name without the extension
        if not any(base_name in f for f in base_names):
            # Only add to the set if this base name hasn't been added before
            base_names.add(base_name)

    # Now, base_names contains the unique base names of all files

    if not text_files:
        Speak("No text files found in the Notepad folder.")
        return

    Speak("Here are the files found in the Notepad folder:")
    for idx, file in enumerate(text_files, start=1):
        Speak(f"{idx}. {os.path.splitext(file)[0]}")

    while True:
        user_choice = Connect().strip().lower()  # Capture the user's choice in lowercase

         # Check if the user's input matches any file name exactly
        matching_files = [file for file in text_files if user_choice == os.path.splitext(file)[0].lower()]
        if not matching_files:
            # Split the user input into words
            user_words = user_choice.split()
            number_word_map = {
                "one": "1",
                "two": "2",
                "three": "3",
                "four": 4,
                "five": 5,
                # Add more mappings as needed
            }

            # Initialize variables to construct the file name
            base_name = ""
            copy_number = ""

            for word in user_words:
                if word == "underscore":
                    # Handle the "underscore" keyword
                    base_name += "_"
                elif word == "copy":
                    # Handle the "copy" keyword
                    copy_number = "1"  # Initialize with 1 by default
                elif word in number_word_map:
                    # Handle number words (e.g., "one," "two")
                    copy_number = number_word_map[word]
                else:
                    # Build the base name of the file
                    base_name += word

            # Construct the full file name
            user_choice = f"{base_name}copy{copy_number}"

        if "cancel" in user_choice or "cancel buddy" in user_choice or "ok listen, do this later" in user_choice:
            Speak("Ok sir, we will do it next time.")
            return

        # Convert the file names in the folder to lowercase for comparison
        lower_case_text_files = [file.lower() for file in text_files]

        # Check if the user's choice matches any file name
        matching_files = [file for file in lower_case_text_files if user_choice in os.path.splitext(file)[0]]

        if not matching_files:
            Speak(f"No file matching '{user_choice}' found in the Notepad folder.")
            return

        if len(matching_files) > 1:
            exact_match = [file for file in matching_files if file == f"{user_choice}.txt"]
            if exact_match:
                file_name = exact_match[0]
            else:
                matching_files = [file for file in text_files if user_choice in os.path.splitext(file)[0].lower()]

                if len(matching_files) > 1:
                    Speak("Multiple files match your choice. Please specify the exact file name.")
                    return
                elif len(matching_files) == 1:
                    file_name = matching_files[0]
                else:
                    Speak(f"No file matching '{user_choice}' found in the Notepad folder.")
                    return
        else:
            file_name = matching_files[0]

        # Get the original case of the matched file
        original_case_file = text_files[lower_case_text_files.index(matching_files[0])]

        file_name = original_case_file

        # Create the full path for the selected file
        file_path_in_database = os.path.join(database_path, file_name)

        Speak(f"File '{file_name}' found. Do you want to update, delete, or copy of this file?")
        user_input = Connect().lower()  # Capture the user's choice in lowercase

        while True:
            if "cancel" in user_input or "cancel buddy" in user_input or "ok listen, do this later" in user_input:
                Speak("Ok sir, we will do it next time.")
                return

            if "update file" in user_input:  # Check for the explicit "update file" command
                # Read the current content of the file
                with open(file_path_in_database, "r") as f:
                    current_content = f.read()
                    Speak(f"Current content of '{file_name}':\n{current_content}")

                Speak(f"Opening '{file_name}' for updates. What would you like to add or modify in this file?")
                content = ""  # Initialize content as an empty string

                while True:
                    # Continuously listen for user input
                    user_input = Connect().lower()  # Capture the user's choice in lowercase

                    if "cancel" in user_input or "cancel buddy" in user_input or "ok listen, do this later" in user_input:
                        Speak("Ok sir, we will do it next time.")
                        return

                    # Handle backspace to remove words
                    if "backspace" in user_input:
                        if content:
                            content = " ".join(content.split()[:-1])  # Remove the last word
                            Speak("Word removed.")
                        else:
                            Speak("There are no words to remove.")
                    elif "update this content" in user_input:  # Check for explicit "update this content" command
                        # Save the updated content to the existing file (overwrite)
                        with open(file_path_in_database, "w") as f:
                            f.write(content + "\n")
                        Speak(f"File '{file_name}' updated with your changes.")
                        return
                    else:
                        # Add the user input to the content
                        content += user_input + "\n"

            elif "copy file" in user_input:
                Speak(f"How many copies do you want to make of '{file_name}'?")
                while True:
                    num_copies = Connect().strip()  # Capture the user's choice in lowercase
                    number_word_map = {
                        "one": 1,
                        "two": 2,
                        "three": 3,
                        "four": 4,
                        "five": 5,
                        # Add more number words as needed
                    }
                    try:
                        if num_copies.lower() in number_word_map:
                            num_copies = number_word_map[num_copies.lower()]
                            if num_copies <= 0:
                                Speak("Please enter a valid number of copies greater than zero.")
                            else:
                                break
                        else:
                            num_copies = int(num_copies)
                            if num_copies <= 0:
                                Speak("Please enter a valid number of copies greater than zero.")
                            else:
                                break
                    except ValueError:
                        Speak("Please enter a valid number.")

                # Extract the base name (without "_copyX") from the current file_name
                base_name_match = re.match(r'^(.*)_copy(\d+)\.txt$', file_name)
                if base_name_match:
                    base_name = base_name_match.group(1)
                else:
                    base_name = os.path.splitext(file_name)[0]

                # Find the highest copy number for this file
                highest_copy_number = 0
                for existing_file in text_files:
                    match = re.match(rf'^{base_name}_copy(\d+)\.txt$', existing_file)
                    if match:
                        copy_number = int(match.group(1))
                        highest_copy_number = max(highest_copy_number, copy_number)

                # Create copies of the file based on the user's input
                for i in range(1, num_copies + 1):
                    new_copy_number = highest_copy_number + i
                    new_file_name = f"{base_name}_copy{new_copy_number}.txt"

                    # Create the full path for the new file within the same database folder
                    new_file_path = os.path.join(database_path, new_file_name)

                    # Copy the content of the original file to the new file
                    with open(file_path_in_database, "r") as f:
                        content = f.read()
                        with open(new_file_path, "w") as new_f:
                            new_f.write(content)

                    Speak(f"Ok, I'm making '{i}' copies of '{file_name}'. ")
                    Speak(f"File '{file_name}' copied as '{new_file_name}'.")

                return

            elif "delete file" in user_input:
                # Delete the specified file
                os.remove(file_path_in_database)
                Speak(f"File '{file_name}' has been deleted.")
                return

            else:
                Speak("Invalid choice. No changes made.")
                return

def close_notepad():
    notepad_processes = [process for process in psutil.process_iter(attrs=['pid', 'name']) if 'notepad' in process.info['name'].lower()]
    
    if notepad_processes:
        for process in notepad_processes:
            try:
                process_info = process.info
                process_name = process_info['name']
                process_id = process_info['pid']
                
                # Terminate the Notepad process
                psutil.Process(process_id).terminate()
                
                Speak("Closing Notepad")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
    else:
        Speak("No Notepad processes are running.")
# Notepadud()
# Example usage:
# Notepad()

# def close_notepad():
#     import pygetwindow as gw
#     notepad_windows = gw.getWindowsWithTitle('Notepad')
#     for window in notepad_windows:
#         if window.isActive:
#             Speak("Closing Notepad")
#             window.close()

# Function to minimize the Chrome browser
def minimize_chrome():
    chrome_window = gw.getWindowsWithTitle("Google Chrome")
    if chrome_window:
        chrome_window[0].minimize()
        Speak("minimize Google Chrome")

def close_chrome():

    # Iterate through all running processes
    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            process_info = process.info
            process_name = process_info['name']
            process_id = process_info['pid']

            # Check if the process is Google Chrome
            if process_name == 'chrome.exe':
                # Terminate the Chrome process
                psutil.Process(process_id).terminate()
                #Speak("Closing Google Chrome")  # Replace Speak with your actual function
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def scesho():
    # Capture the screenshot
    screenshot = pyautogui.screenshot()

    # Generate a unique filename based on the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"Database\\ScreenShot\\screenshot_{timestamp}.png"

    # Save the screenshot to the specified path
    screenshot.save(filename)

    # Ask the user if they want to view the screenshot
    Speak("Screenshot taken. Would you like to see it?")
    toggle_animation()
    user_response = Connect()
    
    if "show ss" in user_response or "yes buddy" in user_response or "yes" in user_response:
        # Open the screenshot using the default image viewer
        screenshot.show()
        toggle_animation()  
        Speak("The screenshot is saved in the database, and I'm showing it to you now.")
    else:
        toggle_animation()
        Speak("The screenshot is saved in the database.")

def close_screenshot():
    # pyautogui.hotkey('win', 'down')  # Minimize on Windows
    # Replace 'Photos' with the correct window title of the Photos app on your system
    window_title = 'Photos'

    # Find the window by its title
    window = gw.getWindowsWithTitle(window_title)

    if window:
        # Minimize the window
        window[0].minimize()
        Speak(f"Minimized {window_title}")
    else:
        print(f"No window found with title: {window_title}")

def take_picture():
    # Specify the directory to save the pictures
    save_directory = "Database\\picture"

    # Generate a picture name based on the current time
    current_time = time.strftime("%Y%m%d%H%M%S")
    output_file = os.path.join(save_directory, f"pic{current_time}.png")

    # Open the default camera (usually the built-in webcam)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Camera not found or cannot be opened.")
        return

    # Ask the user to smile
    Speak("Please smile for the picture.")
    time.sleep(4)

    # Countdown
    for count in range(3, 0, -1):
        Speak(str(count))
        time.sleep(1)

    # Capture a single frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture an image.")
        return

    # Save the captured image with the generated file name in the specified directory
    cv2.imwrite(output_file, frame)

    # Release the camera
    cap.release()

    Speak("Image captured.")

    # Ask the user if they want to see the picture
    Speak("Do you want to see the picture?")

    # Replace this with your function to get user input (e.g., using speech recognition)
    user_input = Connect().lower()

    if "yes" in user_input or "show" in user_input:
        # Show the picture using the default image viewer
        subprocess.Popen(["start", output_file], shell=True)
    else:
        Speak("Image saved.")
        print(f"Image saved as {output_file}")

def Weather(api_key):
    # Get your current location using the 'geocoder' library
    location = geocoder.ip('me')
    city = location.city
    country = location.country

    # Make an API request to get weather data for your current location
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}'
    response = requests.get(weather_url)
    data = response.json()

    if response.status_code == 200:
        main_info = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temp_kelvin  = data['main']['temp']
        humidity = data['main']['humidity']

         # Convert temperature from Kelvin to Celsius
        temp_celsius = temp_kelvin - 273.15

        weather_message = f"Today's weather in {city}, {country}: {main_info}, {description}. Temperature: {temp_celsius:.2f}°C. Humidity: {humidity}%."

        # Use your AI's 'Speak' function to speak the weather message
        Speak(weather_message)
    else:
        Speak("Sorry, I couldn't retrieve the weather information for your current location.")

# Call the Weather() function with your API key
api_key = 'd6b15a2faac86ae2db51c84b9a2d931c'

# Function to open PowerPoint files
def open_powerpoint():
    # Database path
    database_path = "Database\\powerpoint"

    # List PowerPoint files in the database
    powerpoint_files = [f for f in os.listdir(database_path) if f.endswith(".pptx")]

    if not powerpoint_files:
        # No PowerPoint files found in the database
        Speak("There are no PowerPoint files in the database. Do you want to open Microsoft PowerPoint?")
        user_input = Connect().lower()  # Replace with your function to get voice commands
        if any(keyword in user_input for keyword in ["yes", "yup", "yes please", "ya", "yah"]):
            # Open Microsoft PowerPoint
            subprocess.Popen(["start", "powerpnt"], shell=True)
        else:
            Speak("Okay, sir.")
        return

    # Speak the available file names
    Speak("Which file do you want to open? Available files are:")
    for file in powerpoint_files:
        Speak(file.replace(".pptx", ""))

    # Get user input
    user_input = Connect().lower()  # Replace with your function to get voice commands

    # Check if the user input matches a file name
    matching_files = [file for file in powerpoint_files if user_input in file.lower()]

    if matching_files:
        # Open the first matching file with the default application (PowerPoint)
        file_path = os.path.join(database_path, matching_files[0])
        subprocess.Popen(["start", "powerpnt", file_path], shell=True)
    else:
        # If no matching file was found
        Speak("The requested file was not found in the database.")

def close_powerpoint():
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if process.info['name'] == 'POWERPNT.EXE':
            process.kill()
            return True
    return False

def NonInputExecution(query):

    query = str(query)

    if "time" in query:
        Time()

    elif "date" in query:
        Date()

    elif "day" in query:
        Day()

    elif "wishme" in query:
        WishMe()
    
    elif "notepad" in query:
        Notepad()

    elif "udtxt" in query:
        Notepadud()

    # elif "closenotepad" in query:
    #     close_notepad()

    elif "closechrome" in query:
        close_chrome()
        Speak("Closing Google Chrome")

    elif "minimizechrome" in query:
        minimize_chrome()

    elif "clnp" in query: #close notepad
        close_notepad()
    
    elif "screenshot" in query:
        scesho()

    elif "closess" in query:
        close_screenshot()
    
    elif "picture" in query:
        take_picture()
    
    elif "weather" in query:
        Weather(api_key)

    elif "microsoftppt" in query:
        open_powerpoint()
    
    elif "closemipp" in query:
        close_powerpoint()

    else:
        Speak("Hii sir, your personal assistant is ready to help you.")    

#Input functions

# def InputExecution(tag, query):
#     if "wikipedia" in tag:
#         data = open("Brain/intents.json").read()
#         intents = json.loads(data)
#         intent = intents["intents"]
#         tag  = intent[12]["patterns"]
#         name = query
#         if tag in query:
#             name = str(query).replace(tag, "")
#         results =  wikipedia.summary(name, sentences=1)
#         Speak("According to my Knowledge")
#         Speak(results)
            
        
# data = open("Brain/intents.json").read()
# intents = json.loads(data)
# intent = intents["intents"]
# tag  = intent[12]["patterns"]
# print(tag)

# Function to preprocess and save the intro_paragraph to a file
def save_intro_paragraph_to_file(intro_paragraph):
    # Preprocess the intro_paragraph by removing extra newlines and formatting
    intro_paragraph = intro_paragraph.strip()
    with open(r"Features\\wikistore.md", "w", encoding="utf-8") as file:
        # Write the intro_paragraph in Markdown format
        file.write(f"# Introduction\n\n{intro_paragraph}")


# Function to read the intro_paragraph from the file
def read_intro_paragraph_from_file():
    try:
        with open(r"Features\\wikistore.md", "r", encoding="utf-8") as file:
            intro_paragraph = file.read().strip()
        return intro_paragraph
    except FileNotFoundError:
        return ""

# Function to clear the content of the file
def clear_file_content(file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("")




def InputExecution(tag, query):
    data = open("Brain/intents.json").read()
    intents = json.loads(data)
    intent = intents["intents"]
    
    # Find the correct intent based on the given tag
    intent_data = next(item for item in intent if item["tag"] == tag)
    patterns = intent_data["patterns"]
    
    name = ' '.join(query).lower()  # Convert the list of words into a single string
    
    for pattern in patterns:
        if pattern in name:
            name = name.replace(pattern, "").strip()  # Remove pattern and leading/trailing spaces
            break  # Exit loop after removing the pattern
    
    # Inside the "wikipedia" tag block
    if tag == "wikipedia":
        import bs4
        import requests
        import wikipediaapi
        from sumy.parsers.plaintext import PlaintextParser
        from sumy.nlp.tokenizers import Tokenizer
        from sumy.summarizers.lsa import LsaSummarizer
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"  # Replace with a valid user agent
        wiki_wiki = wikipediaapi.Wikipedia(language='en', user_agent=user_agent)
        
        try:
            page = wiki_wiki.page(name)
            
            if page.exists():
                intro_sentences = page.summary.split('.')[:1]  # Get the first sentence
                intro = '. '.join(intro_sentences)
                Speak(intro)

                Speak("You want to know more about it?")
                toggle_animation()

                intro2_sentences = page.summary.split('.')[:2]  # Get the first two sentences
                intro2 = '. '.join(intro2_sentences)
                result = intro2.replace(intro, "")

                user_input = Connect()
                if user_input.lower() in ["yes", "yup", "ya", "yes please"]:
                    toggle_animation()
                    Speak(result) 
                    Speak("Would you like me to summarize the rest of the page?")
                    toggle_animation()
                    user_input = Connect()
                    if user_input.lower() in ["yes", "yup", "ya", "yes please"]:
                        # Get the full page content
                        page_content = page.text
                
                        # Summarize the content
                        parser = PlaintextParser.from_string(page_content, Tokenizer("english"))
                        summarizer = LsaSummarizer()
                        summary_sentences = summarizer(parser.document, 3)  # Adjust '3' to the desired number of sentences in the summary
                        page_summary = ' '.join([str(sentence) for sentence in summary_sentences])
                        
                        # Speak or display the summary
                        toggle_animation()
                        Speak(page_summary)  # Replace 'Speak' with your actual function for text-to-speech
                    elif user_input.lower() in ["no", "no thanks", "I dont want to"]:
                        toggle_animation()
                        Speak("Alright, I won't summarize the page.")
                elif user_input.lower() in ["no", "no thanks", "I dont want to"]:
                    toggle_animation()
                    Speak("Alright sir, anything else for me to do?")
                    
            else:
                Speak("I couldn't find the information you requested on Wikipedia.")
        except Exception as e:
            print(f"An error occurred while fetching Wikipedia data: {str(e)}")
            Speak("An error occurred while fetching Wikipedia data.")

    # Inside the "wikipedia2" tag block
    elif tag == "wikipedia2":
        import wikipediaapi
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        wiki_wiki = wikipediaapi.Wikipedia(language='en', user_agent=user_agent)
        
        try:
            page = wiki_wiki.page(name)
            
            if page.exists():
                intro_paragraph = '\n'.join(page.text.split('\n')[:5]) 
                save_intro_paragraph_to_file(intro_paragraph)
                Speak(intro_paragraph,)
                Speak("If you want to summrize the content now, tell me to summarize.")
                # Save the intro_paragraph to a file for later use in the "summary" tag
            else:
                Speak("I couldn't find the information you requested on Wikipedia2.")
        except Exception as e:
            print(f"An error occurred while fetching Wikipedia data: {str(e)}")
            Speak("An error occurred while fetching Wikipedia data.")
    
    # Inside the "summary" tag block
    elif tag == "summary":
        from sumy.parsers.plaintext import PlaintextParser  # Add this import
        from sumy.nlp.tokenizers import Tokenizer
        from sumy.summarizers.lsa import LsaSummarizer

        try:
            # Read the intro_paragraph from the file
            intro_paragraph = read_intro_paragraph_from_file()

            print("Intro Paragraph Before Summarization:")
            print(intro_paragraph)  # Debugging line

            if intro_paragraph:
                # Perform summarization on the intro_paragraph
                parser = PlaintextParser.from_string(intro_paragraph, Tokenizer("english"))
                summarizer = LsaSummarizer()
                intro_summary = summarizer(parser.document, sentences_count=2)  # Summarize the paragraph to 2 sentences

                print("Summary:")
                print(intro_summary)  # Debugging line

                # Check if there are sentences in the summary
                if len(intro_summary) > 0:
                    intro = ""
                    for sentence in intro_summary:
                        intro += str(sentence)
                    Speak(intro)
                else:
                    Speak("I couldn't generate a summary from the stored content.")
                # Clear the saved intro_paragraph from the file
                clear_file_content("Features\wikistore.md")
            else:
                Speak("I couldn't find the information you requested.")
        except Exception as e:
            print(f"An error occurred while summarizing: {str(e)}")
            Speak("An error occurred while summarizing.")

    # Inside the "google" tag block
    elif tag == "google":
            import pywhatkit
            # pywhatkit.search(name)
            import wikipedia as googleScrap
            Speak("Searching on google")
            query = name
            # Speak("Searching...")
            try:
                pywhatkit.search(query)
                results = googleScrap.summary(query, sentences=1)
                Speak("According to my Knowledge")
                Speak(results)
            except:
                Speak("Sorry, I couldn't find information about '{name}' on Wikipedia.")

    # Inside the "calculator" tag block
    elif tag == "calculator":
        # calculator part starts here==========================
        # Load the spaCy NLP model
        nlp = spacy.load("en_core_web_sm")

        def detect_equation_type(query):
            # Process the user's query using spaCy
            doc = nlp(query.lower())

            # Define keywords and operators for each equation type
            arithmetic_operators = ['+', '-', '*', '/', '^', '%']
            algebraic_keywords = ['x','y','z','a','b','c']
            logarithmic_keywords = ['log', 'logarithm','and','of']
            trigonometric_keywords = ['sin', 'cos', 'tan', 'cot', 'sec', 'cosec']

            # Check if it's a simple arithmetic calculation
            if all(token.text.isnumeric() or token.text in arithmetic_operators for token in doc):
                print("Arithmetic Equation")
                return "arithmetic"

            # Check if it's a logarithmic equation with variables
            elif any(keyword in doc.text for keyword in logarithmic_keywords):
                print("Logarithmic Equation")
                return "logarithmic"

            # Check if it's a trigonometric equation with variables
            elif any(keyword in doc.text for keyword in trigonometric_keywords):
                print("Trigonometric Equation")
                return "trigonometric"

            # Check if it's an algebraic equation with variables
            elif all(token.is_alpha for token in doc if token.text.isalpha()):
                print("Algebraic Equation")
                return "algebraic"
            

            # Calculate probabilities for each equation type based on keyword presence
            probability = {
                'arithmetic': sum(1 for token in doc if token.text in arithmetic_operators) / len(arithmetic_operators),
                'algebraic': sum(1 for token in doc if token.text in algebraic_keywords) / len(algebraic_keywords),
                'logarithmic': sum(1 for token in doc if token.text in logarithmic_keywords) / len(logarithmic_keywords),
                'trigonometric': sum(1 for token in doc if token.text in trigonometric_keywords) / len(trigonometric_keywords),
            }

            # Determine the equation type with the highest probability
            most_likely_equation_type = max(probability, key=probability.get)
            max_probability = probability[most_likely_equation_type]

            # Set a threshold for probability (e.g., 0.7)
            threshold = 0.7

            # If the highest probability exceeds the threshold, return the equation type
            if max_probability >= threshold:
                return most_likely_equation_type
            else:
                return "unknown"  # If none of the types meet the threshold

        # Function to handle arithmetic equations
        def handle_arithmetic_equation(query):
            try:
                # Remove any non-mathematical words and punctuation from the query
                query = query.replace("Calculate", "").strip()
                query = query.replace(" ","").replace("raised to the power of", "**").replace("to the power of", "**").replace("power", "**").replace("^","**").replace("minus", "-").replace("plus", "+").replace("multiplied by", "*").replace("divided by", "/").replace("divide by","/").replace("modulus", "%").replace("remainder", "%").replace("percentage","%").replace("percent","%")
                query = ''.join(filter(lambda x: x in '0123456789+-*/', query))

                # Evaluate the arithmetic expression
                equation_type = "Arithmetic Equation"
                result = eval(query)
                Speak(f"The result is {result}")
                Speak("you want to save this in file?")
                ans = Connect().lower() 
                if ans == "yes" or ans == "ya" or ans == "yup" or ans == "yep" or ans == "yeah" or ans == "ha":
                    # Save the solution to a file
                    save_solution_to_file(query, result, "N/A", equation_type)
                else:
                    Speak("okay sir...")
            except Exception as e:
                Speak("I couldn't calculate the arithmetic expression. Please check your input.")

        # Function to handle algebric equations
        def handle_algebraic_equation(query):
            try:
                # Standardize the input by removing extra whitespace and "solve"
                query = query.strip().replace("solve ", "")
                query = query.replace("equal to","=")

                # Add "*" operator between coefficients and variables if missing
                query = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', query)

                # Split the equation by "=" to separate the left and right sides
                sides = query.split("=")

                # Check if there are exactly two sides
                if len(sides) != 2:
                    print("Invalid input format. Please include '=' to specify the result.")
                    return

                left_side, right_side = sp.sympify(sides[0].strip()), sp.sympify(sides[1].strip())

                # Define symbolic variables
                x, y, z, a, b, c = sp.symbols('x y z a b c')

                # Create an equation with the left and right sides
                equation = sp.Eq(left_side, right_side)

                # Attempt to solve the equation for 'y'
                solution = sp.solve([equation], (x, y, z, a, b, c))

                if solution:
                    for variable, value in solution.items():
                        # print(f"Solve for {variable}: {value}")
                        Speak(f"Solve for {variable}: {value}")

                    # Prepare the steps text
                    steps_text = f"Step 1: Parse the equation.\n"
                    steps_text += f"Step 2: Solve the equation.\n"
                    steps_text += f"Equation: {equation}\n\n"
                    for variable, value in solution.items():
                        steps_text += f"Solve for {variable}: {value}\n"
                        
                    # Call the function to save the solution to a file
                    save_solution_to_file(query, solution, steps_text, "Algebraic Equation")

                else:
                    print("No solution found for the given equation.")

            except Exception as e:
                error_message = f"An error occurred while solving the equation. error: {str(e)}"
                print(error_message)
            # Example usage to solve for 'y'
            # handle_algebraic_equation("2x + 2y = 10x + 5y")

        # Function to handle logarithmic equations
        def handle_logarithmic_equation(query):
            try:
                # Standardize the input by removing extra whitespace and "equal to"
                query = query.strip().replace("equal to", "=")

                # Add "solve" to the query if it's not present
                if not query.lower().startswith("solve "):
                    query = "solve " + query

                # Define a regular expression pattern to match the input format
                log_match = re.search(r'solve\s*log\s*(\d+)\s*and\s*(\d+)\s*=\s*(\w+)', query)

                if log_match:
                    base = float(log_match.group(1))
                    number = float(log_match.group(2))
                    result = log_match.group(3)

                    # Calculate the logarithmic equation
                    if base > 0 and base != 1 and number > 0:
                        x = round(math.log(number, base), 4)
                        result_text = f"{result} = {x:.4f}"
                    else:
                        result_text = "Invalid input. Base and number must be positive, and base cannot be 1."

                    # print(f"Solved: {result_text}")
                    Speak(f"Solved: {result_text}")

                    # Prepare the steps text
                    steps_text = f"Step 1: Parse the equation.\n"
                    steps_text += f"Step 2: Solve the equation.\n"
                    steps_text += f"Equation: log({base})({number}) = {result}\n\n"
                    steps_text += f"Solved: {result_text}\n"

                    # Call the function to save the solution to a file
                    # Assuming you have the `save_solution_to_file` function defined
                    save_solution_to_file(query, result_text, steps_text, "Logarithmic Equation")

                else:
                    print("Invalid input format. Please use the format 'solve log(base) and number = result'.")

            except Exception as e:
                error_message = f"An error occurred while solving the equation. Error: {str(e)}"
                print(error_message)
            # handle_logarithmic_equation("log 3 and 24 = x")

        # Function to handle trigonometric equations
        def handle_trigonometric_equation(query):
            try:
                # Standardize the input by removing extra whitespace and "equal to"
                query = query.strip().replace("equal to", "=")

                # Add "solve" to the query if it's not present
                if not query.lower().startswith("solve "):
                    query = "solve " + query

                # Define a regular expression pattern to match various query formats
                trig_match = re.search(r'(sin|cos|tan|cot|sec|cosec)\s*([a-zA-Z]+)?\s*=\s*(\d+(\.\d+)?)', query)

                if trig_match:
                    trig_function = trig_match.group(1)
                    angle = trig_match.group(2)
                    result = float(trig_match.group(3))  # Convert result to a float

                    # Automatically add brackets around the variable if it's not empty
                    if angle:
                        angle = f"({angle})"

                    # Handle the trigonometric equation here
                    equation = f"{trig_function}{'' if angle is None else angle} = {result}"

                    # Solve the equation symbolically
                    x = sp.symbols('x')
                    symbolic_eq = sp.Eq(sp.sin(x), result)  # Change 'sin' to the appropriate trigonometric function
                    solutions = sp.solve(symbolic_eq, x)

                    # Check if there are solutions
                    if solutions:
                        result_text = f"Trigonometric equation: {equation}\nSolutions for {angle if angle else 'x'}:"
                        for solution in solutions:
                            result_text += f"\n{angle if angle else 'x'} = {solution.evalf()}"
                    else:
                        result_text = f"Trigonometric equation: {equation}\nNo solutions found."

                    # print(f"Solved: {result_text}")
                    Speak(f"Solved: {result_text}")

                    # Prepare the steps text
                    steps_text = f"Step 1: Parse the equation.\n"
                    steps_text += f"Step 2: Solve the equation symbolically.\n"
                    steps_text += f"Equation: {equation}\n\n"
                    steps_text += f"Solved: {result_text}\n"

                    # Call the function to save the solution to a file
                    # Assuming you have the `save_solution_to_file` function defined
                    save_solution_to_file(query, result_text, steps_text, "Trigonometric Equation")

                else:
                    print("Invalid input format. Please use the format 'solve trig_function(variable) = result'.")

            except Exception as e:
                error_message = f"An error occurred while solving the equation. Error: {str(e)}"
                print(error_message)
            # handle_trigonometric_equation("sin x equal to 0.5")

        # Function to generate solution and steps
        def generate_solution_and_steps(equation):
            steps = []  # Create an empty list to store steps

            # Add steps to the list as you calculate them
            steps.append("Step 1: Parse the expression.")
            steps.append("Step 2: Perform the necessary operations.")
            steps.append("Step 3: Get the result.")

            # Join the steps into a single string with line breaks
            steps_text = "\n".join(steps)

            # Attempt to evaluate the expression based on its type
            result = None
            if "arithmetic" in equation:
                result = solve_arithmetic_equation(equation)
            elif "algebraic" in equation:
                result = solve_algebraic_equation(equation)
            elif "logarithmic" in equation:
                result = solve_logarithmic_equation(equation)
            elif "trigonometric" in equation:
                result = solve_trigonometric_equation(equation)

            return result, steps_text

        # Function to save solution and steps in a Markdown file
        def save_solution_to_file(equation, result, steps_text, equation_type):
            # Specify the directory path where files will be saved
            base_directory = "C:\\Users\\qures\\OneDrive\\Desktop\\khizer\\AI3\\Database\\maths"

            # Ask for a filename to save the solution
            Speak("Please specify a filename to save the solution (without extension).")
            file_name = Connect().lower()  # Replace with your voice input method

            # Create the full file path including the directory and .md extension
            full_file_path = os.path.join(base_directory, f"{file_name}.md")

            # Save the solution in a Markdown file
            with open(full_file_path, "w") as md_file:
                md_file.write(f"# {equation_type}\n\n")
                md_file.write(f"**Mathematical Expression**: {equation}\n\n")
                md_file.write(f"**Solution**: {result}\n\n")
                md_file.write(f"**Steps**:\n\n{steps_text}")  # Include steps in the file

            Speak(f"Solution saved as '{file_name}.md' in the specified location.")

        # Main function for the calculator
        def main_calculator():
            query = name # Getting user input by speaking to the microphone
            # query = input("Enter your query: ")
            # Detect the type of mathematical equation
            equation_type = detect_equation_type(query)

            # Set a threshold for probability (e.g., 0.7)
            threshold = 0.7

            # Route the query to the appropriate handler based on the detected equation type and probability
            if equation_type == "arithmetic":
                handle_arithmetic_equation(query)
            elif equation_type == "algebraic":
                handle_algebraic_equation(query)
            elif equation_type == "logarithmic":
                handle_logarithmic_equation(query)
            elif equation_type == "trigonometric":
                handle_trigonometric_equation(query)
            else:
                Speak("I couldn't determine the type of mathematical equation. Please check your input.")

        # Call the main calculator function
        main_calculator()

        # calculator part ends here==========================

    # Inside the "whatsapp" tag block
    elif tag == "whatsapp":
        import pywhatkit as kit
        import datetime
        import time
        # List of contacts and phone numbers
        ListWeb = {
            'team': "+91 82917 88306",
            'potter': "+9191368 48986",
            'king': "+9170212 35976",
            'annabelle': "+9184240 98766",
            'mom': "+9188506 99485",
            'brother': "+9184336 35458",
            'bhai': "+9193262 39256",
            'haroon sir': "+9196643 68663",
            'shahid sir': "+9198217 71054"
            
        }
        
        file_path = "Database\whatsmsg\msg.txt"

        def write_message_from_file(file_path, msg):
            with open(file_path, "w") as msg_file:
                msg_file.write(msg)

        def read_message_from_file(file_path):
            try:
                with open(file_path, "r") as msg_file:
                    msg = msg_file.read()
                return msg.strip()
            except FileNotFoundError:
                return None

        def clear_message_file(file_path):
            with open(file_path, "w") as msg_file:
                msg_file.write("")

        while True:
            # Check if the name is in the contact dictionary
            if name in ListWeb:
                whatsappname = name
                Speak(f"What is the message for {whatsappname}?")
                toggle_animation()
                # Initialize content as an empty string
                content = ""
                # Take input until "ok send this message" is received
                while True:
                    msg_input = Connect()
                    
                    # Handle backspace to remove words
                    if "backspace" in msg_input.lower():
                        if content:
                            content = " ".join(content.split()[:-1])  # Remove the last word
                            Speak("Word removed.")
                        else:
                            Speak("There are no words to remove.")
                    elif msg_input.lower() in ["ok send this message", "okay sent this message","send this message"]:
                        toggle_animation()
                        break
                    else:
                        # Add the user input to the content
                        content += msg_input + " "

                # Remove the phrases before writing to the file
                content = content.replace("ok send this message", "").replace("okay sent this message", "").replace("send this message", "").strip()  

                write_message_from_file(file_path, content)

                msg = read_message_from_file(file_path)
                if msg:
                    # Send the message
                    now = datetime.datetime.now()
                    hour = now.hour
                    minute = now.minute + 1
                    Speak("Sending message, please wait")
                    time.sleep(5)
                    kit.sendwhatmsg(ListWeb[whatsappname], msg, hour, minute)
                    time.sleep(10)
                    Speak("Message sent")
                    
                    # Clear msg.txt
                    clear_message_file(file_path)
                else:
                    Speak("No message found in msg.txt. Please provide a message before sending.")
                break
            else:
                Speak("Please can you say the name once again? I don't have it in the dictionary.")
                name = Connect()

    # Inside the "Identity2" tag block
    elif tag == "Identity2":
        user = name.replace("my name is", "").replace("i am", "").replace("is", "").strip()
        if user:
            Speak(f"Nice to meet you, {user}!")
        else:
            Speak("Sorry can you tell your name?")         

    # Inside the "youtube" tag block
    elif tag == "youtube":
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service as ChromeService
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        # Import the By class
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.keys import Keys
        import time
        import keyboard         
        # Define a global variable to control the YouTube automation
        youtube_automation_active = False
        # Function to control YouTube video playback
        def youtube_automation():
            global youtube_automation_active
            keyboard.press("space") # to get focuse on youtube video
            while youtube_automation_active:
                command = Connect().lower()  # Replace with your function to get voice commands
                if "stop" in command or "start" in command or "wait" in command:
                    Speak("ok sir")
                    keyboard.press("space")  # Press the space bar to stop/play the video
                    keyboard.release("space")
                elif "forward" in command:
                    keyboard.press("l")  # Press the l arrow key to skip forward 10 seconds
                    keyboard.release("l")
                    Speak("Forwarded")
                elif "back" in command or "backward" in command:
                    keyboard.press("j")  # Press the j arrow key to go back 10 seconds
                    keyboard.release("j")
                    Speak("backwarded")
                elif "restart" in command or "again" in command or "replay" in command:
                    Speak("Restarting video")
                    keyboard.press("0")  # Press "0" key to restart the video
                    keyboard.release("0")
                elif "mute" in command:
                    Speak("muting video")
                    keyboard.press("m")  # Press "m" key to mute the video
                    keyboard.release("m")
                elif "unmute" in command:
                    Speak("Unmuting video")
                    keyboard.press("m")  # Press "m" key to unmute the video
                    keyboard.release("m")
                elif "full screen" in command or "escape" in command:
                    Speak("Wait sir")
                    keyboard.press("f")  # Press "f" key to toggle full screen
                    keyboard.release("f")
                elif "half screen" in command:
                    Speak("half sreen mode")
                    keyboard.press("i")  # Press "f" key to toggle full screen
                    keyboard.release("i")
                elif "skip ad" in command:
                    Speak("Skipping ads")
                    keyboard.press("Z")  # Press "s" key to skip the ad
                    keyboard.release("Z")
                elif "next video" in command:
                    keyboard.press("Shift+n")  # Press "n" key to play the next video
                    keyboard.release("Shift+n")
                    Speak("Playing next video")
                elif "previous video" in command:
                    keyboard.press("Shift+p")  # Press "p" key to play the previous video
                    keyboard.release("Shift+p")
                    Speak("Playing previous video")
                elif "subtitles" in command:
                    keyboard.press("c")  # Press "c" key to toggle subtitles
                    keyboard.release("c")
                    Speak("subtitles on")
                elif "no subtitles" in command:
                    keyboard.press("c")  # Press "c" key to toggle subtitles
                    keyboard.release("c")
                    Speak("Subtitles off")
                elif "volume up" in command or "increase volume" in command:
                    keyboard.press("up arrow")  # Press the up arrow key to increase volume
                    keyboard.release("up arrow")
                    Speak("Volume increased")
                elif "volume down" in command or "decrease volume" in command:
                    keyboard.press("down arrow")  # Press the down arrow arrow key to decrease volume
                    keyboard.release("down arrow")
                    Speak("Volume decreased")
                elif "exit" in command:
                    Speak("Ok sir, stopping youtube")
                    youtube_automation_active = False  # Exit the YouTube automation loop
                    break
                else:
                    print("Sorry, I didn't understand that. Please try again.")  # Handle unrecognized commands
                time.sleep(1)
        # Function to open YouTube and play a video
        def open_youtube_video(search_query):
            global youtube_automation_active
            youtube_automation_active = True  # Start the YouTube automation
            # Set the path to the Chrome driver executable
            chromedriver_path = "Database\\win32\\chromedriver.exe"

            # Create a Service object with the executable path
            service = Service(executable_path=chromedriver_path)

            try:
                # Create a Chrome driver with the service
                driver_youtube = webdriver.Chrome(service=service)

                # Maximize the Chrome window
                driver_youtube.maximize_window()

                # Open YouTube and search for the query
                driver_youtube.get("https://www.youtube.com")
                search_box = driver_youtube.find_element(By.CSS_SELECTOR, 'input[name="search_query"]')
                search_box.send_keys(search_query)
                search_box.send_keys(Keys.RETURN)

                # Give time for the search results to load
                time.sleep(2)

                # Find and click on the first video link
                video_links = driver_youtube.find_elements(By.CSS_SELECTOR, ".yt-simple-endpoint.style-scope.ytd-video-renderer")

                if video_links:
                    video_links[0].click()  # Click the first video link
                    time.sleep(10)  # Wait for the video to load
                    # # Start the thread for YouTube automation
                    # youtube_thread = threading.Thread(target=youtube_automation, args=(driver_youtube,))
                    # youtube_thread.start()
                else:
                    print("No videos found for the search query.")
                # Start the YouTube automation loop
                youtube_automation()

            finally:
                driver_youtube.quit()
        name = name.replace("play", "").replace("on youtube", "").replace("on", "").strip() # Remove the words "play" and "on youtube"
        search_query = name
        Speak(f"playing {search_query} on youtube.") 
        open_youtube_video(search_query)
        
    # Inside the "scroll function" tag block
    elif tag == "scroll":

        def scroll(direction, amount=1):
            scroll_amount = amount if direction == "up" else -amount
            pyautogui.scroll(scroll_amount)
            print(f"scrolling {direction}")

        # Function to handle voice commands
        def handle_voice_command_scroll(command):
            if "up" in command:
                scroll("up", amount=300)
            elif "down" in command:
                scroll("down", amount=300)
            else:
                print("Command not recognized")
        handle_voice_command_scroll(name)

    elif tag == "dictionary":
        # Use PyDictionary to get the meaning
        dictionary = PyDictionary()
        meaning = dictionary.meaning(name)
        
        if meaning:
            Speak(f"The meaning of {name} is: {meaning}")
        else:
            Speak(f"Sorry, I couldn't find the meaning for {name}.")