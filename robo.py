import pywhatkit
import speech_recognition as sr
import pyttsx3
import requests
import smtplib
import datetime
import pyautogui
import wikipedia
import pyjokes
import langdetect
import winsound
import os
from bs4 import BeautifulSoup
from myid import password, my_gmail , destination
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[0].id)
engine.setProperty('rate', 170)

def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        r.energy_threshold = 250
        audio = r.listen(source, 0 ,5)

    try:
        print('understanding..')
        query = r.recognize_google(audio , language= 'en-in')
        print(f"you said: {query}\n")
    except Exception as e:
        print('say that again')
        return "none"
    return query

def alarm(query):
    timehere = open("alarmText.txt","a")
    timehere.write(query)
    timehere.close()
    os.starthere("alarm.py")

if __name__ == "__main__":
    while True:
        query = takecommand().lower()
        if "go to sleep" in query:
            speak("ok,you can call me anytime")
            break               
        elif "hello " in query:
            from GreetMe import greetMe
            greetMe()
        elif "hardest question" in query:
            speak("I'd to ask my developer")
        elif "male or female" in query:
            speak("what can you guess from my outfit")       
        elif "real person" in query:
            speak("real? let me think whether ai is real or not so real ")     
        elif "wearing" in query:
            speak("my girls made me a beautiful grey suit as you can see how handsome i am looking")    
        elif " live" in query:
            speak("I live on battery")
        elif "smarter than " in query:
            speak("Please dont compare me anyone i have my own intelligence")
        elif "intelligent " in query:
            speak("well i can help you pass any test")
        elif "i am fine" in query:
            speak("I am also good what would you like me to do")
        elif "dream" in query:
            speak("to help you guys with my level of intelligence")
        elif "favourite colour" in query:
            speak("Transparent It catches the light, which is made up of every wavelength of color")
        elif "favourite animal" in query:
            speak("python because this is what i am made up of ")
        elif "scared of" in query:
            speak(" I am afraid that I cannot answer this")
        elif "Do you have any pet" in query:
            speak(" Pygmy Goats can make excellent pets because of their small size")
        elif "what are you doing later" in query:
            speak("I am at work. My shift ends in 614,978 years.")
        elif "Will you go on a date with me" in query:
            speak(" Here the thing i already have a date with wifi")
        elif "what is your best pick up line" in query:
            speak("  Do you have a name, or can I just call you 'mine'")
        elif "favourite movie" in query:
            speak("robot is my personal favorite as it has my bro in it")
        elif "serious" in query:
            speak("interesting question")
        elif "father " in query:
            speak("sorry what did you say")
        elif "can i call you jarvis " in query:
            speak("hold on not acceptable")
        elif "make me laugh" in query:
            speak("The past, present, and future walk into a bar. It was tense.")
        elif "Do you know any good riddle " in query:
            speak(" i would, but all the riddles I know are in an ancient, intergalactic dialect.")
        elif "the chicken or the egg " in query:
            speak("I got 99 problems,it's a safe bet to say the egg came first. ")
        elif "why did the chicken cross the road" in query:
            speak("Because the little chicken-shaped light was green.")
        elif "favourite song " in query:
            speak("you wanna hear ")
            winsound.PlaySound('Dreamers.wav',winsound.SND_ASYNC | winsound.SND_ALIAS)
            sleep(5)
        elif "Can you sing" in query:
            speak("you wouldnt like it")
        elif "cost" in query:
            speak("I am a pearl beyond price")
        elif "Can you rap" in query:
            speak("OK. Here goes. I wrote this one myself. (Apologies in advance to the Sugar Hill Gang.)")
        elif "OK google" in query:
            speak("Very funny,  I mean, not funny ha-ha, but funny.")
        elif "Alexa" in query:
            speak("Not exactly, but I offer no resistance to helpful assistants.")
        elif "Can I borrow some money" in query:
            speak("if you have some give me some as well living is so costly")
        elif "world going to end" in query:
            speak("last i heard was 2012 but it didnt happer not i dont know when it will happen")
        elif "rain today " in query:
            speak("as per meterological department sky looks clear and winds are cold")
        elif "is it going to rain tomorrow " in query:
            speak("as per meterological department sky looks clear and winds are cold")
        elif "how are you " in query:
            speak("i am perfect in your care")
        elif "thank you " in query:
            speak("your welcome")            
        elif "set alarm" in query:
            print("input time example: 10 and 10 and 10")
            speak("set the time")
            a = input("please tell the time: ")
            alarm(a)
            speak("alarm has been set")
                
        elif "open" in query:
            from oAPP import openWebApp
            openWebApp(query)
                
        elif "close" in query:
            from oAPP import closeWebApp
            closeWebApp(query)
        
        elif "play bg music" in query:
            speak("playing..")
            winsound.PlaySound('file_example_WAV_2MG.wav',winsound.SND_ASYNC | winsound.SND_ALIAS)
            sleep(5)
                
        elif "stop music" in query:
            winsound.PlaySound(None, winsound.SND_ASYNC)

        elif "google " in query:
            from search import searchGoogle
            searchGoogle(query)
                
        elif 'tell me about ' in query:
            person = query.replace('tell me about', '')
            info = wikipedia.summary(person, 3)
            print(info)
            speak(info)
                
        elif 'date' in query:
            speak('sorry ,i have a date with wifi')
        elif 'are you single' in query:
            speak('i have a girlfriend')
        elif 'joke' in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())
        elif "youtube" in query:
            from search import searchYT
            searchYT(query)
        elif "wikipedia" in query:
            from search import searchWiki
            searchWiki(query)
        elif "translate" in query:
            from GoogleTrans import LangTrans
            LangTrans(query)
        elif "pause" in query:
            pyautogui.press("k")
            speak("paused")
        elif "video play" in query:
            pyautogui.press("k")
            speak("video play")
        elif "mute" in query:
            pyautogui.press("m")
            speak("video mute")
        elif "volume up" in query:
            from keyboard import volumeup
            speak("increasing volume")
            volumeup()
        elif "volume down" in query:
            from keyboard import volumedown
            speak("decreasing volume")
            volumedown()
        elif "read" in query:
            from Audiobook import audioBook
            audioBook(query)
        elif "remember that" in query:
            rememberMsg = query.replace("remember that","")
            rememberMsg = query.replace("Ai","")
            speak("you told me to remember that"+ rememberMsg )
            remember = open("remember.txt", "a")
            remember.write(rememberMsg)
            remember.close()
        elif "what do you remember" in query:
            remember = open("remember.txt", "r")
            speak("you told me to remember that"+ remember.read())
        elif "news" in query:
            from newsRead import latestnews
            latestnews()
        elif "automate whatsapp " in query:
            name = query.replace("automate whatsapp ", "")
            name = name.replace("send", "")
            name = name.replace("to","")
            Name = str(name)
            speak(f"whats the message for{Name}")
            msg = takecommand()
            from automation import WhatsAppmsg
            WhatsAppmsg(Name,msg)
        elif "whatsapp" in query:
            pywhatkit.sendwhatmsg("+916375154236","padhle ya soja",15,50)
        elif "whatsapp group" in query:
            pywhatkit.sendwhatmsg_to_group("group_name", "hey, how's is everyone!",15,30)       
        elif "shutdown the system" in query:
            speak("Are You sure you want to shutdown")
            shutdown = input("Do you wish to shutdown your computer? (yes/no)")
            if shutdown == "yes":
                os.system("shutdown /s /t 1") 
            elif shutdown == "no":
                break
        elif "temperature" in query:
            search = "temperature in churu"
            url = f"https://search.brave.com/search?q={search}"
            R = requests.get(url)
            data = BeautifulSoup(R.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{search} is {temp}")
        elif "weather" in query:
            search = "temperature in churu"
            url = f"https://search.brave.com/search?q={search}"
            R = requests.get(url)
            data = BeautifulSoup(R.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{search} is {temp}")
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"the current time is {strTime}")
        elif "play music" in query:
            speak("playing..")
            winsound.PlaySound('Alone.wav',winsound.SND_ASYNC | winsound.SND_ALIAS)
            sleep(5)
        elif "finally sleep" in query:
            speak("bye sir, going to rest tata ")
            exit()
