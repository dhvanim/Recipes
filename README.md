This is a web application that displays a random (hard-coded) food item and generated related tweet!

To use this repository, follow these steps:

0. Sign up for a Twitter Developer's account at https://developer.twitter.com/
1. Create a new project on the Twitter Developer's portal
2. After creating a project, click on the key symbol to see your keys and tokens.
3. Clone this repository using the command 
    'git clone https://github.com/NJIT-CS490/project1-dmm77'
4. Run the following commands to install Flask (https://flask.palletsprojects.com/) and Tweepy (https://www.tweepy.org/)
    '[sudo] pip[3] install flask'
    '[sudo] pip[3] install tweepy'
5. Create a file called twitter.env at the root level and populate it as follows using the information from step 2
    export TWITTER_API_KEY=""
    export TWITTER_API_SECRET_KEY=""
    export TWITTER_ACCESS_TOKEN=""
    export TWITTER_ACCESS_TOKEN_SECRET=""
6. Run the following command to load the previous file into your terminal
    'source twitter.env'
7. Run the following command to launch your application
    'python main.py'

Problems I encountered and resolved:

- Using the Cloud9 interface, changes in my CSS file were not displaying when I refreshed the page. After talking to my peers, we realized this was caused by an issue with cache. To resolve this, simply hard refresh (SHIFT + CTRL + R) your webpage.
- I realized that only the first 140 characters of the tweet were being displayed when using the 'text' attribute associated with the Tweet object. After consulting Tweepy's docs, I realized I had to add the argument 'tweet_mode="extended"' in Cursor which returns Status objects; then, using the 'full_text' attribute associated with Status objects I was able to display the entire tweet.

