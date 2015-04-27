import nltk

#Training tweets
pos_tweets = [('I love this car', 'positive'),
                ('This view is amazing', 'positive'),
                ('I feel great this morning', 'positive'),
                ('I am so excited about the concert', 'positive'),
                ('He is my best friend', 'positive'),
                ('He is a good man','positive'),
                ('she is happy today','positive'),
                ('I am looking pretty today','positive'),
                ('zealous zeal','positive'),
                ('He is sexy','positive')]

neg_tweets = [('I do not like this car', 'negative'),
              ('This view is horrible', 'negative'),
              ('I feel tired this morning', 'negative'),
              ('I am not looking forward to the concert', 'negative'),
              ('He is my enemy', 'negative'),
              ('He is the worst human','negative'),
              ('He is not a good man','negative'),
              ('She is very mean','negative'),
              ('I look bad today','negative'),
              ('He is annoying','negative')]

word_features=[]
global classifer
#~ print pos_tweets
#~ print neg_tweets

def get_words_in_tweets(tweets):
    """returns a list containing all the words in tweets"""
    all_words = []
    for (words, sentiment) in tweets:
      #~ print words
      all_words.extend(words)
    #~ print all_words
    print "============="    
    return all_words

def get_word_features(wordlist):
    """returns the keys or the words in wordlist, i.e. set"""
    wordlist = nltk.FreqDist(wordlist)
    wf = wordlist.keys()
    #~ print wordlist
    #~ print "Modified", word_features
    return wf

#This is used for extracting features of an input tweet based on matching words from trained set which is 'word_features'
def extract_features(inputTweet):
    """Prepares a dict telling input contains which of our stored words, stored words is a set of out pos and neg tweet words"""
    inputTweet_words = set(inputTweet)
    #~ print document_words
    global word_features
    #~ print "Word features",word_features
    features = {}
    for word in word_features:
        features['contains(%s)' %word] = (word in inputTweet_words)
    return features
    
def prepWordFeatureList(tweets):
    """word_features has all the distinct words in the input tweets"""
    global word_features #because this var is to be used in extract_features
    word_features = get_word_features(get_words_in_tweets(tweets))
    return
    

def prepTweetList():
    tweets = []
    for (w,s) in pos_tweets + neg_tweets:
        #list of all words of length >=2 in the tweet
        tweets_filtered = [word.lower() for word in w.split() if len(word)>=3 ]
        tweets.append((tweets_filtered,s)) #list of all the filtered tweets above
    return tweets
"===================Main func starts================"    

def main():
    tweets = prepTweetList()    
    print "Tweets:\n",tweets
    print "========================"    
    prepWordFeatureList(tweets) #sets the global val value
    print "word features:\n",word_features
    print "len of trained word_features list:",len(word_features)
    #use nltk.word_tokenize to convert a string to list, same can be done using split func of strings
    myTweet= "I like this car so much that I like it a lot"
    tokens = nltk.word_tokenize(myTweet) #tokenize doesn't remove duplicates
    print "Tokens:",tokens
    print "Extract features==========\n",extract_features(tokens)
    #Now above call is extracting feature (in form of a dict) only of one tweet,i.e. it tells if the given tweet contains the words 
    #in our word_feature list,(which we made my performing set on tweet and sorting freq wise)
    # to prepare the whole set of trained tweets, we need lot more tweets
    #so we give out training tweets as input to prepare the set
    #For every tweet, it gives the dict sayin
    training_set = nltk.classify.apply_features(extract_features, tweets)
    print "Training set=========\n"
    print "len of feature-words is:",len(training_set[0][0])
    print "No. of tweets given for training:",len(training_set)
    #~ print training_set[len(training_set)-1]
    print training_set
    global classifier
    classifier= nltk.NaiveBayesClassifier.train(training_set)
    
    print classifier.show_most_informative_features(32)

def findSentiment(tweet):
    global classifer
    #tweet = "Larry is my worst friend"
    print "len:",len(extract_features(tweet.split())),extract_features(tweet.split())
    print "Classifier:",classifier.classify(extract_features(tweet.split()))
  
if __name__ == "__main__":
    main()
