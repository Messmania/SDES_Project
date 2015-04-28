##Final code for all 50 states with dictionaries made and showed on map

#For data mining of twitter data :Sentiment Analyses
import json
import pandas as pd
import sys
import re
import csv
import nltk
import unicodedata
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as BM
from matplotlib.colors import rgb2hex
from matplotlib.patches import Polygon
import matplotlib.patches as patches
from pylab import *

#global variables to plot graph
#~ aLow=416                #Happiest
#~ bHigh,bLow=415,411      #Happier
#~ cHigh,cLow=410,401      #Happy
#~ dHigh,dLow=400,391      #OK
#~ eHigh,eLow=390,385      #Not sad

aLow=381                #Happiest
bHigh,bLow=380,366      #Happier
cHigh,cLow=355,351      #Happy
dHigh,dLow=350,331      #OK
eHigh,eLow=330,310      #Not sad

N = 255.00
green=(0/N,100/N,0/N)
lightBlue=(32/N,178/N,170/N)
turquoise=(0/N,206/N,209/N)
cadetBlue=(205/N,175/N,149/N)
orange=(255/N,69/N,0/N)
grey=(112/N,138.0/N,144.0/N)
red=(1,0,0)



##functions to plot graph
def findMidPoint(dim):  
        x = [p[0] for p in dim]
        y = [p[1] for p in dim]
        centroid = (sum(x) / len(dim), sum(y) / len(dim))
        return centroid


def assignColors(myStates_info,popdensity):
        print "Pop density in assignColors \n",popdensity    
        colors={}
        statenames=[]
        state_list=[]
        pop_list=[]
        for shapedict in myStates_info:
                statename = shapedict['NAME']
                # skip DC and Puerto Rico.
                if statename not in ['District of Columbia','Puerto Rico']:
                        pop = popdensity[statename]
                        if statename not in state_list:
                                state_list.append(statename)
                                pop_list.append(pop)
                                minPop = min(pop_list)
                                maxPop = max(pop_list)
                        if pop >=aLow:
                                colors[statename] =green #green
                        elif pop>=bLow and pop<bHigh:
                                colors[statename] =lightBlue #light green
                        elif pop>=cLow and pop<cHigh:
                                colors[statename]=orange #light orange
                        elif pop>=dLow and pop<dHigh:
                                colors[statename]=cadetBlue #orange
                        else:
                                colors[statename]=red #red           
                statenames.append(statename)
        print "Sorted",sorted(pop_list),state_list
        print "Min,max:",minPop,maxPop
        return statenames,colors

def createPolygons(myStates,statenames,colors):
        ax = plt.gca() # get current axes instance
        state_list=[]
        for nshape,seg in enumerate(myStates):        
                if statenames[nshape] not in ['District of Columbia','Puerto Rico']:
                        #if statenames[nshape] not in state_list:        
                        color = rgb2hex(colors[statenames[nshape]]) 
                        poly = Polygon(seg,facecolor=color,edgecolor='black')
                        ax.add_patch(poly)
           
                        if statenames[nshape] not in state_list:
                                state_list.append(statenames[nshape]) 
                                centroid=findMidPoint(seg)
                                ax.plot(centroid[0],centroid[1], 'bo')
                                ax.annotate(statenames[nshape],xy=(centroid[0],centroid[1]),fontsize=10,horizontalalignment='right')


def setPlotProperties():
        plt.title('State wise sentiment analysis',fontsize=18)
        b1 = bar([0, 1, 2], [0.2, 0.3, 0.1], width=0.2, align="center",color=green)
        b2 = bar([0, 1, 2], [0.2, 0.3, 0.1], width=0.2, align="center",color=lightBlue)
        b3 = bar([0, 1, 2], [0.2, 0.3, 0.1], width=0.2, align="center",color=cadetBlue)
        b4 = bar([0, 1, 2], [0.2, 0.3, 0.1], width=0.2, align="center",color=orange)
        b5 = bar([0, 1, 2], [0.2, 0.3, 0.1], width=0.2, align="center",color=red)
        plt.legend([b1,b2,b3,b4,b5], ["Happiest","Happier","Happy","Fine","Not sad"],loc='lower left',fancybox=True,framealpha=0.0)

    
    
def plotOnMap(popdensity):
        m = BM(llcrnrlon=-119,llcrnrlat=20,urcrnrlon=-64,urcrnrlat=49,projection='laea',lat_1=33,lat_2=45,lon_0=-95,lat_0=50)
        m.fillcontinents()
        shp_info = m.readshapefile('st99_d00','myStates',drawbounds=True) 
        statenames,colors=assignColors(m.myStates_info,popdensity)
        createPolygons(m.myStates,statenames,colors)

        m.drawparallels(np.arange(25,65,20),labels=[1,0,0,0])
        m.drawmeridians(np.arange(-120,-40,20),labels=[0,0,0,1])

        setPlotProperties()
        plt.show()

def plotPercentage(percentageDict):    
    fig = plt.figure()
    ax = fig.add_subplot(111)

    N = 50
    ## necessary variables
    ind = np.arange(N)                # the x locations for the groups
    width = 0.15                      # the width of the bars


    ## the bars
    ax.bar(ind, percentageDict.values(), width,color=(0.1,0.749,1))

    # axes and labels
    ax.set_xlim(-3*width,len(ind)+4*width,3*width)
    ax.set_ylim(0,100)
    ax.set_ylabel('Percentage of positive tweets')
    ax.set_title('Percentage of happiness in states')
    xTickMarks = percentageDict.keys()
    ax.set_xticks(ind+width+width)
    xtickNames = ax.set_xticklabels(xTickMarks)
    plt.setp(xtickNames, rotation=80, fontsize=8)


    plt.show()
