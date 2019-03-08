from sys import argv
from wordcloud import WordCloud
import matplotlib.pyplot as plt

script, filename = argv
data = {'date':[],'sender':[], 'msg':[]}

def splitData(f):
    text = ""
    for line in f:
     try:
      splitted = line.split(': ')
      meta = splitted[0]
      msg = splitted[1]
      if('Medien' not in msg): # If any form of media is sent, WhatsApp prints "<Media Omitted>". Getting rid of this. TO DO: Improve this functionality.
       text = text + "\n" + msg
       data['msg'].append(msg)
       splitMeta(meta)
     except:
         pass
    return text

def splitMeta(m):
    try:
        splitted = m.split(" - ")
        date = splitted[0]
        sender = splitted[1]
        data['date'].append(date)
        data['sender'].append(sender)
    except:
        print("Ups")

if __name__ == "__main__":

    f = open(filename,'r')
    text = splitData(f)

    for line in data['msg']:
        print(line)

    wordcloud = WordCloud().generate(text)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")

    wordcloud = WordCloud(max_font_size=40).generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    f.close()
