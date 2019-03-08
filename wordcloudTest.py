import pandas as pd
from PIL import Image
from os import path
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

chat = pd.read_csv('chatLogLr.txt',
sep=r'[0-9] -', names=['time', 'message'])
