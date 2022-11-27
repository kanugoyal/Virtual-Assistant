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

p = password
g = my_gmail
d = destination

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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(g,p)
    server.sendmail(g , d , content)
    server.close()

def alarm(query):
    timehere = open("alarmText.txt","a")
    timehere.write(query)
    timehere.close()
    os.starthere("alarm.py")

if __name__ == "__main__":
    while True:
        query = takecommand().lower()
        if "wake up " in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takecommand().lower()
                if "go to sleep" in query:
                    speak("ok,you can call me anytime")
                    break
                
                elif "hello" in query:
                    speak("hello, how are you?")
                elif "i am fine" in query:
                    speak("what would you like me to do?")
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
                elif ' send email ' in query:
                  try:
                      speak("What should I say?")
                      content = takecommand()
                      to = d   
                      sendEmail(to, content)
                      speak("Email has been sent !")
                  except Exception as e:
                      print(e)
                      speak("I am not able to send this email")
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
                elif "stop bg music" in query:
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
                    speak('playing..')
                    music = "C:\\Users\\Anamika Computer\\Music"
                    song = os.startfile(os.path.join(music))
                    sleep(15)
                elif "finally sleep" in query:
                    speak("bye sir, going to rest tata ")
                    exit()











  