import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
from wordcloud import STOPWORDS
import matplotlib.pylab as plt

base_domain = 'https://dblp.uni-trier.de/db/conf/sp/'
#version_1.0 support S&P only

def get_res(Conferences,tp,year):
    #Conferences is a palceholder
    #sp is Conferences or Workshops
    #year
    print "Connecting to the website"
    if(tp=='sp'):
        target = base_domain + 'sp' + str(year) + '.html'
    else:
        target = base_domain + 'spw' +str(yaer) + '.html'
    try:
        r = requests.get(target)
    except:
        print('can not connect to the target website,please cheek the connection')
    return r

def cook_soup(res):
    #res from request
    soup = BeautifulSoup(res.text)
    artical_list = soup.find_all(class_='title',itemprop='name')
    word_list = []
    for i in artical_list:
        word_list.append(i.string.split(' '))
    l = [n for a in word_list for n in a ]
    s = ' '.join(l)
    return s
sw = set(STOPWORDS)
sw.add("Security")
sw.add("Secure")
sw.add("Using")
sw.add("Without")
sw.add("End")
sw.add("Two")
sw.add("Via")
sw.add("Based")
def draw_wordcloud(s):
    # lower max_font_size
    wordcloud = WordCloud(stopwords=sw,max_font_size=40).generate(s)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
r = get_res(0,'sp',2018)
s = cook_soup(r)
draw_wordcloud(s)


