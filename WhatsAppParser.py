from sys import argv
from wordcloud import WordCloud
import matplotlib.pyplot as plt

class WaParser:
    chatData = []
    file = ""

    def __init__(self, file):
        self.file = file
        self.loadData()

    # Takes a whatsapp chatlog file as parameter and returns an array
    # Every Entry of the Array is a Dictionary with the keys
    # msg, date and sender
    def loadData(self):
        for line in self.file:
            try:
                splitted = line.split(': ')
                meta = splitted[0]
                text = splitted[1]
                if('Medien' not in text): # Deletes every "Media" Notification
                    msg = {'text':text, 'date':0, 'sender':""}
                    msg['date'], msg['sender'] = meta.split(" - ")
                    self.chatData.append(msg)
            except:
                pass

    def parseToString(self, sender=""):
        if sender=="":
            text = ""
            for i in self.chatData:
                text = text + "\n" + i['text']
            return text
        else:
            text = ""
            for i in self.chatData:
                if(i['sender']==sender):
                    text = text + "\n" + i['text']
            return text

if __name__ == "__main__":

    script, filename = argv

    f = open(filename,'r')
    chat = parseData(f)
    text = parseToString(chat)
    f.close()
