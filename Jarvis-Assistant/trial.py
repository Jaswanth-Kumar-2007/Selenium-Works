import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def youtube():
    speak("Hi Jaswanth")
    speak("Wait a minute I will open YouTube")
    speak("Opened successfully")

with sr.Microphone() as source:
    print("Speak...")
    audio = r.listen(source)

    text = r.recognize_google(audio)
    print("You said:", text)

    text = text.lower()

    if "youtube" in text:
        youtube()


import speech_recognition as sr
import pyttsx3
import time

engine = pyttsx3.init()

r = sr.Recognizer()

def youtube():
    engine.say("Hi Jaswanth")
    engine.say("Wait a Minute I will open youtube")
    engine.say("Opened Successfully")
    engine.runAndWait()

with sr.Microphone() as source:
    print("Speak...")
    audio = r.listen(source)

    text = r.recognize_google(audio)
    print("You said:", text)

    if ("jarvis" in text.lower()):
        engine.say("Hello Jaswanth, My Name is Jarvis")
        engine.runAndWait()
    elif ("youtube" in text.lower()):
        youtube()
    engine.say("Bye Jaswanth")
    engine.runAndWait()