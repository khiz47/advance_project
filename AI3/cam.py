import cv2
import face_recognition

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

# Initialize the camera
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Perform face recognition on the frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for face_encoding in face_encodings:
        # Check if the face matches any known face
        matches = face_recognition.compare_faces(known_faces, face_encoding)

        if True in matches:
            # The face is recognized
            name = known_names[matches.index(True)]
            print(f"Welcome, {name}!")
        else:
            # The face is not recognized
            print("Unknown face!")

    # Display the frame
    cv2.imshow('Face Recognition', frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
