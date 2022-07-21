import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id)
engine.setProperty('rate', 170)

def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

dictapp = {"commandprompt":"cmd","notepad":"np","excel":"excel","brave": "brave"}

def openWebApp(query):
    speak("Launching web...")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("jarvis open","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")

def closeWebApp(query):
    speak("closing...")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
    elif "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(1)
        pyautogui.hotkey("ctrl","w")
        speak("all tab closed")
    elif "3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(1)
        pyautogui.hotkey("ctrl","w")
        sleep(1)
        pyautogui.hotkey("ctrl","w")
        speak("all tab closed")
    elif "4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(1)
        pyautogui.hotkey("ctrl","w")
        sleep(1)
        pyautogui.hotkey("ctrl","w")
        sleep(1)
        pyautogui.hotkey("ctrl","w")
        speak("all tab closed")
    elif "5 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(1)
        pyautogui.hotkey("ctrl","w")
        sleep(1)
        pyautogui.hotkey("ctrl","w")
        sleep(1)
        pyautogui.hotkey("ctrl","w")
        sleep(1)
        pyautogui.hotkey("ctrl","w")
        speak("all tab closed")
    
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")

    


    


