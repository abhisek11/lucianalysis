from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob


#---------------------------------------------------------------------------

consumer_key = 'AMskkMrTiil0Re1iKuJcQHseH'
consumer_secret = 'fZ0nOB4IqqYka7P70EAVkHkRFeFjTYXC1dIuUaWn3gF8YiCp9a'
access_token = '3135870607-MXL8UNUuZEWcgHE6wdN2kTYpqumiQWC5FVNpnUR'
access_token_secret = 'qMtb33qKZeGyMxqYJVICOjTYNuqZUOyhIlNBIlyrJWmOW'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#-------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    # t = [[]]
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    return jsonify({"success":True,"tweets":t})


#---------------------------------------------------------------------------


