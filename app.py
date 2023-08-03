import streamlit as st
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

st.markdown('<h1 style="text-align:center; margin-bottom: 30px; letter-spacing:5px; font-size:70px;">Word Cloud 🧩</h1>', unsafe_allow_html=True)
st.markdown('<hr>', unsafe_allow_html=True)
st.set_option('deprecation.showPyplotGlobalUse', False)
user_input = st.text_area("Paste or enter texts here 👇")

stopwords = STOPWORDS
# Create a list of themes
#themes = ['autumn', 'candy', 'dark', 'default', 'grayscale', 'light', 'random', 'solarized']
# Get the selected theme
theme = ['Pastel1',
        'Pastel2',
        'Paired',
        'Accent',
        'Dark2',
        'Set1',
        'Set2',
        'Set3',
        'tab10',
        'tab20',
        'tab20b',
        'tab20c'
]
# Create a dropdown menu to select the theme


st.button('visualize')
theme_selector = st.selectbox('Select a theme', theme)

try:
    wordcloud = WordCloud(background_color='#232323',  stopwords=stopwords, height=1000, width=1000, colormap=theme_selector).generate(user_input)
    #Display the generated image:
    plt.figure(dpi=600)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    #plt.show()
    plt.tight_layout()
    st.pyplot()
    
except ValueError:
    st.write('')




