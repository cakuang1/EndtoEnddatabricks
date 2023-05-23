
from dotenv import load_dotenv
import pandas as pd
from inputoutput import imp_file,getdate,save_file
from textblob import TextBlob





def reddittransform():
    dirname = 'redditbronze'
    date = getdate()
    df = imp_file(dirname,date)

    #Create a function to get the subjectivity
    def getSubjectivity(text):
        return TextBlob(text).sentiment.subjectivity
    #Create a function to get Polarity
    def getPolarity(text):
        return TextBlob(text).sentiment.polarity


    df['Subjectivity'] = df['submission'].apply(getSubjectivity)
    df['Polarity'] = df['submission'].apply(getPolarity)
    df['date'] = date


    save_file('redditgold',date,df)

    return





