import pyttsx3
import speech_recognition as sr
import PyPDF2

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

def audioBook(query):
    if "read" in query:
        query = query.replace("jarvis","")
        query = query.replace("read","")
        query = query.replace("jarvis read","")
        book = open('os.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages
        print(pages)
        pg = pdfReader.getPage(2)
        text = pg.extractText()
        speak(text)
