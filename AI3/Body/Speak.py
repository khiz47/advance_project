# Ai speaking function 
# two types of speak function( Windows based and Chrome based )
# Chrome based is more accurate but requires internet connection
# Windows based is less accurate but does not require internet connection
# modules we needed are
# pip install pyttsx3
# pip install selenium==(version)

import pyttsx3

# first we make windows based 
def Speak(Text):
    engine = pyttsx3.init("sapi5")
    # engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voices",voices[0].id)
    engine.setProperty("rate",170)
    engine.setProperty("volume",1)
    print(f"\nBuddy : {Text}.")
    engine.say(Text)
    engine.runAndWait()
# Speak("Assalamualaikum sir, I am Buddy, your personal assistant. How may I help you?")
# second we make chrome based main advantage Overspeaking disadvatag is word limit
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from time import sleep

# chrome_options = Options()
# chrome_options.add_argument("--log-levels=3")
# chrome_options.add_argument("--headless")  # Set headless mode here

# Path = "Database\win32\chromedriver.exe"
# service = Service(Path)  # Create a Service object with the path to ChromeDriver
# driver = webdriver.Chrome(service=service, options=chrome_options)  # Use 'service' instead of 'executable_path'
# driver.maximize_window()


# website = r"https://ttsmp3.com/text-to-speech/British%20English"
# driver.get(website)

# ButtonSelection = Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
# ButtonSelection.select_by_visible_text('British English / Brian')

# def Speak(Text):
#     lenghtoftext =len(str(Text))
#     if lenghtoftext == 0:
#         pass
#     else:
#         print("")
#         print(f"Buddy : {Text}.")
#         print("")
#         Data = str(Text)
#         Xpathofsec = '/html/body/div[4]/div[2]/form/textarea'
#         driver.find_element(by=By.XPATH,value=Xpathofsec).send_keys(Data)
#         driver.find_element(by=By.XPATH,value='//*[@id="vorlesenbutton"]').click()
#         driver.find_element(by=By.XPATH,value="/html/body/div[4]/div[2]/form/textarea").clear()

#         if lenghtoftext >= 30:
#             sleep(4)
#         elif lenghtoftext >=40:
#             sleep(6)
#         elif lenghtoftext >=55:
#             sleep(8)
#         elif lenghtoftext >=70:
#             sleep(10)
#         elif lenghtoftext >=100:
#             sleep(13)
#         elif lenghtoftext >=120:
#             sleep(14)
#         else:
#             sleep(2)
# # Speak("Assalamualaikum sir, I am Buddy, your personal assistant. How may I help you?")