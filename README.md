This is a web application that displays a random (hard-coded) food item and generated related tweet!

<b>To use this repository, follow these steps:</b>

0. Sign up for a Twitter Developer's account at https://developer.twitter.com/

1. Create a new project on the Twitter Developer's portal

2. After creating a project, click on the key symbol to see your keys and tokens.

3. Sign up for Spoonacular's API at https://spoonacular.com/food-api/console

4. Click on your profile to view your API key

5. Clone this repository using the command 
<blockquote>git clone https://github.com/NJIT-CS490/project1-dmm77</blockquote>

6. Run the following commands to install Flask (https://flask.palletsprojects.com/) and Tweepy (https://www.tweepy.org/) 
<blockquote> [sudo] pip[3] install flask <br> [sudo] pip[3] install tweepy </blockquote>

7. Create a file called twitter.env at the root level and populate it as follows using the information from step 2
<blockquote>
export TWITTER_API_KEY="" <br>
export TWITTER_API_SECRET_KEY="" <br>
export TWITTER_ACCESS_TOKEN="" <br>
export TWITTER_ACCESS_TOKEN_SECRET=""
</blockquote>

8. Create a file called spoonacular.env at the root level and populate it as follows using the information from step 4
<blockquote>
export export SPOON_API_KEY=""
</blockquote>

9. Run the following commands to load the two previous files into your terminal 
<blockquote> 
source twitter.env <br>
source spoonacular.env
</blockquote>


10. Run the following command to launch your application
<blockquote> python main.py </blockquote>

<b>Problems I encountered and resolved:</b>

- I realized my application was not reading my CSS file at all. After researching online, I found out that with Flask you have to save your CSS files in a folder under the root directory named <i>static</i> and insert the line <i>app.static_folder = 'static'</i> in your main python application. The href link in your HTML file to your CSS file should be <i>"{{ url_for('static', filename='style.css') }}"</i> 
    <blockquote> https://stackoverflow.com/questions/13772884/css-problems-with-flask-web-app </blockquote>

- Using the Cloud9 interface, changes in my CSS file were not displaying when I refreshed the page. After talking to my peers, we realized this was caused by an issue with cache. To resolve this, simply hard refresh (SHIFT + CTRL + R) your webpage.

- I realized that only the first 140 characters of the tweet were being displayed when using the 'text' attribute associated with the Tweet object. After consulting Tweepy's docs, I realized I had to add the argument 'tweet_mode="extended"' in Cursor which returns Status objects; then, using the 'full_text' attribute associated with Status objects I was able to display the entire tweet.
    <blockquote> http://docs.tweepy.org/en/latest/extended_tweets.html </blockquote>

<b>Issues with the application:</b>

- Some tweets have an image/gif included and my application displays it as just a text link. I could parse the string and either use the link to display the actual image/gif or add a hyperlink.

- My application collects the 15 most recent tweets about the chosen food and randomly chooses from those. Collecting more tweets and having parameters to collect the most popular (and possibly relevant) tweets would add to randomization and help ensure that the chosen tweet is actually appropriate. This can be resolved by searching Tweepy docs for information on its search functions.

- I attemped to add a search bar so users could type in a food name and the related information would load. I kept getting "VFS connection does not exist issue". However, after this I manually reloaded the page using <i>Preview running application</i> and it would display it with the user's chosen food, but clearly it did not work with my form. If I had more time I could read more online about how AWS C9 works with redirecting URL's and using form variables with Flask.