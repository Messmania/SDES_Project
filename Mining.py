#For data mining of twitter data
import json

def addTweetToList():   
    #fh = open("twitter_streaming_data.json")
    tweet_list = []
    for line in open("twitter_streaming_data.json"):
        try:
            #print line
            #print "type of line:",type(line)
            tweet = json.loads(line)
            tweet_list.append(tweet)
        except:
            continue
    print "keys are:",tweet_list[0].keys() 
       
    print "Number of tweets are:",len(tweet_list)
    #call another function which takes this list as arg and processes! 
    countMax(tweet_list)

def countMax(x):
    """Counts the max number of tweets country wise for now"""
    print "In count max"
    print "first element is:",x[0],"of type",type(x[0])
    
if __name__=='__main__':
    addTweetToList()
#print type(tweets)
