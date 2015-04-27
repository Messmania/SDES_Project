#For data mining of twitter data :Sentiment Analyses
import json
import pandas as pd
import sys
import re
import matplotlib.pyplot as plt
import csv
import nltk
#import regex #to eliminate username and replace with AT_USER

#global featureList
#featureList = []


#make list of tweets
def addTweetToList(x):
	"""for constructing a list out of multiple json objects in a file""" 
	try:
		
		#if len(sys.argv)<=1:
		#    raise ValueError  
 
		#filename = sys.argv[1]
		filename = x  		
		tweet_list = []
		""
		for line in open(filename):
		    try:

			tweet = json.loads(line)
			tweet_list.append(tweet)
		    except:
			continue 
		   
		print "Number of tweets are:",len(tweet_list)
		
		return tweet_list

	except ValueError:
		print "Please enter a filename to be read (should be a json file)"
 

#start process_tweet--->Returns processed tweets

def processTweet(tweet):
	# process the tweets

	#Convert to lower case
	tweet = tweet.lower()
	#Convert www.* or https?://* to URL
	tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
	#Convert @username to AT_USER
	tweet = re.sub('@[^\s]+','AT_USER',tweet)
	#Remove additional white spaces
	tweet = re.sub('[\s]+', ' ', tweet)
	#Replace #word with word; remove hash 
	tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
	#look for 2 or more repetitions of character and replace with the character itself
	pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
	tweet = pattern.sub(r"\1\1", tweet)
	#trim
	tweet = tweet.strip('\'"')
	return tweet
#end

#Read the tweets one by one and process it
#fp = open('data/sampleTweets.txt', 'r')
#line = fp.readline()

#if __name__ == '__main__':

#while line:
#    processedTweet = processTweet(line)
#    print processedTweet
#    line = fp.readline()
##end loop
#fp.close()



##start replaceTwoOrMore
#def replaceTwoOrMore(s):
#    #look for 2 or more repetitions of character and replace with the character itself
#    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
#    return pattern.sub(r"\1\1", s)
##end



#start getStopWordList
def getStopWordList(stopWordListFileName):
	#initialize stopWords
	stopWords = []
	#read the stopwords file and build a list
	stopWords = []
	stopWords.append('AT_USER')
	stopWords.append('URL')

	fp = open(stopWordListFileName, 'r')
	line = fp.readline()
	while line:
		word = line.strip()
		stopWords.append(word)
		line = fp.readline()
	fp.close()
	return stopWords
#end

#start getfeatureVector
def getFeatureVector(processedTweet,stopWords):
    featureVector = []
    #split tweet into words
    words = processedTweet.split()
    for w in words:
        #strip punctuation
        w = w.strip('\'"?,.')
        #check if the word starts with an alphabet
        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
        #ignore if it is a stop word
        if(w in stopWords or val is None):
            continue
        else:
            featureVector.append(w.lower())
    return featureVector
#end

##Read the tweets one by one and process it
#fp = open('data/sampleTweets.txt', 'r')
#line = fp.readline()

#st = open('data/feature_list/stopwords.txt', 'r')
#stopWords = getStopWordList('data/feature_list/stopwords.txt')

#while line:
#    processedTweet = processTweet(line)
#    featureVector = getFeatureVector(processedTweet)
#    print featureVector
#    line = fp.readline()
##end loop
#fp.close()

def getFeatureList(SampleCsvFile,stopWords):

	global featureList
	inpTweets = csv.reader(open(SampleCsvFile, 'rb'), delimiter=',', quotechar='|')

	# Get tweet words
	tweets = []
	for row in inpTweets:
		sentiment = row[0]
		tweet = row[1]
		processedTweet = processTweet(tweet)
		featureVector = getFeatureVector(processedTweet, stopWords)
		featureList.extend(featureVector)
		tweets.append((featureVector, sentiment));
	#end loop

	# Remove featureList duplicates
	featureList = list(set(featureList))
	return tweets


#start extract_features
def extract_features(tweet):
	global featureList

	tweet_words = set(tweet)
	features = {}
	for word in featureList:
		features['contains(%s)' % word] = (word in tweet_words)
	return features
#end

    
if __name__=='__main__':

	global featureList
	featureList = []
	
	###########################################################################
	#definition and declaration part

	#list contains all the tweets corresponding data
	processed_tweet_list = []
	feature_vector_list = []
	extracted_feature_list = []

	extracted_feature_dict = {} # individual tweet features

	#files to store corresponding data of individual tweets
	proc_tweet = open('proc_tweet.txt','w')
	feature_vector = open('feature_vector.txt','w')
	extracted_feature = open('extracted_feature.txt','w')
	tweet_sentiment = open('tweet_sentiment','w')


	###########################################################################
	#program to write the training set

	#Stop Words collection in the list
	stopWords = getStopWordList('stopwords.txt')

	#get feature list stored in a file (for reuse)
	#featureList is update according to training set and returns 
	#returns list of tuples of tweet_feature_word and corresponding sentiment
	training_tweets = getFeatureList('sampletweets.csv',stopWords)
	
	
	# Extract feature vector for all tweets in one shote
	training_set = nltk.classify.util.apply_features(extract_features, training_tweets)

	#Train the classifier
	NBClassifier = nltk.NaiveBayesClassifier.train(training_set)
	################################################################################
	#program to find individual tweets sentiment
	
	x = sys.argv[1]
	tweet_list = addTweetToList(x) #list contents are tweet in form of dictionary element
	tweets = pd.DataFrame()

	#Extracting the data of text from individual dictionary tweet
	tweets['text'] = map(lambda tweet: tweet['text'], tweet_list)
	l = tweet_list[0].keys()
	print l


	for tweet in tweets['text']:
		
		processedTweet = processTweet(tweet)
		proc_tweet.write(processedTweet)	#not all data in tweets can be written in file
		proc_tweet.write('\n')
		processed_tweet_list.append(processedTweet)
		
		featureVector = getFeatureVector(processedTweet,stopWords)
		for word in featureVector:		
			feature_vector.write(word)
			feature_vector.write(' ')
		feature_vector.write('\n')
		feature_vector_list.append(featureVector)

		extracted_feature_dict = extract_features(featureVector)
		for i in range(0,len(extracted_feature_dict)):
			extracted_feature.write(extracted_feature_dict.keys()[i])
			extracted_feature.write(' : ')
			extracted_feature.write(str(extracted_feature_dict.values()[i]))
			extracted_feature.write(',')

		extracted_feature.write('\n')
		extracted_feature_list.append(extracted_feature_dict)

		output = NBClassifier.classify(extracted_feature_dict)
		print output
		tweet_sentiment.write(output)
		tweet_sentiment.write('\n')

		


	proc_tweet.close()
	feature_vector.close()
	extracted_feature.close()
	tweet_sentiment.close()	



	

		

