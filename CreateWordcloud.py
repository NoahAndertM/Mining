import pandas as pd
from PIL import Image
from os import path
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from sys import argv
import WhatsAppParser as wap

if __name__ == "__main__":

    print("Start")
    #script, filename, sendername = argv
    filename = argv[1]
    # TODO FIX sendername = "" if argv[2] == null else argv[2]

    f = open(filename,'r')
    chat = wap.parseData(f)
    text = wap.parseToString(chat, "Tobi")
    f.close()
    print("Parsing fertig")

    image_mask = np.array(Image.open("../MiningData/sora3.jpg"))
    wc = WordCloud(background_color = "white", max_words=2000, mask=image_mask,)
    wc.generate(text)
    wc.recolor(color_func=ImageColorGenerator(image_mask))

    plt.imshow(wc)
    print("fertig ")
    wc.to_file("../MiningData/output/word_cloud.png")
