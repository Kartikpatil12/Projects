import ntpath
import os
from time import sleep
import sys
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import pyaudio
import pywhatkit as kit
import datetime 

def talk(audio):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def getcommand():
    print("listening....")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        command = r.listen(source)
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
    
#wish()
x = datetime.datetime.now()
time = x.strftime("%I%M %p")

while True:
    query = getcommand()
    if "wake up" in query:
        talk(f"hello sir. it's {time} . how may i help you sir")

    elif "date" in query:
        x = datetime.date.today()
        talk(x.strftime("%B %d ,%Y"))

    elif "notepad" in query:
        npath = "C:\\WINDOWS\\system32\\notepad.exe"
        os.startfile(npath)
        currentpath = npath
    
    elif "vs code" in query:
        npath = "D:\Microsoft VS Code\\code.exe"
        os.startfile(npath)
        currentpath = npath

    elif "cmd" in query:
        talk("Opening cmd...")
        os.system("start cmd")

    elif "wikipedia" in query:
         talk("searching on wikipedia...")
         query = getcommand()
         query.replace("wikipedia","")
         print(query)
         result = wikipedia.summary(query , sentences = 1)
         talk(result)
    
    elif "youtube" in query:
        talk("What do you like to search on youtube")
        query = getcommand()
        kit.playonyt(query)
    
    elif "google" in query:
        talk("What do you like to search on google ")
        query = getcommand()
        kit.search(query)

    
    elif "send message" in query:
        talk("please , Enter the number ")
        num = str(input())
        talk("What message you want to send ")
        query = getcommand()
        if "None" in query:
            query = getcommand()
        kit.sendwhatmsg_instantly(num , query)
        sleep(0.5)
        
        
    elif "thank" in query:
        talk("Welcome sir, Have nice day sir")
        sys.exit()

 
