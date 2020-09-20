from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import sys
import os
import flask
import random

api_key = os.environ["TWITTER_API_KEY"]
api_secret = os.environ["TWITTER_API_SECRET_KEY"]
access_token = os.environ["TWITTER_ACCESS_TOKEN"]
access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

auth = OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)
    
app = flask.Flask(__name__)

app.static_folder = 'static'


@app.route('/')
def index():
    
    foods = ["poke bowl", "ice cream cake", "eggplant parmesean", "fondant potatoes", "chole channa", "mushroom burger", "pizza"]
    chosen_food = random.choice(foods)
    
    searched_tweets = []
    for tweet in Cursor(auth_api.search, q=chosen_food, lang="en", tweet_mode="extended").items(15):
        searched_tweets.append(tweet)
        
    chosen_tweet = searched_tweets[ random.randint(0,14) ]
    
    return flask.render_template(
        "index.html", 
        food = chosen_food,
        tweet = chosen_tweet.full_text,
        tweet_author = chosen_tweet.user.screen_name,
        tweet_time = chosen_tweet.created_at,
    )

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)