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
    script, filename = argv
    f = open(filename,'r')
    chat = wap.parseData(f)
    text = wap.parseToString(chat)
    f.close()
    print("Parsing fertig")
    image_mask = np.array(Image.open("../MiningData/Soos.png"))
    wc = WordCloud(background_color = "white", max_words=2000, mask=image_mask,)
    wc.generate(text)
    plt.imshow(wc)
    print("fertig ")
    wc.to_file("../MiningData/output/word_cloud.png")
