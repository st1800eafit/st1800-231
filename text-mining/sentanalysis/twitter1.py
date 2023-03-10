# Import the libraries
# pip install tweepy, textblob, wordcloud
#
import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

consumerKey = ""
consumerSecret = ""
accessToken = ""
accessTokenSecret = ""

# Create the authentication object
authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret)

# Set the access token and access token secret
authenticate.set_access_token(accessToken, accessTokenSecret)

# Creating the API object while passing in auth information
api = tweepy.API(authenticate, wait_on_rate_limit=True)

# Extract 100 tweets from the twitter user
posts = api.user_timeline(screen_name="eafit",count=100, lang="sp", tweet_mode="extended")

#  Print the last 5 tweets
print("Show the 5 recent tweets:\n")
i = 1
for tweet in posts[:5]:
    print(str(i) + ') ' + tweet.full_text + '\n')
    i = i+1
