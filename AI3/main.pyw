# import json
# import subprocess
# from Body.Listen import Connect  # Import your Connect module here
# from Body.Speak import Speak  # Import your Speak module here

# def main():
#     # Load the intents from the JSON file
#     with open("Brain/intents.json", "r") as file:
#         intents = json.load(file)["intents"]

#     while True:
#         text = Connect().lower()  # Assuming Connect() returns the recognized text as a string
#         # print("You said:", text)

#         # Check if the recognized text matches "wakeup" tag and patterns
#         for intent in intents:
#             if intent["tag"] == "wakeup" and any(pattern in text for pattern in intent["patterns"]):
#                 print("Wake-up phrase detected: {}".format(text))
#                 script_path = "C:\\Users\\qures\\OneDrive\\Desktop\\khizer\\AI3\\Buddy.py"
#                 subprocess.Popen(["python", script_path])  # Run the script using the Python interpreter
#                 return  # Exit the loop after executing the script

# if __name__ == "__main__":
#     Speak("listening mode on")
#     main()
import json
import subprocess
import cv2
import face_recognition
from Body.Listen import Connect  # Import your Connect module here
from Body.Speak import Speak  # Import your Speak module here

# Specify the path to your database folder
path = "Database/facedetection"

# Load the known faces and names from the database folder
known_faces = []
known_names = []

# Iterate over the files in the database folder
import os
for file in os.listdir(path):
    if file.endswith(".jpeg"):
        face_image = face_recognition.load_image_file(os.path.join(path, file))
        face_encoding = face_recognition.face_encodings(face_image)[0]
        known_faces.append(face_encoding)
        known_names.append(file.split(".")[0])

def main():
    # Load the intents from the JSON file
    with open("Brain/intents.json", "r") as file:
        intents = json.load(file)["intents"]

    while True:
        text = Connect().lower()  # Assuming Connect() returns the recognized text as a string

        # Check if the recognized text matches "wakeup" tag and patterns
        for intent in intents:
            if intent["tag"] == "wakeup" and any(pattern in text for pattern in intent["patterns"]):
                print("Wake-up phrase detected: {}".format(text))

                # Initialize the camera
                cap = cv2.VideoCapture(0)

                while True:
                    # Capture a frame from the camera
                    ret, frame = cap.read()

                    if ret: #check if the frame is valid
                        # Perform face recognition on the frame
                        face_locations = face_recognition.face_locations(frame)
                        face_encodings = face_recognition.face_encodings(frame, face_locations)

                        for face_encoding in face_encodings:
                            tolerance = 0.6  # Adjust this value (default is 0.6)
                            matches = face_recognition.compare_faces(known_faces, face_encoding, tolerance=tolerance) # Compare the captured face with the known faces


                            if True in matches:
                                Speak("Welcome, {}".format(known_names[matches.index(True)]) + "!")
                                # The face is recognized
                                name = known_names[matches.index(True)]
                                print(f"Welcome, {name}!")
                                cap.release()  # Release the camera
                                cv2.destroyAllWindows()  # Close OpenCV windows
                                script_path = "C:\\Users\\qures\\OneDrive\\Desktop\\khizer\\AI3\\Buddy.py"
                                subprocess.Popen(["python", script_path])  # Run the script using the Python interpreter
                                return  # Exit the loop after executing the script
                        if not any(matches):
                            print("Access denied")
                            Speak("Access denied")
                        
                    # Speak("access denied")
                    # Display the frame
                    cv2.imshow('Face Recognition', frame)

                    # Exit the loop when 'q' is pressed
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                cap.release()  # Release the camera
                cv2.destroyAllWindows()  # Close OpenCV windows

if __name__ == "__main__":
    Speak("Listening mode on")
    main()
