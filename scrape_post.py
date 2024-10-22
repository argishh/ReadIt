import praw
import pandas as pd
import os
from streamlit import secrets
from dotenv import load_dotenv

# Loading all environmenmt variables
load_dotenv()
 
# ------------------------- Configuring PRAW ------------------------- 
client_id = os.getenv("REDDIT_CLIENT_ID")
client_secret = os.getenv("REDDIT_CLIENT_SECRET")
# client_id = secrets["REDDIT_CLIENT_ID"]
# client_secret = secrets["REDDIT_CLIENT_SECRET"]
user_agent = 'webapp:ReadIt:v1.0.0 (by u/venizonen)'

# Set up the Reddit instance
reddit = praw.Reddit(client_id=client_id, 
                     client_secret=client_secret, 
                     user_agent=user_agent)


# ------------------------- Defining Functions ------------------------- 
def fetch_comments(reddit_url, limit=10):
    # Get the submission from the URL
    submission = reddit.submission(url=reddit_url)
    
    # Fetch top comments
    submission.comments.replace_more(limit=0)
    comments = submission.comments.list()
    
    # Collect comments in a DataFrame
    comment_data = []
    for comment in comments[:limit]:
        comment_data.append([comment.body, comment.score])
    
    comments_df = pd.DataFrame(comment_data, columns=['Comment', 'Score'])
    comments_df = comments_df.sort_values(by='Score', ascending=False).reset_index(drop=True)

    return comments_df['Comment']


# ------------------------------ Example ------------------------------ 
# reddit_url = "https://www.reddit.com/r/csMajors/comments/1g8wroy/in_which_language_i_should_do_dsa/"
# comments_df = fetch_comments(reddit_url, limit=20)
# print(comments_df)
