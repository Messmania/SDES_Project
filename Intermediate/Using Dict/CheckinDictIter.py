#checking dict iterations

myDict={"a":"yo","b":"yoyo","c":"yoyoyo"}

def iterateOverKV(myDict):
    for key,value in myDict.iteritems():
        print key,value

def iterateOverKeys(myDict):
    for key in myDict.iterkeys():
        print key

def iterateOverValues(myDict):
    for value in myDict.itervalues():
        print value
