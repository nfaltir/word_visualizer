import streamlit as st
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

st.markdown('<h1 style="text-align:center; margin-bottom: 30px;">Visualizing Words 🧩</h1>', unsafe_allow_html=True)
st.markdown('<hr>', unsafe_allow_html=True)
st.write('A simple python application that takes a collection of words and returns the most used words')

st.set_option('deprecation.showPyplotGlobalUse', False)
# Create some sample text
user_input = st.text_area("text(s) goes in here 👇")
st.button('visualize')

stopwords = STOPWORDS

try:
    wordcloud = WordCloud(background_color='#232323',  stopwords=stopwords, height=1000, width=1000).generate(user_input)
    #Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    st.pyplot()
except ValueError:
    st.write('')


# Create and generate a word cloud image:



