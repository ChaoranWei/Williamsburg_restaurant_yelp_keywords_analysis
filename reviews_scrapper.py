import urllib2 
#from bs4 import BeautifulSoup
#import nltk
import re

def scrapper(url):
    html = urllib2.urlopen(url).read()#.decode('utf8')
    all =  re.compile('<p itemprop="description" lang="en">(.*?)</p>')
    all_date =  re.compile('<meta itemprop="datePublished" content="(.*?)">')
    
    #list = re.findall(all,html)
    #list2 = re.findall(all_date,html)
    List = zip(re.findall(all_date,html),re.findall(all,html))
    
    string = ' '.join([' '.join(i) for i in List])
    return string 

    
fil = open('peter_chang_date.txt', 'w')
String = ''
url = 'http://www.yelp.com/biz/peter-chang-williamsburg'
String += scrapper(url)
print(0)
for i in range(20, 20*5 + 1, 20):
    String += scrapper(url + '?start=' + str(i))

    print(i)

fil.write(String)
fil.close()