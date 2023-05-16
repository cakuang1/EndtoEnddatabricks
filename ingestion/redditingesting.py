"""

Extracts all comments with the word "ChatGpt" of the current day. This


"""


import praw

# Authenticate with your Reddit app credentials
reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    user_agent='YOUR_USER_AGENT',
)

# Specify the subreddit you want to search in
subreddit = reddit.subreddit('all')  # You can change 'all' to a specific subreddit

# Specify the keyword you want to search for in comments
keyword = 'YOUR_KEYWORD'

# Fetch comments containing the keyword
comments = subreddit.comments(limit=100)  # Adjust the limit as per your requirements

# Iterate through the comments and print the ones containing the keyword
for comment in comments:
    if keyword in comment.body:
        print(comment.body)
        print('---')