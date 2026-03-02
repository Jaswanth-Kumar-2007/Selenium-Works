# Selenium Library

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Other Library

import time
import speech_recognition as sr
import pyttsx3
from datetime import datetime

# Output Audio

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()



############################################################

# Introduction Function

def introduction(sample_text = "Hi"):
    speak(f"{sample_text} Jaswanth , How is your Day")
    speak("How may I Help You")

# Weather Function

def weather():
    driver = webdriver.Edge()
    driver.get("https://www.msn.com/en-in/weather/forecast/")
    temp_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'a[title][href*="temperature"]')
        )
    )
    sky_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR,'div[class*="summaryCaptionCompact"]')
        )
    )
    sky = sky_element.text
    temperature = temp_element.get_attribute("title")
    driver.quit()
    temp_res = int(temperature[0:2])
    speak(f"Jaswanth , Temperature is {temp_res} degree celsius")
    if (temp_res < 10):
        speak(f"Jaswanth , It was Cold Outside")
    elif (temp_res < 30):
        speak(f"Jaswanth , It was Chill Time")
    elif (temp_res < 35):
        speak(f"Jaswanth , It was Hot")
    elif (temp_res < 50):
        speak("Jaswanth , It was Very Hotty Outside")
    speak(f"And the Sky was {sky}")
    speak("Jarvis Executed")

# Youtube Function

def youtube(text):

    driver = webdriver.Edge()

    speak("Opening Youtube")

    driver.get("https://www.youtube.com")

    search_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.NAME, 'search_query')
        )
    )

    speak(f"Opening {text}")

    search_element.send_keys(f"{text}")
    search_element.send_keys(Keys.ENTER)

    video = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "video-title"))
    )

    video.click()

    time.sleep(3)

    speak("Video Opened Succesfully")

    time.sleep(50)

    speak("Jarvis Executed")

    driver.quit()

# Date and Time 

def tell_time():
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    speak(f"Jaswanth, the current time is {current_time}")

def tell_date():
    today = datetime.now()
    current_date = today.strftime("%d %B %Y")
    speak(f"Jaswanth, today's date is {current_date}")

# Websites

def open_website(text):

    driver = webdriver.Edge()

    driver.get(f"https://www.{text}.com")

    speak(f"Jaswanth {text} Opened Successfully")
    time.sleep(15)
    speak("Jarvis Executed")
    driver.quit()

# News Reader

def news_reader():
    
    driver = webdriver.Edge()

    driver.get(f"https://www.news.google.com")

    speak("Jaswanth News Opened Successfully")

    news_highlights = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, 'a.svxzne[href*="stories"]')
        )
    )
    for news in news_highlights:
        print(news.text)
        speak(f"Jaswanth {news.text}")
        time.sleep(3)
    time.sleep(10)
    speak("Jarvis Executed")
    driver.quit()


############################################################

# Main Function

def main():
    speak("Jarvis was Started")
    while(True):
        i = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak...")
            audio = i.listen(source)

            text = i.recognize_google(audio)
            print("You said:", text)

            text = text.lower()
        result = text.split()
        if (len(result) == 2):
            if (result[0] == "hi" and result[1] == "jarvis"):
                introduction()
            elif ("date" in result):
                tell_date()
            elif ("time" in result):
                tell_time()
            elif ("exit" in result):
                speak("Jarvis Was Closing")
                break
        elif (len(result) == 3):
            if (result[0] == "jarvis" and result[1] == "open"):
                open_website(result[2])
        elif ("news" in result):
            news_reader()
        elif (len(result) == 5):
            if (result[0] == "jarvis" and result[4] == "weather"):
                weather()
        elif ("youtube" in result):
            if (result[0] == "jarvis" and result[2] == "youtube"):
                text = ""
                for i in range(5,len(result)):
                    text += result[i]
                    text += " "
                youtube(text)
        else:
            speak("No Command Exist. Please Try Again")


# Run the Function

main()

