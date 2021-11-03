import requests
import pandas as pd

url = "https://www.reddit.com/r/wallstreetbets/" #fix link
resp = requests.get(url)

df = pd.read_html(url)
print(df)