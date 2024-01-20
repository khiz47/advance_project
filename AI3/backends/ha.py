import serial
import time

# Connect to Arduino
ser = serial.Serial('COM5', 9600)  # Adjust 'COM3' based on your Arduino's port

def light_on():
    ser.write('a'.encode())
    time.sleep(1)  # Allow time for Arduino to process the command

def light_off():
    ser.write('b'.encode())
    time.sleep(1)  # Allow time for Arduino to process the command

# Example usage
light_on()  # Turn on the light
time.sleep(5)  # Wait for 5 seconds
light_off()  # Turn off the light
