from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer

def botWrite():
    chatbot = ChatBot('Chatbot')
    trainer= ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.english")
    #print(chatbot.get_response("what is computer"))
    print("hi,I am chatbot")
    while True:
        query = input(">>>")
        print(chatbot.get_response(Statement(text = query, search_text = query)))
