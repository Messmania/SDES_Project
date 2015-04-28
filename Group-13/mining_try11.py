#for in the day during afternoon,evening,night bar chart

#For data mining of twitter data :Sentiment Analyses
import json
import pandas as pd
import sys
import re
#import matplotlib.pyplot as plt
import csv
import nltk
import unicodedata
#import regex #to eliminate username and replace with AT_USER
####################################################################
#for bar data plotting
import numpy as np
import matplotlib.pyplot as plt

####################################################################
#for plotting bar graph for 500 tweets
def plotDayWiseScore(alabama,california,florida):
	fig = plt.figure()
	ax = fig.add_subplot(111)

	## the data
	N = 3
	## necessary variables
	ind = np.arange(N)                # the x locations for the groups
	width = 0.15                      # the width of the bars


	## the bars
	rects1 = ax.bar(ind, alabama, width,color=(0.1,0.749,1))

	rects2 = ax.bar(ind+width, california, width,color='orange')

	rects3 = ax.bar(ind+width+width, florida, width,color='green')

	# axes and labels
	ax.set_xlim(-3*width,len(ind)+4*width,3*width)
	ax.set_ylim(0,450)
	ax.set_ylabel('Scores')
	ax.set_title('Happiness score of states, time wise')
	xTickMarks = ['Afternoon','Evening','Night']
	ax.set_xticks(ind+width+width)
	xtickNames = ax.set_xticklabels(xTickMarks)
	plt.setp(xtickNames, rotation=0, fontsize=12)

	ax.legend( (rects1[0], rects2[0],rects3[0]), ('Alabama', 'California','Florida'))

	plt.show()

##################################################################
#for plotting bar graph for 500 tweets
def plotDayWiseScore50(alabama,california,florida):
	fig = plt.figure()
	ax = fig.add_subplot(111)

	## the data
	N = 3
	## necessary variables
	ind = np.arange(N)                # the x locations for the groups
	width = 0.15                      # the width of the bars


	## the bars
	rects1 = ax.bar(ind, alabama, width,color=(0.1,0.749,1))

	rects2 = ax.bar(ind+width, california, width,color='orange')

	rects3 = ax.bar(ind+width+width, florida, width,color='green')

	# axes and labels
	ax.set_xlim(-3*width,len(ind)+4*width,3*width)
	ax.set_ylim(0,45)
	ax.set_ylabel('Scores')
	ax.set_title('Happiness score of states, time wise')
	xTickMarks = ['Afternoon','Evening','Night']
	ax.set_xticks(ind+width+width)
	xtickNames = ax.set_xticklabels(xTickMarks)
	plt.setp(xtickNames, rotation=0, fontsize=12)

	ax.legend( (rects1[0], rects2[0],rects3[0]), ('Alabama', 'California','Florida'))

	plt.show()

##################################################################


#global featureList
#featureList = []

file_list_time_50 = ['state_time/alabama_afternoon_50.json','state_time/california_afternoon_50.json',                           'state_time/florida_afternoon_50.json','state_time/alabama_evening_50.json','state_time/california_evening_50.json',                      'state_time/florida_evening_50.json','state_time/alabama_night_50.json','state_time/california_night_50.json',                   'state_time/florida_night_50.json']

file_list_time_500 = ['state_time/alabama_afternoon_500.json','state_time/california_afternoon_500.json',                           'state_time/florida_afternoon_500.json','state_time/alabama_evening_500.json','state_time/california_evening_500.json',          'state_time/florida_evening_500.json','state_time/alabama_night_500.json','state_time/california_night_500.json',                 'state_time/florida_night_500.json']
 
