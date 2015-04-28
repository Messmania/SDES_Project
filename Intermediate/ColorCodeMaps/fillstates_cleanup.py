#from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as BM
from matplotlib.colors import rgb2hex
from matplotlib.patches import Polygon
import matplotlib.patches as patches
from pylab import *

#global variables
aLow=45
bHigh,bLow=44,35
cHigh,cLow=34,25
dHigh,dLow=24,11
eHigh,eLow=10,0
N = 255.00
green=(0/N,100/N,0/N)
lightBlue=(32/N,178/N,170/N)
turquoise=(0/N,206/N,209/N)
cadetBlue=(205/N,175/N,149/N)
orange=(255/N,69/N,0/N)
grey=(112/N,138.0/N,144.0/N)
red=(1,0,0)

#Dummy input
popdensity = {
    'Alaska':     52,
    'New Jersey':  438.00,
    'Rhode Island':   387.35,
    'Massachusetts':   312.68,
    'Connecticut':    271.40,
    'Maryland':   209.23,
    'New York':    155.18,
    'Delaware':    154.87,
    'Florida':     114.43,
    'Ohio':  107.05,
    'Pennsylvania':  105.80,
    'Illinois':    86.27,
    'California':  83.85,
    'Hawaii':  72.83,
    'Virginia':    69.03,
    'Michigan':    67.55,
    'Indiana':    65.46,
    'North Carolina':  63.80,
    'Georgia':     54.59,
    'Tennessee':   53.29,
    'New Hampshire':   53.20,
    'South Carolina':  51.45,
    'Louisiana':   39.61,
    'Kentucky':   39.28,
    'Wisconsin':  38.13,
    'Washington':  36.20,
    'Alabama':     33.84,
    'Missouri':    39.36,
    'Texas':   30.75,
    'West Virginia':   29.00,
    'Vermont':     25.41,
    'Minnesota':  23.86,
    'Mississippi':   23.42,
    'Iowa':  20.22,
    'Arkansas':    19.82,
    'Oklahoma':    19.40,
    'Arizona':     17.43,
    'Colorado':    16.01,
    'Maine':  15.95,
    'Oregon':  13.76,
    'Kansas':  12.69,
    'Utah':  10.50,
    'Nebraska':    8.60,
    'Nevada':  7.03,
    'Idaho':   6.04,
    'New Mexico':  5.79,
    'South Dakota':  3.84,
    'North Dakota':  3.59,
    'Montana':     2.39,
    'Wyoming':      1.96
    }

def findMidPoint(dim):  
    x = [p[0] for p in dim]
    y = [p[1] for p in dim]
    centroid = (sum(x) / len(dim), sum(y) / len(dim))
    return centroid


def assignColors(myStates_info,popdensity):    
    colors={}
    statenames=[]
    print aLow,bLow,cLow,dLow,eLow,bHigh,cHigh,dHigh,eHigh
    for shapedict in myStates_info:
        statename = shapedict['NAME']
        # skip DC and Puerto Rico.
        if statename not in ['District of Columbia','Puerto Rico']:
            pop = popdensity[statename]            
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
    plt.legend([b1,b2,b3,b4,b5], ["Happiest","Very happy","Happy","Fine","Sad :("],loc='lower left',fancybox=True,framealpha=0.0)

    
    
def plotOnMap(popdensity):
    m = BM(llcrnrlon=-119,llcrnrlat=20,urcrnrlon=-64,urcrnrlat=49,projection='laea',lat_1=33,lat_2=45,lon_0=-95,lat_0=50)
    #m.bluemarble()
    m.fillcontinents()
    shp_info = m.readshapefile('st99_d00','myStates',drawbounds=True)    
    statenames,colors=assignColors(m.myStates_info,popdensity)
    createPolygons(m.myStates,statenames,colors)
    
    m.drawparallels(np.arange(25,65,20),labels=[1,0,0,0])
    m.drawmeridians(np.arange(-120,-40,20),labels=[0,0,0,1])
    
    setPlotProperties()
    plt.show()


if __name__=='__main__':
    plotOnMap(popdensity)


