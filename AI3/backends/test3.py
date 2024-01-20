# # # import cv2

# # # print("OpenCV version:", cv2.__version__)
# # import requests
# # import geocoder

# # def Weather(api_key):
# #     # Get your current location using the 'geocoder' library
# #     location = geocoder.ip('me')
# #     city = location.city
# #     country = location.country

# #     # Make an API request to get weather data for your current location
# #     weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}'
# #     response = requests.get(weather_url)
# #     data = response.json()

# #     if response.status_code == 200:
# #         main_info = data['weather'][0]['main']
# #         description = data['weather'][0]['description']
# #         temp_kelvin  = data['main']['temp']
# #         humidity = data['main']['humidity']

# #          # Convert temperature from Kelvin to Celsius
# #         temp_celsius = temp_kelvin - 273.15

# #         weather_message = f"Today's weather in {city}, {country}: {main_info}, {description}. Temperature: {temp_celsius:.2f}°C. Humidity: {humidity}%."

# #         # Use your AI's 'Speak' function to speak the weather message
# #         print(weather_message)
# #     else:
# #         print("Sorry, I couldn't retrieve the weather information for your current location.")

# # # You need to define the 'Speak' function appropriately in your code.

# # # Call the Weather() function with your API key
# # api_key = 'd6b15a2faac86ae2db51c84b9a2d931c'
# # Weather(api_key)

# # import phonenumbers
# # from phonenumbers import carrier
# # import opencage
# # import folium
# # from phonenumbers import geocoder
# # from opencage.geocoder import OpenCageGeocode


# # number = "+91 9372136651"

# # ch_number = phonenumbers.parse(number)
# # location  = geocoder.description_for_number(ch_number, "en")
# # print(location)

# # service_number = phonenumbers.parse(number)
# # print(carrier.name_for_number(service_number, "en"))    


# # key = "24e14f3efe7443b08d11ab3241b7c520"

# # geocoder = OpenCageGeocode(key)
# # query = str(location)
# # results = geocoder.geocode(query)
# # # print(results)

# # lat = results[0]['geometry']['lat']
# # lng = results[0]['geometry']['lng']
# # print(lat, lng) 

# # myMap = folium.Map(location=[lat, lng], zoom_start=9)
# # folium.Marker([lat, lng], popup=location).add_to((myMap))
# # myMap.save("mylocation.html")

# # import geocoder

# # def CurrentLocation():
# #     # Get your current location using the 'geocoder' library
# #     location = geocoder.ip('me')
# #     city = location.city
# #     country = location.country
# #     latitude = location.latlng[0]
# #     longitude = location.latlng[1]

# #     location_message = f"You are currently in {city}, {country}. Latitude: {latitude}, Longitude: {longitude}."

# #     # Use your AI's 'Speak' function to speak the location message
# #     print(location_message)

# # # You need to define the 'Speak' function appropriately in your code.

# # # Call the CurrentLocation() function to get and display your current location
# # CurrentLocation()

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# # Import the By class
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# import keyboard         

# # Define a global variable to control the YouTube automation
# youtube_automation_active = False

# def open_youtube_video(search_query):
#     global youtube_automation_active
#     youtube_automation_active = True  # Start the YouTube automation

#     # Set the path to the Chrome driver executable
#     chromedriver_path = "win32\\chromedriver.exe"

#     # Create a Service object with the executable path
#     service = Service(executable_path=chromedriver_path)

#     # Initialize driver_youtube to None
#     driver_youtube = None

#     try:
#         # Create a Chrome driver with the service
#         driver_youtube = webdriver.Chrome(service=service)

#         # Maximize the Chrome window
#         driver_youtube.maximize_window()

#         # Open YouTube and search for the query
#         driver_youtube.get("https://www.youtube.com")
#         search_box = driver_youtube.find_element(By.CSS_SELECTOR, 'input[name="search_query"]')
#         search_box.send_keys(search_query)
#         search_box.send_keys(Keys.RETURN)

#         # Give time for the search results to load
#         time.sleep(2)

#         # Find and click on the first video link
#         video_links = driver_youtube.find_elements(By.CSS_SELECTOR, ".yt-simple-endpoint.style-scope.ytd-video-renderer")

#         if video_links:
#             video_links[0].click()  # Click the first video link
#             time.sleep(10)  # Wait for the video to load
#             # Start the YouTube automation loop
#             youtube_automation()
#         else:
#             print("No videos found for the search query.")

#     finally:
#         if driver_youtube is not None:
#             driver_youtube.quit()

# name = name.replace("play", "").replace("on youtube", "").replace("on", "").strip() # Remove the words "play" and "on youtube"
# search_query = name
# Speak(f"playing {search_query} on youtube.") 
# open_youtube_video(search_query)


# name="mockingbird"
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
# Import the By class
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import keyboard   
from webdriver_manager.chrome import ChromeDriverManager
driver_youtube = webdriver.Chrome(ChromeDriverManager().install())