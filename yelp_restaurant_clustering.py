from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts
import re
from nltk.corpus import stopwords
from collections import Counter


f = open('peterchang.txt', 'r')
text = f.read()
words = re.findall(r'\w+', text)
stops = set(stopwords.words("english")) 
stops2 = ['ve', 'get', 'came', 'didn', 'ever', 'never', 'though']
meaningful_words = [w for w in words if ((not w in stops) and (not w in stops2))]   
cap_words = [word.lower() for word in meaningful_words] 

word_counts = Counter(cap_words)
counts = dict(word_counts)
text = ''
for i in counts.keys():
    if counts[i] > 4:
        text = text + (' ' + i) * counts[i]



tags = make_tags(get_tag_counts(text), maxsize=120)
create_tag_image(tags, 'peterchang.png', size=(700, 700), fontname='Lobster')