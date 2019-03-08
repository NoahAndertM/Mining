import pandas as pd
from PIL import Image
from os import path
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from sys import argv
from WhatsAppParser import WaParser

def createWordcloud(text, image="", dest="wordcloud.png",
show=False, maxWords=2000, bgColor="white"):
    if(image==""):
        wc = WordCloud(background_color = bgColor, max_words=maxWords)
        wc.generate(text)
    else:
        image_mask = np.array(Image.open(image))
        wc = WordCloud(background_color = "white", max_words=2000, mask=image_mask)
        wc.generate(text)
        wc.recolor(color_func=ImageColorGenerator(image_mask))
    if(show): plt.imshow(wc)
    wc.to_file(dest)


if __name__ == "__main__":

    print("Start")
    #script, filename, sendername = argv
    filename = argv[1]
    # TODO optionale CIL Arguments

    f = open(filename,'r')
    parser = WaParser(f)
    text = parser.parseToString()
    f.close()
    print("Parsing fertig")

    createWordcloud(text, image="../MiningData/Soos.png", show=True)
