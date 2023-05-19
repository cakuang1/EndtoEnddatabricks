"""

Extracts all comments with the word "ChatGpt" of the current day. This


"""




import os
from dotenv import load_dotenv
import pandas as pd
from inputoutput import save_file,getdate
import praw

dateparameter = getdate()

def re():
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
    save_file('redditbronze',dateparameter,df)








