import requests
import pyttsx3
import json


engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id)
engine.setProperty('rate', 170)

def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    apidict = {"sports":"https://newsapi.org/v2/top-headlines?country=in&apiKey=67113e90ecac417c8b781fa6789eee2c",
                  "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=67113e90ecac417c8b781fa6789eee2c",
                  "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=67113e90ecac417c8b781fa6789eee2c",
                  "business":"https://newsapi.org/v2/top-headlines?country=in&apiKey=67113e90ecac417c8b781fa6789eee2c",
                  "technology":"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=67113e90ecac417c8b781fa6789eee2c"}

    content = None
    url = None
    speak("which field news you want")
    field =input("Type the field you want:")
    for key, value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
            if url is True:
                print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        
    speak("thats all")

