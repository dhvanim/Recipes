from tweepy import OAuthHandler
from tweepy import API
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
    return flask.render_template(
        "index.html", 
    )

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)