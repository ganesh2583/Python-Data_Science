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
allTweetsOnModi = api.search(tweetToBeSearched)

dataForCSV = [["Tweet", "Polarity", "Subjectivity"]]

# Loop through the tweets and get print the tweets
# and print the sentiment analysis
for tweetsOnModi in allTweetsOnModi:
    print(tweetsOnModi.text)
    analysis = TextBlob(tweetsOnModi.text)
    print(analysis.sentiment)
    csvEntry = [tweetsOnModi.text, analysis.sentiment.polarity, analysis.sentiment.subjectivity]
    dataForCSV.append(csvEntry)

myFile = open('twitterReport.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(dataForCSV)
print("Writing complete")
