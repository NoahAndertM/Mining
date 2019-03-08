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
       splitMeta(meta,splittedMessage)
       chatData.append(splittedMessage)
     except:
         pass
    return chatData

def splitMeta(m, d):
    try:
        splitted = m.split(" - ")
        date = splitted[0]
        sender = splitted[1]
        #data['date'].append(date)
        #data['sender'].append(sender)
        splittedMessage['date'] = date
        splittedMessage['sender'] = sender
    except:
        pass

def parseToString(chatData):
    text = ""
    for i in chatData:
        text = text + "\n" + i['msg']

    return text

if __name__ == "__main__":

    script, filename = argv

    f = open(filename,'r')
    chat = parseData(f)
    text = parseToString(chat)
    f.close()
