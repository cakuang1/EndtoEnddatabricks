"""

Ingests data from google news api. Looks for recent articles about ChatGPT for the day,and extractts the text. Then loads it into a textfile.

"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import pandas as pd
from inputoutput import save_file


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



df = pd.DataFrame(columns=['headline', 'source'])

for articles in response.json()['articles']:
    new_row = {'headline':[ articles['title']], 'source': ['Google News']}
    new_df = pd.DataFrame(new_row)
    df = pd.concat([df, new_df], ignore_index=True)





save_file('newbronze',dateparameter,df)












    


















































    

    



















