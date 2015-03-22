import urllib
import json
import tweepy
#response=urllib.urlopen("https://twitter.com/search?q=%40twitterapi")
#print type(response)

twitter_datafile_path ="twitter_streaming_data.txt"
twitter_file = open(twitter_datafile_path)
twitter_data=[]
for line in twitter_file:
    try:
        tweet = json.loads(line)
        twitter_data.append(tweet)
    except:
        continue

print len(twitter_data)
