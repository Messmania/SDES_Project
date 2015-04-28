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

def checkPolyFillStates():
    ax = plt.gca()

    N = 3
    patches = []
    #x=[[1,1.5] [2,2.5] [3,3.5]]
    dim1 = np.random.rand(N,2)
    dim2 = np.random.rand(N,2)
    dim3 = np.random.rand(N,2)
    arrayCoordinates=[dim1,dim2,dim3]
    #dim = np.array([[1,2],[2,3],[3,4],[5,2]])
    print "Type:",type(dim1)
    #~ dim=np.array([[ 1 0.5 ]
        #~ [ 2 2.5 ]
        #~ [ 3 3.5 ]])
    print "Dim:",dim1
    textArr=["Poly1","Poly2","Poly3"]
    for i in range(N):
        poly = Polygon(arrayCoordinates[i], True)
        ax.add_patch(poly)
        centroid=findMidPoint(arrayCoordinates[i])
        ax.text(centroid[0],centroid[1],textArr[i],fontsize=12)
    plt.show()
    

def findMidPoint(dim):    
    print dim    
    x = [p[0] for p in dim]
    y = [p[1] for p in dim]
    centroid = (sum(x) / len(dim), sum(y) / len(dim))
    print centroid
    return centroid

    
