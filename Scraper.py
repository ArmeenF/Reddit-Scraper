# Imports
import praw
import pandas as pd
import datetime as dt

# Auth Variables


# Getting Reddit and subreddit instances.
reddit = praw.Reddit(client_id='PERSONAL_USE_SCRIPT_14_CHARS',
                     client_secret='SECRET_KEY_27_CHARS ',
                     user_agent='YOUR_APP_NAME',
                     username='YOUR_REDDIT_USER_NAME',
                     password='YOUR_REDDIT_LOGIN_PASSWORD')

# Assign subreddit name to variable.
subreddit = reddit_authorized.subreddit('Superstonk')

# Basic information about the subreddit to check that we have access.
print("Display Name:", subreddit.display_name)
print("Title:", subreddit.title)
# print("Description:", subreddit.description)

# Will return a list-like object with the limit submission in a given subreddit.
top_subreddit = subreddit.top(limit=10)

# Create dictionary to store the data.
topics_dict = {"title": [],
               "score": [],
               "id": [], "url": [],
               "comms_num": [],
               "created": []}

# Iterate through our top_subreddit object and append the information to our dictionary.
for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)

# Create Data Frame
topics_data = pd.DataFrame(topics_dict)

# Function to get post date


def get_date(created):
    return dt.datetime.fromtimestamp(created)


_timestamp = topics_data["created"].apply(get_date)

topics_data = topics_data.assign(timestamp=_timestamp)

# Print
# print(topics_data)
topics_data.to_csv('test.csv', index=False)
