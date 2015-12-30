from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts
import re
from nltk.corpus import stopwords
from collections import Counter



f = open('peter_chang_date.txt', 'r')
text = f.read()
words = re.findall(r'\w+', text)
lower_words = [word.lower() for word in words] 
stops = set(stopwords.words("english")) 
stops2 = ['ve', 'get', 'came', 'didn', 'ever', 'never', 'though', 'wasn','food','williamsburg','restaurant', 'br', '39','34', 'place','go','even']
meaningful_words = [w for w in lower_words if ((not w in stops) and (not w in stops2))]   


word_counts = Counter(meaningful_words)
counts = dict(word_counts)
text = ''
for i in counts.keys():
    text = text + (' ' + i) * (counts[i])
#food for thought: 60, 10, 90


tags = make_tags(get_tag_counts(text)[:50], maxsize=100)
create_tag_image(tags, 'peter_chang.png', size=(900, 700), fontname = 'Lobster')
