import speech_recognition as sr
import pyttsx3

sr.__version__

#creating a listener who would recognize your voice
listener = sr.Recognizer()
engine = pyttsx3.init()          #alexa will speak to us
engine.say('I am Alexa')
engine.say('What can i do for you?')
engine.runAndWait()


try:
    with sr.Microphone() as source:       #considering microphone as source
        print('listening...')
        voice = listener.listen(source)        #calling this speech recognizer to listen to the source
        command = listener.recognize_sphinx(voice)   #declareing a variable = giving voice to google and google will give text
        command = command.lower()
        if 'alexa' in command: 
            
            type(command)
except: 
    pass