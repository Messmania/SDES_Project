from tweepy.streaming import StreamListener
from tweepy import OAuthHandler as OA
from tweepy import Stream
import json

#Variables that contains the user credentials to access Twitter API 
access_token = "60860629-uBPHcQkeXOZa2TWVPUetNmq4IGX44aIdt93pWZMk4"
access_token_secret = "rrJp4rUixyWwI6xp9QC85GJNjZdYkVlTSLrxpbFa1EHt7"
consumer_key = "RyT3d9Pco5KYrcX5Figq9uBoY"
consumer_secret = "m5zUdszvur2reYdFFfoZjNypkuNj7tkhIQA6ovga0QiUrAVS5h"


"""This is a basic listener that just prints received tweets to stdout"""

class StdOutListener(StreamListener): #this means it is inheriting from class StreamListener
  
    def on_data(self,data):
        """for dumping tweets which are not the deleted ones"""
        if 'delete' not in data:
            print data
        return True

    def on_error(self, status):
        print "This is error:",status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OA(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    
    stream.filter(languages=["en"], locations=[-120,30,-70,50], track= ["a","an","the","i","you","u"])  
	#longitude:120W-70W and latitude:30N-50N
    #stream.sample() #works: collects tweets

