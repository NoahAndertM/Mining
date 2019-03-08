import CreateWordcloud
from WhatsAppParser import WaParser
import argparse
import CreateWordcloud as cw

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Creates a Neat little Word cloud from Whatsapp Chatlogs')
    parser.add_argument('Source', metavar="S", help="The source Whatsapplog .txt file")
    parser.add_argument('-Image', metavar="I", help="The Image Mask")
    #parser.add_argument('-Sender', metavar="s", help="filters text for Sender")
    #parser.add_argument('-Destination', metavar="D", help="The destination File")
    #parser.add_argument('-show', metavar="sh", help="Defines wether or not the Wordcloud should be shown after creation", type=bool)
    #parser.add_argument('-MaxWords', metavar="M", help="Defines the Word Limit", type=int)
    #parser.add_argument('-BGcolor', metavar="B", help="Defines the background color")

    args = parser.parse_args()
    filename = args.Source
    f = open(filename,'r')
    parser = WaParser(f)
    f.close()

    text = parser.parseToString()
    print("Parsing fertig")

    cw.createWordcloud(text,image=args.Image)
