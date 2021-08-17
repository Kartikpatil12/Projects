import os
import sys
import webbrowser

import pyttsx3
import speech_recognition as sr
import wikipedia
import pyaudio
import datetime

def talk(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

def getcommand():
    print("listening....")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        command = r.listen(source , timeout=1)
    try:
        query = r.recognize_google(command , language="en-in").lower()
        print(f'You said {query}')

    except Exception as e:
        print(e)
        talk("Sorry sir i didn't recognize it . Can you please say that again..")
        return "None"
    return query

def wish():
    hour = datetime.datetime.now().hour
    if hour>0 and hour<12:
        talk("Good morning")
    elif hour>12 and hour<18:
        talk("Good afternoon")
    elif hour>18:
        talk("Good afternoon")
    talk("Hello Sir, How may i help you ")

talk("Jarvis is ready")
wish()
while True:
    query = getcommand()
    if "date" in query:
        x = datetime.date.today()
        talk(x)
    elif "cmd" in query:
        talk("Opening cmd...")
        os.system("start cmd")
    elif "google" in query:
        talk("opening google...")
        webbrowser.open("https://www.google.com/")

    elif "wikipedia" in query:
         talk("searching on wikipedia...")
         query.replace("wikipedia","")
         result = wikipedia.summary(query, sentences = 2)
         talk(result)
    elif "thank" in query:
        talk("Thank for using me, Have nice day sir")
        sys.exit()



