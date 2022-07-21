import pyttsx3
import datetime
import os


engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id)
engine.setProperty('rate', 170)

def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

extractedtime = open("alarmText.txt","rb")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("alarmText.txt","r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("jarvis","")
    timenow = timeset.replace("set an alarm","")
    timenow = timeset.replace(" and ",":")
    AlarmTime = str(timenow)
    print(AlarmTime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == AlarmTime:
            speak("Allarm buzzing...")
            os.startfile("almusic.mp3")
        elif currenttime + "00:00:30" == AlarmTime:
            exit()



