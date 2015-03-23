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
        print "keys are:",tweet_list[0].keys() 
           
        print "Number of tweets are:",len(tweet_list)
        #call another function which takes this list as arg and processes! 
        countMax(tweet_list)
    except ValueError:
        print "Please enter a filename to be read (should be a json file)"

def countMax(x):
    """Counts the max number of tweets country wise for now"""
    print "In count max"
    print "first element is:",x[0],"of type",type(x[0])
    
    
if __name__=='__main__':
    addTweetToList()
#print type(tweets)
