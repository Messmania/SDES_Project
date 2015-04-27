#testing json.load
#it takes file handle as input
import json

#works only for single json object in a file!
jsonfile="twitter_streaming_data.json"
fh = open(jsonfile)
print fh
x=json.load(fh)
print x.keys()


# for reading multiple json objects--Doesn't work

#~ jsonfile="twitter_streaming_data.json"
#~ fh = open(jsonfile)
#~ print fh
#~ for line in fh:
    #~ x_line = str(line)
    #~ x=json.loads(x_line)
    #~ print x.keys()
