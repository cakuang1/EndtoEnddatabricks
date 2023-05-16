"""

Ingests data from google news api. Looks for recent articles about ChatGPT for the day,and extractts the text. Then loads it into a textfile.


"""






import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()


today = datetime.now().date()
# Subtract one day to get the date before today
yesterday = today - timedelta(days=1)
wordparameter= 'ChatGpt'
languageparameter = 'en'
dateparameter = yesterday.strftime('%Y-%m-%d')
keyparameter = os.environ.get('GOOGLENEWSAPI')
print(keyparameter)

# Sends a GET request to the API endi point with the parameters 
response = requests.get(f'https://newsapi.org/v2/everything?q={wordparameter}&language={languageparameter}&from={dateparameter}&sortBy=popularity&apiKey={keyparameter}')




for articles in response.json()['articles']:
    r=requests.get(articles['url'])
    r.encoding = 'utf-8'
    html = r.text
    soup = BeautifulSoup(html)
    text = soup.get_text()
    clean_text= text.replace("n", " ")
    clean_text= clean_text.replace("/", " ") 












    

    



















