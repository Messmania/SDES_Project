import numpy as np
import matplotlib
from matplotlib.patches import Circle, Wedge, Polygon
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
from matplotlib.colors import rgb2hex

def checkEnumerate():
    for i in enumerate([1,2,3,70,12]):
        print i

#~ def checkPolygon():    
    #~ cmap = plt.cm.hot
    #~ colors ={}
    #~ colors['alaska'] = cmap(1.-np.sqrt((2)/(5)))[:3]
    #~ print colors
    #~ color = rgb2hex(colors['alaska']) 
    #~ input1=np.random.rand(3,2)
    #~ print "Input:",input1
    #~ poly = Polygon(input1,True)
#~ 
#~ def checkPoly():
    #~ N= 3
    #~ patches=[]
    #~ for i in range(N):
        #~ polygon = Polygon(np.random.rand(N,2), True)
        #~ patches.append(polygon)
#~ 
    #~ colors = 100*np.random.rand(len(patches))
    #~ p = PatchCollection(patches, cmap=matplotlib.cm.jet, alpha=0.4)
    #~ p.set_array(np.array(colors))
    #~ ax.add_collection(p)
    #~ plt.colorbar(p)
#~ 
    #~ plt.show()

def checkPolygon():
    fig, ax = plt.subplots()

    N = 3
    patches = []
    #x=[[1,1.5] [2,2.5] [3,3.5]]
    dim=np.random.rand(N,2)
    print "Type:",type(dim)
    #~ dim=np.array([[ 1 0.5 ]
        #~ [ 2 2.5 ]
        #~ [ 3 3.5 ]])
    print "Dim:",dim
    for i in range(N):
        polygon = Polygon(dim, True)
        patches.append(polygon)

    colors = 100*np.random.rand(len(patches))
    p = PatchCollection(patches, cmap=matplotlib.cm.jet,alpha=0.4)
    p.set_array(np.array(colors))
    ax.add_collection(p)
    plt.colorbar(p)

    plt.show()

#checkPolygon()

    
