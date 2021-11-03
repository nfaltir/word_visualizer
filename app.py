import matplotlib.pyplot as plt 
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import sys, os




os.chdir(sys.path[0])


#Read text

new_target = pd.read_csv(open('bill.pdf'))
print(new_target)
stopwords = STOPWORDS

#attributes
wc = WordCloud(
    background_color='#232323',
    stopwords=stopwords,
    height=1000,
    width=1000
)

#wc.generate(new_target)


#store to file
#wc.to_file('bill2.png')

