import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import pandas as pd
from inputoutput import imp_file,getdate,save_file
from textblob import TextBlob






dirname = 'redditbronze'
date = getdate()
df = imp_file(dirname,date)

#Create a function to get the subjectivity
def getSubjectivity(text):
 return TextBlob(text).sentiment.subjectivity
#Create a function to get Polarity
def getPolarity(text):
 return TextBlob(text).sentiment.polarity


df['Subjectivity'] = df['headline'].apply(getSubjectivity)
df['Polarity'] = df['headline'].apply(getPolarity)
df['date'] = date

save_file('newgold',date,df)




