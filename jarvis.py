
import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import pywhatkit

speaker=pyttsx3.init()
mic=sr.Recognizer()

speaker.say("welcome to jarvis")
speaker.runAndWait()

with sr.Microphone() as source:
     print("start speaking..")
     voice=mic.listen(source)
     text=mic.recognize_google(voice)
if "open Notepad" in text:
    print("Opening Notepad..")
    os.system("notepad")
elif "open command prompt" in text:
    print("Opening Command Prompt..")
    os.system("cmd")
elif "open YouTube" in text:
    print("Opening YouTube..")
    webbrowser.open("https://www.youtube.com")
elif "play naat" in text:
    print("playing naat..")
    webbrowser.open("https://www.youtube.com/watch?v=mlsehR6KgTQ&list=RDmlsehR6KgTQ&start_radio=1&pp=ygUEbmFhdKAHAQ%3D%3D")
elif "play song" in text:
    print("playing song..")
    webbrowser.open("https://youtu.be/9iIX4PBplAY?list=RD9iIX4PBplAY")
elif "open instagram" in text:
    print("Opening Instagram..")
    webbrowser.open("https://www.instagram.com")
    
elif "send message" in text:
    print("sending msg..")
    pywhatkit.sendwhatmsg_instantly("+9162693606","hi")