# Jarvis-Library Basic_Codes

## pyttsx3

```python
import pyttsx3

engine = pyttsx3.init()

engine.say("Hello Sir, I am Jarvis")
engine.runAndWait()
```

```python
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)   # 0 = male, 1 = female (usually)
```

## Sppech Recognition and PyAudio

```python
import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)

try:
    command = recognizer.recognize_google(audio)
    print("You said:", command)
except Exception as e:
    print("Sorry, I did not understand.")
```

---
