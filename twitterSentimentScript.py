import sys
import csv
import tweepy
from textblob import TextBlob

# Read the argument. This will the twitter search word
tweetToBeSearched=sys.argv[1]

# Twitter app Consumer Key and Consumer Secret
consumer_key = 'RPbZlqCZUrYwP6t1FIrI5hvfb'
consumer_secret = 'wF37kEMfLJmqKlmpMwQ9f5KbP51Us9ycGApJYpjg9ceKaZBQ8T'

# Twitter app access token and access token key
access_token = '129485220-OhrYwXuoQSJ8mDSAUodtYk0L39iUej9t4yQUD6iy'
access_token_secret = 'AX87fbX8nygeanLaRQDLQCI61xckUoEaLlRY8CbmdFRpM'

# Perform Auth to twitter app created using the keys mentioned above
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Access the twitter API
api = tweepy.API(auth);

# Search for a tweet
allTweets = api.search(tweetToBeSearched, count=150)

dataForCSV = [["Tweet", "Result", "Subjectivity"]]

# Loop through the tweets and get print the tweets
# and print the sentiment analysis
for tweet in allTweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    analysis.tags
    if analysis.sentiment.polarity > 0:
        csvEntry = [tweet.text, "Positive", analysis.sentiment.subjectivity]
    else:
        csvEntry = [tweet.text, "Negetive", analysis.sentiment.subjectivity]
    print(analysis.sentiment)
    dataForCSV.append(csvEntry)

myFile = open('twitterReport.csv', 'w', encoding='utf-8')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(dataForCSV)
print("Writing complete")
