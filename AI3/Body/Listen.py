# Listening in English and Hindi
# To build Listening function install the following packages  
# pip install googletrans=="new version"
# pip install speechrecognization


import speech_recognition as sr
from googletrans import Translator

# listen function 

# def Listen():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source,0,8) # if we use 8 here than it abort listening and listen again till 8 second (it stuck in listening mode thats why we use this)
#     try:
#         print("Recognizing.........")
#         text = r.recognize_google(audio,language="hi")
#         # print("You said : {}".format(text))
#     except:
#         print("Sorry could not recognize what you said")
#         text = "Sorry could not recognize what you said"
#     text = str(text).lower()
#     return text

# listen function

def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.5  # Adjust the pause threshold to capture natural pauses
        r.energy_threshold = 500  # Adjust the energy threshold for noise sensitivity
        audio = r.listen(source,0,8)  # Use timeout parameter instead of pause_threshold
    try:
        print("Recognizing...")  # Provide audio feedback that recognition is ongoing
        text = r.recognize_google(audio, language="hi, en-IN")
        # print("You said : {}".format(text))
    except sr.UnknownValueError:
        # print("Sorry, could not recognize what you said")
        print("Sorry, could not recognize what you said")  # Provide audio feedback for recognition failure
        text = "Sorry, could not recognize what you said"
    text = str(text).lower()
    return text


# translate function

def TranslationHintoEng(Text):
    line = str(Text)
    translator = Translator()
    translation = translator.translate(line,src="hi",dest="en")   
    print(f"You : {translation.text}.")
    return translation.text

# Connect

def Connect():
    query = Listen()
    data = TranslationHintoEng(query)
    return data

# Connect() # for testing purpose
