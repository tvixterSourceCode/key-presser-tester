import keyboard
import pyttsx3
import threading

current_key = None

while True:
    if keyboard.read_key():
        current_key = keyboard.read_key()
        threading.Thread(target=pyttsx3.speak,args=("you pressed "+ current_key,)).start()
        print(current_key)
        while keyboard.is_pressed(current_key):
           None
           