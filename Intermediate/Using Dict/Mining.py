#For data mining of twitter data
import json
import pandas as pd
import sys

def addTweetToList():
    """for constructing a list out of multiple json objects in a file""" 
    try:
        #print len(sys.argv),sys.argv[0]
        if len(sys.argv)<=1:
            raise ValueError   
        filename = sys.argv[1]
        tweet_list = []
        ""
        for line in open(filename):
            try:
                #print line
                #print "type of line:",type(line)
                tweet = json.loads(line)
                tweet_list.append(tweet)
            except:
                continue
        #listTypes(tweet_list)        
        print "keys are:",tweet_list[0].keys()
        filterBy(tweet_list) 
           
        #print "Number of tweets are:",len(tweet_list)
        #call another function which takes this list as arg and processes! 
        countMax(tweet_list)
    except ValueError:
        print "Please enter a filename to be read (should be a json file)"


def listTypes(tweet_list):
    """finding the types of all list elements, prepares a list of all the elements of a tweet which are dict"""
    
    print "List index:Type"
    for tweet in range(0,len(tweet_list)):
        #print tweet,type(tweet_list[tweet])
        #each value is checked if it is a dict
        for key,value in tweet_list[tweet].iteritems():
            if type(value)==dict:
                print key,
                
        print " "
    
        
def countMax(x):
    """Counts the max number of tweets country wise for now"""
    #print "In count max"
    #print "first element is:",x[0],"of type",type(x[0])
    

def filterBy(tweet_list):
    tweets = pd.DataFrame()
    tweets['text'] = map(lambda tweet: tweet['text'], tweet_list)
    tweets['lang'] = map(lambda tweet: tweet['lang'] if tweet['lang']=='en' else None, tweet_list)
    tweets['country'] = map(lambda tweet:tweet['place']['country'] if tweet['place']!=None else None, tweet_list)
    print tweets
    
    
if __name__=='__main__':
    addTweetToList()
#print type(tweets)



