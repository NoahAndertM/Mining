from sys import argv
from wordcloud import WordCloud
import matplotlib.pyplot as plt

script, filename = argv
data = {'date':[],'sender':[], 'msg':[]}

def parseData(f):
    chatData = []
    #text = ""
    for line in f:
     try:
      splitted = line.split(': ')
      meta = splitted[0]
      msg = splitted[1]
      if('Medien' not in msg): # If any form of media is sent, WhatsApp prints "<Media Omitted>". Getting rid of this. TO DO: Improve this functionality.
       #text = text + "\n" + msg
       #data['msg'].append(msg)
       #splitMeta(meta)
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

def getMsgTexts(chatData):
    text = ""
    for i in chatData:
        text = text + "\n" + i['msg']

    return text

if __name__ == "__main__":

    f = open(filename,'r')
    chat = parseData(f)
    text = getMsgTexts(chat)
    #for line in data['msg']:
    #    print(line)

    wordcloud = WordCloud().generate(text)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")

    wordcloud = WordCloud(max_font_size=40).generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    f.close()
