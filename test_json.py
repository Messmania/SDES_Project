#testing json.load
#it takes file handle as input
import json

jsonfile="twitter_streaming_data.json"
fh = open(jsonfile)
print fh
x=json.load(fh)
print x.keys()
