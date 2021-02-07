"""
All time top posts on Reddit /r/Jokes.
The code is written by following the guide from https://www.storybench.org/how-to-scrape-reddit-with-python/
The description of columns can be found in https://github.com/reddit-archive/reddit/wiki/JSON
Note that Reddit has limit that praw cannot get submissions over 1,000 posts.
"""

# Import
import praw
import json

# Connect to Reddit
reddit = praw.Reddit(client_id="client_id",
                     client_secret="client_secret",
                     user_agent="user_agent",
                     username="username",
                     password="password")
subreddit = reddit.subreddit("Jokes")

# Get top 1000 of /r/Jokes
top_jokes = subreddit.top(limit=1000)

jokes_dict = { "title":[],
                "author":[],
                "score":[],
                "comms_num": [],
                "created": [],
                "over_18": [],
                "url": [],
                "body":[]}
for submission in top_jokes:
    jokes_dict["title"].append(submission.title)
    jokes_dict["author"].append(str(submission.author))
    jokes_dict["score"].append(submission.score)
    jokes_dict["comms_num"].append(submission.num_comments)
    jokes_dict["created"].append(submission.created)
    jokes_dict["over_18"].append(submission.over_18)
    jokes_dict["url"].append(submission.url)
    jokes_dict["body"].append(submission.selftext)

# Write in JSON
with open("top_reddit_joke.json", "w") as json_file:
    json.dump(jokes_dict, json_file)

