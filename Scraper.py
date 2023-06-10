# Imports
import praw
import pandas as pd
import datetime as dt

# Getting Reddit and subreddit instances.
reddit_authorized = praw.Reddit(client_id="",
                                client_secret="",
                                user_agent="",
                                username="",
                                password="")

# Suggest a subreddit based on console search.


def get_subreddit_suggestions(query):
    subreddits = reddit_authorized.subreddits.search(query, limit=5)
    suggestions = [subreddit.display_name for subreddit in subreddits]
    return suggestions


def main():
    query = input("Enter subreddit query: ")
    print("------------------------------")
    suggestions = get_subreddit_suggestions(query)
    # User will see a list if 5 subreddit's if search query does not exist.
    print("Suggestions:")
    print('\n'.join(suggestions))
    # User will enter final subreddit name based on suggestions.
    subreddit_name = input("Enter subreddit name: ")
    print("------------------------------")

    # Assign subreddit name to variable.
    subreddit = reddit_authorized.subreddit(subreddit_name)

    # Display subreddit name and title.
    # Basic information about the subreddit to check that we have access
    print("Subreddit Name:", subreddit.display_name)
    print("Subreddit Title:", subreddit.title)
    print("------------------------------")

    # Create dictionary of time options.
    time_options = {
        '1': 'hour',
        '2': 'day',
        '3': 'week',
        '4': 'month',
        '5': 'year',
        '6': 'all'
    }

    # Presents the time options to the user.
    print("Time Options:")
    for option, time_range in time_options.items():
        print(option, '-', time_range)

    # Prompts them to enter the desired time option.
    time_option = None
    while time_option not in time_options:
        time_option = input("Enter the desired time option: ")
        print("------------------------------")
        if time_option not in time_options:
            print("Invalid time option. Please try again.")
            print("------------------------------")

    time_range = time_options[time_option]

    # Get top 10 posts of subreddit.
    # Return a list-like object with the limit and time submission in a given subreddit.
    top_subreddit = subreddit.top(time_filter = time_range, limit=10)

    # Create dictionary to store the data.
    # Data includes post title, score, id, url, amount of comments, post creation date
    topics_dict = {
        "title": [],
        "score": [],
        "id": [],
        "url": [],
        "comms_num": [],
        "created": []
    }

    # Iterate through our top_subreddit object and append the info to our dictionary.
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

    # Print to console or CSV
    print(topics_data)
    # topics_data.to_csv('test.csv', index=False)


if __name__ == '__main__':
    main()
