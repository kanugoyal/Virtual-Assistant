import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

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

query =  takecommand().lower()
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id)
engine.setProperty('rate', 170)

def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("this is what i found")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,3)
            speak(result)

        except:
            speak("no speakable output available")

def searchYT(query):
    if "youtube" in query:
        speak("this is what i found")
        query = query.replace("youtube","")
        query = query.replace("search on youtube","")
        query = query.replace("jarvis","")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("done")

def searchWiki(query):
    if "wikipedia" in query:
        speak("searching from wikipedia")
        query = query.replace("wikipedia","")
        query = query.replace("search on wiki","")
        query = query.replace("jarvis","")
        results = wikipedia.summary(query, sentences = 2)
        speak("according to wikipedia..")
        print(results)
        speak(results)
        



        
