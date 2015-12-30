from images2gif import writeGif
from PIL import Image, ImageSequence
import sys, os
from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts
import re
from nltk.corpus import stopwords
from collections import Counter


def get_image(text, image):
    tags = make_tags(get_tag_counts(text)[:50], maxsize=100)
    create_tag_image(tags, image, size=(900, 700), fontname = 'Lobster') 
    
def preprocessing(text, year):
    words = re.findall(r'\w+', text)
    lower_words = [word.lower() for word in words] 
    stops = set(stopwords.words("english")) 
    stops2 = ['ve', 'get', 'came', 'didn', 'ever', 'never', 'though', 'wasn','food','williamsburg','restaurant', 'br', '39','34', 'place','go','even', '2015','2014','2013','2012','2011','2010','2009','2008','2007','2006','2005','2004']
    meaningful_words = [w for w in lower_words if ((not w in stops) and (not w in stops2))]   
    
    
    word_counts = Counter(meaningful_words)
    counts = dict(word_counts)
    most_common,num_most_common = word_counts.most_common(1)[0]
    
    text = ''
    for i in counts.keys():
        text = text + (' ' + i) * (counts[i])    
    text += (' ' + str(year)) * (num_most_common)    
    return text

f = open('peter_chang_date.txt', 'r')
text = f.read()

im = []
for i in range(int(text[:4]), 2004, -1): #yelp was founded in 2004
    if str(i) in text:
        temp = text.split(str(i -1))[0]
        text = text[len(temp) - 1:]
        get_image(preprocessing(temp, i), str(i) + '.png')
        im.append(Image.open(str(i) + '.png'))
    

im = [i.resize([650,650], Image.ANTIALIAS) for i in im]

writeGif('peter_chang.gif', im, duration=1.2)

