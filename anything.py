from asyncio import exceptions
from datetime import datetime
from email.mime import audio
import speech_recognition as sr
import googletrans
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import PyPDF2
import gtts
import playsound
import smtplib
from myid import password, my_gmail , destination

p = password
g = my_gmail
d = destination




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
            voice = r.listen(source)
            command = r.recognize_google(voice)
            
            if 'alexa' in command:
                command = command.replace('kari', '')

        
                talk(command)
    
    except:
        print("sorry could not recognize")

    return command

def pdf_reader():
    book = open('os.pdf','rb')
    read = PyPDF2.PdfFileReader(book)
    pages = PyPDF2.PdfReader.numPages
    engine("Total number of pages in this pdf{pages} ")
    engine("Enter the page number i have to read:")
    pg = int(input())
    page = read.getPage(pg)
    text = page.extractText()
    talk(text)


        
def whatsAppmsg():
      pywhatkit.sendwhatmsg('7976989128', 'hey! this is kanu ka kari :p')
      
def greet():
    t_hour = datetime.datetime.now().hour
    if 24> t_hour < 4:
        talk('Good night and have sweet dreams ')
    elif 12> t_hour > 4:
        talk('Good morning')
    elif 12< t_hour <17:
        talk('Good afternoon')
    else:
        talk('Good evening')

    print(t_hour)


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()                                   #to connect  our server to gmail server
    server.starttls()
    server.login(g,p)
    server.sendmail(g,d, 'Mail from kanu ka Kari' )
    server.close()

def trans_text():
    trans_lang = 'hi'
    try:

        with sr.Microphone() as source:
            
            print("Listening...")

            r.adjust_for_ambient_noise(source, duration= 1)
            voice = r.listen(source)
            command = r.recognize_google(voice)
            regional = translator.translate(command , dest = trans_lang )
            print(regional.command)
            converted_audio = gtts.gTTS(regional.command, lang= trans_lang)
            converted_audio.save('regionallang.mp3')
            playsound.playsound('regionallang.mp3')



    except:
        print("sorry could not recognize")

    return command

    


if __name__ == "__main__":
    while True:

        command = take_command()
        print(command)
        if 'play' in command:
          song = command.replace('play','')
          talk('playing'+ song)
          pywhatkit.playonyt(song)
        elif 'time' in command:
          time = datetime.datetime.now().strftime('%I:%M %p')
          print(time)
          talk('Current time is ' + time)
        elif 'tell me about ' in command:
          person = command.replace('tell me about', '')
          info = wikipedia.summary(person, 3)
          print(info)
          talk(info)
        elif 'date' in command :
          talk('sorry ,i have a date with wifi')
        elif 'are you single' in command:
          talk('i have a girlfriend')
        elif 'joke' in command:
          print(pyjokes.get_joke())
          talk(pyjokes.get_joke())
        elif 'read pdf' in command:
          pdf_reader()
        elif 'WhatsApp' in command:
          pywhatkit.sendwhatmsg('+917976989128', 'hey! this is kanu ka Alexa :p',16,40)
        elif 'send email' in command:
          try:
            talk("what should i mail")
            content = take_command()
            to  = d
            sendemail(to, content)
            talk('email sent successfully')

          except Exception as e:
            print(e)
            talk('email has not been sent')
        elif 'translate' in command:
          talk('what should i translate for you')
          trans_text()
        elif 'greet' in command:
            greet()
        elif 'bye' in command:
          exit()

    
        else:
          talk('Please say the command again.')


        



#translated = translator.translate(text)
#print(translated.text)