###################################################################################

#global featureList
#featureList = []
 
#oklohoma and indiana are not there in file list as there are no tweets
file_list_50 = ['states/alabama.json','states/georgia.json','states/maryland.json','states/new_mexico.json','states/tennessee.json', 'states/alaska.json','states/hawaii.json','states/massachusetts.json','states/new_york.json','states/idaho.json','states/   michigan.json','states/north_carolina.json','states/texas.json','states/arizona.json','states/illinois.json','states/minnesota.json', 'states/north_dakota.json','states/utah.json','states/missisippi.json','states/ohio.json','states/vermont.json','states/arkansas.json','states/missouri.json','states/virginia.json','states/california.json','states/iowa.json','states/montana.json','states/ oregon.json','states/washington.json','states/colorado.json','states/kansas.json','states/nebraska.json','states/pennsylvania.json', 'states/west_virginia.json','states/connecticut.json','states/kentucky.json','states/nevada.json','states/rhode_island.json','states/  wisconsin.json','states/delaware.json','states/louisiana.json','states/new_hamsphire.json','states/south_carolina.json','states/  wyoming.json','states/florida.json','states/maine.json','states/new_jersey.json','states/south_dakota.json']

file_list_500 = ['states_500/alabama500.json','states_500/georgia500.json','states_500/maryland500.json','states_500/new_mexico500.json','states_500/tennessee500.json', 'states_500/alaska500.json','states_500/hawaii500.json','states_500/massachusetts500.json','states_500/new_york500.json','states_500/idaho500.json','states_500/michigan500.json','states_500/north_carolina500.json','states_500/texas500.json','states_500/arizona500.json','states_500/illinois500.json','states_500/minnesota500.json', 'states_500/north_dakota500.json','states_500/utah500.json','states_500/mississippi500.json','states_500/ohio500.json','states_500/vermont500.json','states_500/arkansas500.json','states_500/missouri500.json','states_500/virginia500.json','states_500/california500.json','states_500/iowa500.json','states_500/montana500.json',                       'states_500/oregon500.json','states_500/washington500.json','states_500/colorado500.json','states_500/kansas500.json','states_500/nebraska500.json','states_500/pennsylvania500.json', 'states_500/west_virginia500.json','states_500/connecticut500.json','states_500/kentucky500.json','states_500/nevada500.json','states_500/rhode_island500.json','states_500/wisconsin500.json','states_500/delaware500.json','states_500/louisiana500.json','states_500/new_hampshire500.json','states_500/south_carolina500.json',        'states_500/wyoming500.json','states_500/florida500.json','states_500/maine500.json','states_500/new_jersey500.json',           'states_500/south_dakota500.json']

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
        plot_dict_positive_tweets = {'Oklahoma':390,'Indiana':390}  # for 50 tweets 42 
        plot_dict_negative_tweets = {'Oklahoma':60,'Indiana':60} # for 50 tweets 8
        plot_dict_happy_score = {'Oklahoma':330,'Indiana':330}# for 50 tweets 8 


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

        #run code for all states and get dictionary corresponding
        #for k in range(0,len(file_list_500)): # 48 here as other 2 are defaults ,for 50 tweets comparing use file_list_50
        for k in range(0,len(file_list_500)):
                ###########################################################################
                #definition and declaration part

                file_name = file_list_500[k]
                state_name = file_name.split("/")[1]
                state_name = state_name.split(".")[0]
                state_name = state_name.replace("500","")       #for 50 tweets list comment this line
                state_name = state_name.replace("_"," ")        #for 50 tweets list comment this line
                state_name = state_name.title()

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
                for i in range(0,450):  #len(tweet_list) make it 450 when u stream 500 and 45 when u stream 500 tweets
                        tweet_text_list.append(tweet_list[i]['text'])
                positive_tweets = 0
                negative_tweets = 0
        
                #for tweet in tweets['text']:
                for i in range(0,len(tweet_text_list)):
                        tweet = tweet_text_list[i]
                        processedTweet = processTweet(tweet)

                        processedTweet = unicodedata.normalize('NFKD', processedTweet).encode('ascii','ignore')
                        #processedTweet = processedTweet.decode('unicode_escape').encode('ascii','ignore')
                        proc_tweet.write(processedTweet)        #not all data in tweets can be written in file
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
                plot_dict_positive_tweets[state_name] = positive_tweets
                plot_dict_negative_tweets[state_name] = negative_tweets
                plot_dict_happy_score[state_name] = happy_score 
                #print "State record added in dictionary"

                proc_tweet.close()
                feature_vector.close()
                extracted_feature.close()
                tweet_sentiment.close() 

        #print "Positive Tweets Dictionary : ",plot_dict_positive_tweets
        #print "Negative Tweets Dictionary : ",plot_dict_negative_tweets
        #print "Happy Score Dictionary : ",plot_dict_happy_score

        plot_dict_percent_pos_tweets = {}
        
        for key in plot_dict_positive_tweets:
                plot_dict_percent_pos_tweets[key] = float(int(plot_dict_positive_tweets[key]))/450*100
 

        #print "Percentage Tweets Dictionary : ",plot_dict_percent_pos_tweets

        #plotOnMap(plot_dict_positive_tweets)    #send dict. whose color representation is to be shown
        plotOnMap(plot_dict_happy_score)
        plotPercentage(plot_dict_percent_pos_tweets)
        
