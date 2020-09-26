from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import sys
import os
import flask
import random
import requests

spoon_api = os.environ["SPOON_API_KEY"]

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
    
    foods = ["Ice Cream Cake", "Eggplant Parmesan", "Potato", "Mushroom Burger", "Ratatouille"]
    chosen_food = random.choice(foods)
    
    print(chosen_food)
    
    searched_tweets = []
    for tweet in Cursor(auth_api.search, q=chosen_food, lang="en", tweet_mode="extended").items(15):
        searched_tweets.append(tweet)
        
    chosen_tweet = random.choice(searched_tweets)
    
    # request recipe based on chosen food
    get_recipe = "https://api.spoonacular.com/recipes/complexSearch"
    r_conditions = {"query" : chosen_food, "addRecipeInformation" : "true", "number" : "1", "apiKey" : spoon_api}
    recipe_response = requests.get(get_recipe, params = r_conditions)
    
    recipe_info = recipe_response.json()

    # get recipe name, id, url, image
    recipe_name = recipe_info["results"][0]["title"]
    recipe_id = recipe_info["results"][0]["id"]
    recipe_url = recipe_info["results"][0]["sourceUrl"]
    recipe_image = recipe_info["results"][0]["image"]
    
    # use recipe id to get ingredient information
    get_ingredients = "https://api.spoonacular.com/recipes/" + str(recipe_id) + "/ingredientWidget.json"
    i_conditions = {"apiKey":spoon_api}
    ingredients_response = requests.get(get_ingredients, params = i_conditions)
   
    ingredients_info = ingredients_response.json()
    
    # iterate through ingredients response and compile in list
    ingredients_list = []
    for ingredient in ingredients_info["ingredients"]:
        name = ingredient["name"]
        amount = ingredient["amount"]["us"]["value"] 
        unit = ingredient["amount"]["us"]["unit"]
        
        item = str(amount) + " " + unit + " " + name 
        ingredients_list.append( item )
    
    # for later
    '''
    # iterate through recipe steps and compile in list
    steps_list = []
    steps_info = recipe_info["results"][0]["analyzedInstructions"]["steps"]
    for step in steps_info:
     
    '''   
    
    return flask.render_template(
        "index.html", 
        tweet = chosen_tweet.full_text,
        tweet_author = chosen_tweet.user.screen_name,
        tweet_time = chosen_tweet.created_at,
        
        recipe_name = recipe_name,
        recipe_image = recipe_image,
        recipe_url = recipe_url,
        ingredients = ingredients_list
    )

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)