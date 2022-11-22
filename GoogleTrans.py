import googletrans
import speech_recognition as sr
import pyaudio
import pyttsx3
import pywhatkit
import gtts
from langdetect import detect
import playsound

#print(googletrans.LANGCODES)
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        r.energy_threshold = 250
        audio = r.listen(source, 0 ,5)
    try:
        print('understanding..')
        input_lang = 'en-in'
        d = detect(input_lang)
        print(d)
        query = r.recognize_google(audio , language= input_lang)
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


def LangTrans(query):
    if "translate" in query:
        query = query.replace("robo","")
        query = query.replace("translate","")
        query = query.replace("robo translate","")
        t_lang = 'hi'
        translator = googletrans.Translator()
        translated = translator.translate(query , dest= t_lang)
        print(translated.text)
        convertedAudio = gtts.gTTS(translated.text, lang= t_lang)
        convertedAudio.save('translated.mp3')
        playsound.playsound('translated.mp3')
        speak("done")
