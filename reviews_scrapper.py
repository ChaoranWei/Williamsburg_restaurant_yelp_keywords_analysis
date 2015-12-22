import urllib2 
from bs4 import BeautifulSoup
import nltk
import re

def scrapper(url):
    html = urllib2.urlopen(url).read()#.decode('utf8')
    all =  re.compile('<p itemprop="description" lang="en">(.*?)</p>')
    
    list = re.findall(all,html)
    for e in range(0, 1):
        print list
    string = ''
    for e in list:
        
        string += e
    return string 

fil = open('peter_chang.txt', 'w')
String = ''
url = 'http://www.yelp.com/biz/peter-chang-williamsburg'
String += scrapper(url)
print(0)
for i in range(20, 101, 20):
    String += scrapper(url + '?start=' + str(i))
    print(i)

fil.write(String)
fil.close()