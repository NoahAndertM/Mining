from sys import argv
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Takes a whatsapp chatlog file as parameter and returns an array
# Every Entry of the Array is a Dictionary with the keys
# msg, date and sender
def parseData(f):
    chatData = []
    for line in f:
     try:
      splitted = line.split(': ')
      meta = splitted[0]
      msg = splitted[1]
      if('Medien' not in msg): # Deletes every "Media" Notification
       splittedMessage = {'msg':msg, 'date':0, 'sender':""}
       splittedMessage['date'], splittedMessage['sender'] = meta.split(" - ")
       chatData.append(splittedMessage)
     except:
         pass
    return chatData

def parseToString(chatData, sender=""):
    if sender=="":
        text = ""
        for i in chatData:
            text = text + "\n" + i['msg']
        return text
    else:
        text = ""
        for i in chatData:
            if(i['sender']==sender):
                text = text + "\n" + i['msg']
        return text

if __name__ == "__main__":

    script, filename = argv

    f = open(filename,'r')
    chat = parseData(f)
    text = parseToString(chat)
    f.close()
