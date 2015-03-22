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

    #Added--Monika
    #~ def on_connect(self):
        #~ print "Connection successfully established"
    def on_data(self, data):
        #print data
        #Added--Monika
        json_object = json.loads(data)
        print data
        #print self.json_object
        #print type(json_object)
        #print json_object
        #print json_object.keys()
        #return True #returning true means keep the connection alive and keep reading tweets, it prints tweets one by one
        return False

    def on_error(self, status):
        print "This is error:",status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OA(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    #Trying api
    #api=tweepy.API(auth)
    #api.update_s

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
   
    #stream.filter(track=['python', 'javascript', 'ruby'])
    #stream.filter(track=['yay', 'happy', 'glad','omg','Oh my god'])
    #stream.filter() #doesn't work
    stream.filter(follow=['60860629'],track=['#UFGrad','Ravi'],languages=['English'])
