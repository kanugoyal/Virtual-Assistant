import speech_recognition as sr
import googletrans
import pyttsx3
import pywhatkit


r = sr.Recognizer()
translator = googletrans.Translator()
engine = pyttsx3.init()

def talk(text):

    engine.say(text)
    #engine.say('What can I do for you')
    engine.runAndWait()


#mic = sr.Microphone()
#sr.Microphone.list_microphone_names()
def take_command():

    try:

        with sr.Microphone() as source:
            
            print("Listening...")

            r.adjust_for_ambient_noise(source, duration= 1)
            audio = r.listen(source)
            command = r.recognize_google(audio)
            if 'alexa' in command:
                command = command.replace('alexa', '')

        
                talk(command)
    
    except:
        print("sorry could not recognize")

    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing'+ song)
        pywhatkit.playonyt(song)

run_alexa()        



#translated = translator.translate(text)
#print(translated.text)
