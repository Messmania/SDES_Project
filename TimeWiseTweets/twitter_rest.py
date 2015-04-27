from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import time

access_token = "60860629-uBPHcQkeXOZa2TWVPUetNmq4IGX44aIdt93pWZMk4"
access_token_secret = "rrJp4rUixyWwI6xp9QC85GJNjZdYkVlTSLrxpbFa1EHt7"
consumer_key = "RyT3d9Pco5KYrcX5Figq9uBoY"
consumer_secret = "m5zUdszvur2reYdFFfoZjNypkuNj7tkhIQA6ovga0QiUrAVS5h"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

count=0
morningTweets=[]
eveningTweets=[]
nightTweets=[]
afternoonTweets=[]
loc1=[-111.05,41,-104.05,45]
c = tweepy.Cursor(api.search,q='test',include_entities=True).items()
#for tweet in tweepy.Cursor(api.search,q='test',lang='en',locations=[-111.05,41,-104.05,45]).items():
mT = open('morningTweets.txt','w')
aT = open('afternoonTweets.txt','w')
eT = open('eveningTweets.txt','w')
nT = open('nightTweets.txt','w')
while True:
    if count >200:
        break
    else:
        tweet = c.next()
        count+=1
        twt = tweet.text
        #print twt
        creationTime = tweet.created_at
        #print "===Creation====:",creationTime
        hr = creationTime.hour
        #print hr
        #print type(creationTime)
        
        if hr in range(0,12):
            morningTweets.append(twt)           
        elif hr in range(12,16):
            afternoonTweets.append(twt)            
        elif hr in range(16,20):
            eveningTweets.append(twt)            
        elif hr in range(20,24):
            nightTweets.append(twt)
           
            
print "Morning:",len(morningTweets)

print "Evening:",len(eveningTweets)
print "Night:",len(nightTweets)
print "Afternoon:",len(afternoonTweets)

mT.write(morningTweets)
aT.write(afternoonTweets)
eT.write(eveningTweets)
nT.write(nightTweets)

mT.close()
aT.close()
eT.close()
nT.close()
