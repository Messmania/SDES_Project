#this is the final file for live streaming state wise in U.S.

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
    #~ def on_data(self, data):
        #~ #print data
        #~ #Added--Monika
        #~ #json_object = json.loads(data)
        #~ #for i in range(0,5):
        #~ if 'delete' not in data: # do not dump deleted tweets in the file
            #~ print data
        #~ #print self.json_object
        #~ #print type(json_object)
        #~ #print json_object
        #~ #print json_object.keys()
        #~ #return True #returning true means keep the connection alive and keep reading tweets, it prints tweets one by one
        #~ return True
        
        #return False
    
    def __init__(self):
        """for setting the count variable for the no. of tweets we want"""
        self.count = 0
        
    def on_data(self,data):
        """for dumping only first 10 tweets which are not the deleted ones"""
        if 'delete' not in data:
            self.count = self.count + 1
            print data
        if self.count==500:            
            return False
        return True
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
    #Entire U.S.                                long1,lat1,long2,lat2
    #stream.filter(languages=["en"], locations=[-125,30,-70,50], track=["a","and","the","i","is","of","in","it","you","u","for"])
 
    #1.Alabama
    #Longitude: 84deg 51' W to 88deg 28' W
    #Latitude: 30deg 13' N to 35deg N
    #stream.filter(languages=["en"], locations=[-88.466,30.216,-84.80,35], track=["a","and","the","i","is","of","in","it","you","u","for"])

    #2.Alaska
    #Longitude: 130deg W to 173deg E
    #Latitude: 54deg 40' N to 71deg 50' N
    #stream.filter(languages=["en"], locations=[-130,54.66,173,71.8], track= ["a","and","the","i","is","of","in","it","you","u","for"])

    #3.Arizona
    #Longitude: 109deg 3' W to 114deg 50' W
    #Latitude: 31deg 20' N to 37deg N
    #stream.filter(languages=["en"], locations=[-114.8,31.33,-109.05,37], track= ["a","and","the","i","is","of","in","it","you","u","for"])

    #4.Arkansas
    #Longitude: 89deg 41' W to 94deg 42' W
    #Latitude: 33deg N to 36deg 30' N
    #stream.filter(languages=["en"], locations=[-94.66,33,-89.66,36.5], track= ["a","and","the","i","is","of","in","it","you","u","for"])

    #5.California
    #Longitude: 114deg 8' W to 124deg 24' W
    #Latitude: 32deg 30' N to 42deg N
    #stream.filter(languages=["en"], locations=[-124.4,32.5,-114.133,42], track= ["a","and","the","i","is","of","in","it","you","u","for"])

    #6.Colorado
    #Longitude: 102deg W to 109deg W
    #Latitude: 37deg N to 41deg N
    #stream.filter(languages=["en"], locations=[-109,37,-102,41], track= ["a","and","the","i","is","of","in","it","you","u","for"])

    #7.Connecticut
    #Longitude: 71deg 47' W to 73deg 44' W
    #Latitude: 40deg 58' N to 42deg 3' N
    #stream.filter(languages=["en"], locations=[-73.67,41,-71.783,42.05], track= ["a","and","the","i","is","of","in","it","you","u","for"])

    #8.Delaware
    #Longitude: 75deg 2' W to 75deg 47' W
    #Latitude: 38deg 27' N to 39deg 50' N
    #stream.filter(languages=["en"], locations=[-75.783,38.48,-75.033,39.8], track= ["a","and","the","i","is","of","in","it","you","u","for"])

    #9.Florida
    #Longitude: 79deg 48' W to 87deg 38' W
    #Latitude: 24deg 30' N to 31deg N
    stream.filter(languages=["en"], locations=[-87.66,24.5,-79.78,31], track= ["a","and","the","i","is","of","in","it","you","u","for"])

    #10.Georgia
    #Longitude: 81deg W to 85deg 53' W
    #Latitude: 30deg 31' N to 35deg N
    #stream.filter(languages=["en"], locations=[-85.82,30.5,-81,35], track= ["a","and","the","i","is","of","in","it","you","u","for"])

    #11.Hawaii
    #Longitude: 154deg 40' W to 162deg W
    #Latitude: 16deg 55' N to 23deg N
    #stream.filter(languages=["en"], locations=[-162,16.916,-154.66,23], track= ["a","and","the","i","is","of","in","it","you","u","for"])

    #12.Idaho
    #Longitude: 111degW to 117deg W
    #Latitude: 42deg N to 49deg N
    #stream.filter(languages=["en"], locations=[-117,42,-111,49], track= ["a","and","the","i","is","of","in","it","you","u","for"])

    #13.Illinois
    #Longitude: 87deg 30' W to 91deg 30' W
    #Latitude: 36deg 58' N to 42deg 30' N
    #stream.filter(languages=["en"], locations=[-91.5,37,-87.5,42.5], track= ["a","and","the","i","is","of","in","it","you","u","for"])

    #14.Indiana --No tweets
    #Longitude: 84deg 49' W to 88deg 4' W
    #Latitude: 37deg 47' N to 41deg 46' N
    #stream.filter(languages=["en"], locations=[-84.8,37.783,-88.066,41.75], track= ["a","and","the","i","is","of","in","it","you","u","for"])

    #15.Iowa
    #Longitude: 89deg 5' W to 96deg 31' W
    #Latitude: 40deg 36' N to 43deg 30' N
    #stream.filter(languages=["en"], locations=[-96.5,40.60,-89.0833,43.5], track= ["a","and","the","i","is","of","in","it","you","u","for"])

    #16.Kansas
    #Longitude: 94deg 38'W to 102deg 1' 34"W
    #Latitude: 37degN to 40degN
    #stream.filter(languages=["en"], locations=[-102,37,-94.59,40], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #17.Kentucky
    #Longitude: 81deg 58'W to 89deg 34'W
    #Latitude: 36deg 30'N to 39deg 9'N
    #stream.filter(languages=["en"], locations=[-89.55,36.5,-82,39.15], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #18.Louisiana
    #Longitude: 89degW to 94degW
    #Latitude: 29degN to 33degN
    #stream.filter(languages=["en"], locations=[-94,29,-89,33], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #19.Maine
    #Longitude: 66deg 57'W to 71deg 7'W
    #Latitude: 43deg 4'N to 47deg 28'N
    #stream.filter(languages=["en"], locations=[-71.12,43.066,-66.95,47.5], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #20.Maryland
    #Longitude: 75deg 4'W to 79deg 33'W
    #Latitude: 37deg 53'N to 39deg 43'N
    #stream.filter(languages=["en"], locations=[-79.52,37.87,-75.066,39.7166], track= ["a","and","the","i","is","of","in","it","you","u","for"])	


    #21.Massachusetts
    #Longitude: 69deg 57' W to 73deg 30' W
    #Latitude: 41deg 10' N to 42deg 53' N
    #stream.filter(languages=["en"], locations=[-73.5,41.166,-69.95,42.88], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #22.Michigan
    #Longitude: 82deg 26' W to 90deg 31' W
    #Latitude: 41deg 41' N to 47deg 30' N
    #stream.filter(languages=["en"], locations=[-90.5,41.66,-82.433,47.5], track= ["a","and","the","i","is","of","in","it","you","u","for"])

	
    #23.Minnesota
    #Longitude: 89deg 34'W to 97deg 12'W
    #Latitude: 43deg 34'N to 49deg 23'N
    #stream.filter(languages=["en"], locations=[-97.2,43.55,-89.55,49.3833], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #24.Mississippi
    #Longitude: 88deg 7' W to 91deg 41' W
    #Latitude: 30deg 13' N to 35deg N
    #stream.filter(languages=["en"], locations=[-91.66,30.216,-88.116,35], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #25.Missouri
    #Longitude: 89deg 6'W to 95deg 42'W
    #Latitude: 36degN to 40deg 35'N
    #stream.filter(languages=["en"], locations=[-95.66,36,-89.1,40.583], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #26.Montana
    #Longitude: 104deg 2'W to 116deg 2'W
    #Latitude: 44deg 26'N to 49degN
    #stream.filter(languages=["en"], locations=[-116.033,44.433,-104.033,49], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #27.Nebraska
    #Longitude: 95deg 25'W to 104degW
    #Latitude: 40degN to 43degN
    #stream.filter(languages=["en"], locations=[-104,40,-95.416,43], track= ["a","and","the","i","is","of","in","it","you","u","for"])
	

    #28.Nevada
    #Longitude: 114degW to 120degW
    #Latitude: 35degN to 42degN
    #stream.filter(languages=["en"], locations=[-120,35,-114,42], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #29.New Hampshire
    #Longitude: 70deg 37'W to 72deg 37'W
    #Latitude: 42deg 40'N to 45deg 18'N
    #stream.filter(languages=["en"], locations=[-72.617,42.66,-70.617,45.31], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #30.New Jersey
    #Longitude: 73deg 53' 39"W to 75deg 35'W
    #Latitude: 38deg 55'N to 41deg 21' 23"N
    #stream.filter(languages=["en"], locations=[-75.55,38.916,-73.883,41.33], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #31.New Mexico
    #Longitude: 103degW to 109degW
    #Latitude: 31deg 20'N to 37degN
    #stream.filter(languages=["en"], locations=[-109,31.33,-103,37], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #32.New York
    #Longitude: 71deg 47' 25" W to 79deg 45' 54" W
    #Latitude: 40deg 29' 40" N to 45deg 0' 42" N
    #stream.filter(languages=["en"], locations=[-79.75,40.5,-71.78,45], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #33.North Carolina
    #Longitude: 75deg 30' W to 84deg 15' W
    #Latitude: 34deg N to 36deg 21' N
    #stream.filter(languages=["en"], locations=[-84.25,34,-75.5,36.33], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #34.North Dakota
    #Longitude: 97degW to 104degW
    #Latitude: 45deg 55'N to 49degN
    #stream.filter(languages=["en"], locations=[-104,45.916,-97,49], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #35.Ohio
    #Longitude: 80deg 32' W to 84deg 49' W
    #Latitude: 38deg 27' N to 41deg 58' N
    #stream.filter(languages=["en"], locations=[-84.8,38.5,-80.5,42], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #36.Oklahoma  --no tweet data
    #Longitude: 94deg 29'W to 103degW
    #Latitude: 33deg 35'N to 37degN
    #stream.filter(languages=["en"], locations=[-103,37,-94.5,33.55], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #37.Oregon
    #Longitude: 116deg 45'W to 124deg 30'W
    #Latitude: 42degN to 46deg 15'N
    #stream.filter(languages=["en"], locations=[-124.5,42,-116.75,46.25], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #38.Pennsylvania
    #Longitude: 74deg 43' W to 80deg 31' W
    #Latitude: 39deg 43' N to 42deg N
    #stream.filter(languages=["en"], locations=[-80.5,39.67,-74.66,42], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #39.Rhode Island
    #Longitude: 71deg 8'W to 71deg 53'W
    #Latitude: 41deg 18'N to 42deg 1'N
    #stream.filter(languages=["en"], locations=[-71.883,41.3,-71.11,42], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #40.South Carolina
    #Longitude: 78deg 30"W to 83deg 20' W
    #Latitude: 32deg 4' 30"N to 35deg 12'N
    #stream.filter(languages=["en"], locations=[-83.33,32.0667,-78.5,32.2], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #41.South Dakota
    #Longitude: 98deg 28' 33"W to 104deg 3'W
    #Latitude: 42deg 29' 30"N to 45deg 56'N
    #stream.filter(languages=["en"], locations=[-104.05,42.5,-98.466,45.93], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #42.Tennessee
    #Longitude: 81deg 37'W to 90deg 28'W
    #Latitude: 35degN to 36deg 41'N
    #stream.filter(languages=["en"], locations=[-90.466,35,-81.616,36.66], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #43.Texas
    #Longitude: 93deg 31' W to 106deg 38' W
    #Latitude: 25deg 50' N to 36deg 30' N
    #stream.filter(languages=["en"], locations=[-106.6,25.8,-93.5,36.5], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #44.Utah
    #Longitude: 109degW to 114degW
    #Latitude: 37degN to 42degN
    #stream.filter(languages=["en"], locations=[-114,37.783,-109,42], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #45.Vermont
    #Longitude: 71deg 28'W to 73deg 26'W
    #Latitude: 42deg 44'N to 45deg 0' 43"N
    #stream.filter(languages=["en"], locations=[-73.47,42.75,-71.5,45], track= ["a","and","the","i","is","of","in","it","you","u","for"])

	
    #46.Virginia
    #Longitude: 75deg 13'W to 83deg 37'W
    #Latitude: 36deg 31'N to 39deg 37'N
    #stream.filter(languages=["en"], locations=[-83.6,36.5,-75.2,39.6], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #47.Washington
    #Longitude: 116deg 57'W to 124deg 48'W
    #Latitude: 45deg 32'N to 49degN
    #stream.filter(languages=["en"], locations=[-124.78,45.5,116.98,49], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #48.West Virginia
    #Longitude: 77deg 40'W to 82deg 40'W
    #Latitude: 37deg 10'N to 40deg 40'N
    #stream.filter(languages=["en"], locations=[-82.66,37.166,-77.66,40.66], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #49.Wisconsin
    #Longitude: 86deg 49'W to 92deg 54'W
    #Latitude: 42deg 30'N to 47deg 3'N
    #stream.filter(languages=["en"], locations=[-92.9,42.5,-86.8,47.05], track= ["a","and","the","i","is","of","in","it","you","u","for"])


    #50.Wyoming
    #Longitude: 104deg 3'W to 111deg 3'W
    #Latitude: 41degN to 45degN
    #stream.filter(languages=["en"], locations=[-111.05,41,-104.05,45], track= ["a","and","the","i","is","of","in","it","you","u","for"])


	#US:longitude:120W-70W and latitude:30N-50N
	#stream.sample() #works: collects tweets