#oklohoma and indiana are not there in file list as there are no tweets
file_list_50 = ['states/alabama.json','states/georgia.json','states/maryland.json','states/new_mexico.json','states/tennessee.json', 'states/alaska.json','states/hawaii.json','states/massachusetts.json','states/new_york.json','states/idaho.json','states/   michigan.json','states/north_carolina.json','states/texas.json','states/arizona.json','states/illinois.json','states/minnesota.json', 'states/north_dakota.json','states/utah.json','states/missisippi.json','states/ohio.json','states/vermont.json','states/arkansas.json','states/missouri.json','states/virginia.json','states/california.json','states/iowa.json','states/montana.json','states/ oregon.json','states/washington.json','states/colorado.json','states/kansas.json','states/nebraska.json','states/pennsylvania.json', 'states/west_virginia.json','states/connecticut.json','states/kentucky.json','states/nevada.json','states/rhode_island.json','states/  wisconsin.json','states/delaware.json','states/louisiana.json','states/new_hamsphire.json','states/south_carolina.json','states/  wyoming.json','states/florida.json','states/maine.json','states/new_jersey.json','states/south_dakota.json']

file_list_500 = ['states_500/alabama500.json','states_500/georgia500.json','states_500/maryland500.json','states_500/new_mexico500.json','states_500/tennessee500.json', 'states_500/alaska500.json','states_500/hawaii500.json','states_500/massachusetts500.json','states_500/new_york500.json','states_500/idaho500.json','states_500/michigan500.json','states_500/north_carolina500.json','states_500/texas500.json','states_500/arizona500.json','states_500/illinois500.json','states_500/minnesota500.json', 'states_500/north_dakota500.json','states_500/utah500.json','states_500/missisippi500.json','states_500/ohio500.json','states_500/vermont500.json','states_500/arkansas500.json','states_500/missouri500.json','states_500/virginia500.json','states_500/california500.json','states_500/iowa500.json','states_500/montana500.json',                       'states_500/oregon500.json','states_500/washington500.json','states_500/colorado500.json','states_500/kansas500.json','states_500/nebraska500.json','states_500/pennsylvania500.json', 'states_500/west_virginia500.json','states_500/connecticut500.json','states_500/kentucky500.json','states_500/nevada500.json','states_500/rhode_island500.json','states_500/wisconsin500.json','states_500/delaware500.json','states_500/louisiana500.json','states_500/new_hampshire500.json','states_500/south_carolina500.json',        'states_500/wyoming500.json','states_500/florida500.json','states_500/maine500.json','states_500/new_jersey500.json',           'states_500/south_dakota500.json']

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
			if('limit' in tweet.keys()):
				continue
			else:
				tweet_list.append(tweet)
		    except:
			continue 
		   
		#print "Number of tweets are:",len(tweet_list)
		
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
	#oklohoma and indiana are not there in file list as there are no tweets so default 
	#plot_dict_positive_tweets = {'oklohoma':'390','indiana':'390'}	# for 50 tweets 42 
	#plot_dict_negative_tweets = {'oklohoma':'60','indiana':'60'} # for 50 tweets 8
	#plot_dict_happy_score = {'oklohoma':'60','indiana':'60'}# for 50 tweets 8 
	plot_dict_positive_tweets_500 = {}	
	plot_dict_negative_tweets_500 = {} 
	plot_dict_happy_score_500 = {}
	plot_dict_positive_tweets_50 = {}	
	plot_dict_negative_tweets_50 = {} 
	plot_dict_happy_score_50 = {}

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
	

	###########################################################################

	#run code for 3 states for different time in day for 500 tweets and get dictionary corresponding
	#for k in range(0,len(file_list_500)): # 48 here as other 2 are defaults ,for 50 tweets comparing use file_list_50
	for k in range(0,len(file_list_time_500)):
		###########################################################################
		#definition and declaration part

		file_name = file_list_time_500[k]
		state_name = file_name.split("/")[1]
		state_name = state_name.split(".")[0]
		state_name = state_name.replace("500","") 	#for 50 tweets list comment this line

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

		################################################################################
		#program to find individual tweets sentiment
	
		x = file_name
		tweet_list = addTweetToList(x) #list contents are tweet in form of dictionary element
		#tweets = pd.DataFrame()

		#Extracting the data of text from individual dictionary tweet
		#tweets['text'] = map(lambda tweet: tweet['text'], tweet_list)

		#key_text_exists = 'text' in tweet_list[0].keys()
		#print "Text key Exists : " , key_text_exists
		#print tweet_list[1]['text']
	
		tweet_text_list = []
		for i in range(0,450): 	#len(tweet_list) make it 450 when u stream 500 and 45 when u stream 500 tweets
			tweet_text_list.append(tweet_list[i]['text'])
		positive_tweets = 0
		negative_tweets = 0
	
		#for tweet in tweets['text']:
		for i in range(0,len(tweet_text_list)):
			tweet = tweet_text_list[i]
			processedTweet = processTweet(tweet)

			processedTweet = unicodedata.normalize('NFKD', processedTweet).encode('ascii','ignore')
			#processedTweet = processedTweet.decode('unicode_escape').encode('ascii','ignore')
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
			for j in range(0,len(extracted_feature_dict)):
				extracted_feature.write(extracted_feature_dict.keys()[j])
				extracted_feature.write(' : ')
				extracted_feature.write(str(extracted_feature_dict.values()[j]))
				extracted_feature.write(',')

			extracted_feature.write('\n')
			extracted_feature_list.append(extracted_feature_dict)

			output = NBClassifier.classify(extracted_feature_dict)
			#print output
			if(output == "positive"):
				positive_tweets = positive_tweets + 1
			if(output == "negative"):
				negative_tweets = negative_tweets + 1
			tweet_sentiment.write(output)
			tweet_sentiment.write('\n')
			happy_score = positive_tweets - negative_tweets

		
		#print "Positive Tweets: ", positive_tweets
		#print "Negative Tweets: ", negative_tweets
		#print "Happy Score: ", happy_score
		plot_dict_positive_tweets_500[state_name] = str(positive_tweets)
		plot_dict_negative_tweets_500[state_name] = str(negative_tweets)
		plot_dict_happy_score_500[state_name] = str(happy_score) 
		#print "State record added in dictionary"

		proc_tweet.close()
		feature_vector.close()
		extracted_feature.close()
		tweet_sentiment.close()	

	#print "Positive Tweets Dictionary : ",plot_dict_positive_tweets_500
	#print "Negative Tweets Dictionary : ",plot_dict_negative_tweets_500
	#print "Happy Score Dictionary : ",plot_dict_happy_score_500

	plot_dict_percent_pos_tweets_500 = {}
	
	for key in plot_dict_positive_tweets_500:
		plot_dict_percent_pos_tweets_500[key] = str(float(int(plot_dict_positive_tweets_500[key]))/450*100)		

	#print "Percentage Tweets Dictionary : ",plot_dict_percent_pos_tweets_500
	alabama500 = [0,0,0] #initialization
	california500 = [0,0,0]
	florida500 = [0,0,0]
	for key in plot_dict_positive_tweets_500:
		if("alabama_afternoon" in key):
			alabama500[0] = int(plot_dict_positive_tweets_500[key])
		elif("alabama_evening" in key):
			alabama500[1] = int(plot_dict_positive_tweets_500[key])
		elif("alabama_night" in key):
			alabama500[2] = int(plot_dict_positive_tweets_500[key])

		elif("florida_afternoon" in key):
			florida500[0] = int(plot_dict_positive_tweets_500[key])
		elif("florida_evening" in key):
			florida500[1] = int(plot_dict_positive_tweets_500[key])
		elif("florida_night" in key):
			florida500[2] = int(plot_dict_positive_tweets_500[key])

		elif("california_afternoon" in key):
			california500[0] = int(plot_dict_positive_tweets_500[key])
		elif("california_evening" in key):
			california500[1] = int(plot_dict_positive_tweets_500[key])
		elif("california_night" in key):
			california500[2] = int(plot_dict_positive_tweets_500[key])


	plotDayWiseScore(alabama500,california500,florida500)

	###########################################################################

	#run code for 3 states for different time in day for 50 tweets and get dictionary corresponding
	#for k in range(0,len(file_list_500)): # 48 here as other 2 are defaults ,for 50 tweets comparing use file_list_50
	for k in range(0,len(file_list_time_50)):
		###########################################################################
		#definition and declaration part

		file_name = file_list_time_50[k]
		state_name = file_name.split("/")[1]
		state_name = state_name.split(".")[0]
		state_name = state_name.replace("50","") 	#for 50 tweets list comment this line

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

		################################################################################
		#program to find individual tweets sentiment
	
		x = file_name
		tweet_list = addTweetToList(x) #list contents are tweet in form of dictionary element
		#tweets = pd.DataFrame()

		#Extracting the data of text from individual dictionary tweet
		#tweets['text'] = map(lambda tweet: tweet['text'], tweet_list)

		#key_text_exists = 'text' in tweet_list[0].keys()
		#print "Text key Exists : " , key_text_exists
		#print tweet_list[1]['text']
	
		tweet_text_list = []
		for i in range(0,45): 	#len(tweet_list) make it 450 when u stream 500 and 45 when u stream 500 tweets
			tweet_text_list.append(tweet_list[i]['text'])
		positive_tweets = 0
		negative_tweets = 0
	
		#for tweet in tweets['text']:
		for i in range(0,len(tweet_text_list)):
			tweet = tweet_text_list[i]
			processedTweet = processTweet(tweet)

			processedTweet = unicodedata.normalize('NFKD', processedTweet).encode('ascii','ignore')
			#processedTweet = processedTweet.decode('unicode_escape').encode('ascii','ignore')
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
			for j in range(0,len(extracted_feature_dict)):
				extracted_feature.write(extracted_feature_dict.keys()[j])
				extracted_feature.write(' : ')
				extracted_feature.write(str(extracted_feature_dict.values()[j]))
				extracted_feature.write(',')

			extracted_feature.write('\n')
			extracted_feature_list.append(extracted_feature_dict)

			output = NBClassifier.classify(extracted_feature_dict)
			#print output
			if(output == "positive"):
				positive_tweets = positive_tweets + 1
			if(output == "negative"):
				negative_tweets = negative_tweets + 1
			tweet_sentiment.write(output)
			tweet_sentiment.write('\n')
			happy_score = positive_tweets - negative_tweets

		
		#print "Positive Tweets: ", positive_tweets
		#print "Negative Tweets: ", negative_tweets
		#print "Happy Score: ", happy_score
		plot_dict_positive_tweets_50[state_name] = str(positive_tweets)
		plot_dict_negative_tweets_50[state_name] = str(negative_tweets)
		plot_dict_happy_score_50[state_name] = str(happy_score) 
		#print "State record added in dictionary"

		proc_tweet.close()
		feature_vector.close()
		extracted_feature.close()
		tweet_sentiment.close()	

	print "Positive Tweets Dictionary : ",plot_dict_positive_tweets_50
	print "Negative Tweets Dictionary : ",plot_dict_negative_tweets_50
	print "Happy Score Dictionary : ",plot_dict_happy_score_50

	plot_dict_percent_pos_tweets_50 = {}
	
	for key in plot_dict_positive_tweets_50:
		plot_dict_percent_pos_tweets_50[key] = str(float(int(plot_dict_positive_tweets_50[key]))/45*100)		

	print "Percentage Tweets Dictionary : ",plot_dict_percent_pos_tweets_50

	alabama50 = [0,0,0] #initialization
	california50 = [0,0,0]
	florida50 = [0,0,0]
	for key in plot_dict_positive_tweets_50:
		if("alabama_afternoon" in key):
			alabama50[0] = int(plot_dict_positive_tweets_50[key])
		elif("alabama_evening" in key):
			alabama50[1] = int(plot_dict_positive_tweets_50[key])
		elif("alabama_night" in key):
			alabama50[2] = int(plot_dict_positive_tweets_50[key])

		elif("florida_afternoon" in key):
			florida50[0] = int(plot_dict_positive_tweets_50[key])
		elif("florida_evening" in key):
			florida50[1] = int(plot_dict_positive_tweets_50[key])
		elif("florida_night" in key):
			florida50[2] = int(plot_dict_positive_tweets_50[key])

		elif("california_afternoon" in key):
			california50[0] = int(plot_dict_positive_tweets_50[key])
		elif("california_evening" in key):
			california50[1] = int(plot_dict_positive_tweets_50[key])
		elif("california_night" in key):
			california50[2] = int(plot_dict_positive_tweets_50[key])

	print "alabama :",alabama50
	print "california :",california50
	print "florida :",florida50 

	plotDayWiseScore50(alabama50,california50,florida50)

	

		

