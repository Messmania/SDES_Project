import tweepy
 
# Consumer keys and access tokens, used for OAuth
access_token = "60860629-uBPHcQkeXOZa2TWVPUetNmq4IGX44aIdt93pWZMk4"
access_token_secret = "rrJp4rUixyWwI6xp9QC85GJNjZdYkVlTSLrxpbFa1EHt7"
consumer_key = "RyT3d9Pco5KYrcX5Figq9uBoY"
consumer_secret = "m5zUdszvur2reYdFFfoZjNypkuNj7tkhIQA6ovga0QiUrAVS5h"
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
 
# Sample method, used to update a status
#api.update_status('Hello Python Central!')
