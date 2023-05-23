
import pandas as pd
import praw
import snowflake.connector
from dotenv import load_dotenv
import os
from dotenv import load_dotenv
from snowflake.connector.pandas_tools import write_pandas
from inputoutput import imp_file,getdate,save_file
from textblob import TextBlob
load_dotenv()



snowflake_user = os.environ.get('snowflake_user')
snowflake_password = os.environ.get('snowflake_password')
snowflake_account = os.environ.get('snowflake_account')
snowflake_database = os.environ.get('snowflake_database')
snowflake_schema = os.environ.get('snowflake_schema')



# connect to Snowflake and create new table



direc = 'redditgold'
date = getdate()




def redditingesting():
    reddit = praw.Reddit(
        client_id='s4bVKgZTQc1EYQAHkVOlxw',
        client_secret='2-6qBlx60zvs3N38ND8MzDg8CXi2kg',
        user_agent='OptionNo3583',
    )

    # Specify the subreddit you want to search in
    subreddit = reddit.subreddit('all')  # You can change 'all' to a specific subreddit

    # Specify the keyword you want to search for in comments
    keyword = 'ChatGpt'

    # Fetch comments containing the keyword
    posts = subreddit.search(query=keyword, sort='top', time_filter='day', syntax='cloudsearch')

    df = pd.DataFrame(columns=['submission', 'source'])

    ## Submissions for the 
    for post in posts:
        new_row = {'submission':[post.title], 'source': ['Reddit']}
        new_df = pd.DataFrame(new_row)
        df = pd.concat([df, new_df], ignore_index=True)
    print(df)
    save_file('redditbronze',date,df)



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







def redditransfer():
    snowflake_conn = snowflake.connector.connect(
            user=snowflake_user,
            password=snowflake_password,
            account=snowflake_account,
            database=snowflake_database,
            schema=snowflake_schema
    )
    def perform_data_quality_check(df):
        # Data Completeness Check

        null_values = df.isnull()
        condition1 = null_values.any().any()

        print(condition1)
        duplicate_rows = df.duplicated(subset=['submission'])
        condition2 = duplicate_rows.any()
        print(condition2)

        if condition1:
            print("Warning: Missing values detected!")
        if condition2 :
            duplicate_rows = df.duplicated()
            print(df[duplicate_rows])
            print("Warning: Duplicate records detected!")
            df.drop_duplicates(inplace=True)
            print("Dropped Duplicates")

        if condition1:
            print("Data quality conditions not met. Snowflake table not updated.")
        else:
            #Write DataFrame to Snowflake table
            print(df)
            write_pandas(snowflake_conn,df,"REDDIT",quote_identifiers = False)
            print("Data loaded into Snowflake.")



    df = imp_file(direc,date)
    df.rename(columns={'date': 'INGESTDATE'}, inplace=True)
    print(df)

    # Loads if data quality tests are passed


    perform_data_quality_check(df)


    snowflake_conn.close()