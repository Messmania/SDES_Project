#from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap
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




# Lambert Conformal map of lower 48 states.
m = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,projection='lcc',lat_1=33,lat_2=45,lon_0=-95)
#m = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,projection='lcc',lat_1=33,lat_2=45,lon_0=-95)
#m.drawmapboundary(fill_color='aqua')
#m.bluemarble()
#m.etopo()
#m.fillcontinents(color='coral')
# draw state boundaries.

# data from U.S Census Bureau
# http://www.census.gov/geo/www/cob/st2000.html
shp_info = m.readshapefile('st99_d00','myStates',drawbounds=True)
#shp_info = m.readshapefile('./cb_2013_us_state_500k/cb_2013_us_state_500k','myStates',drawbounds=True)
#shp_info = m.readshapefile('./states_21basic/states','myStates',drawbounds=True)
#print "Shp_info==========\n",shp_info,"\nType========\n",type(shp_info)

print "Keys are:",m.myStates_info[0].keys()

#print("Printing shape file",shp_info)
# population density by state from http://en.wikipedia.org/wiki/List_of_U.S._states_by_population_density
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


"==========================================="
#~ print "Mstates info==========\n val1======\n",m.states_info[0],"no.of keys:",len(m.states_info[0].keys())
#~ 
#~ print "\nKeys are:",m.states_info[0].keys(),"\n"
#~ 

print "Type:",type(m.myStates_info),type(m.myStates_info[1])

print "Value:",m.myStates_info[0],len(m.myStates_info)
#~ #print "val2======\n",m.states_info[1],"\n Type:",type(m.states_info[0])
#~ print "LSAD_TRANS field:",m.states_info[0]['LSAD_TRANS'],"len",len(m.states_info[0]['LSAD_TRANS'])


#print "Type of:",type(m),type(m.states)
#print "M states_info keys:==\n",m.states_info[0].keys()


# choose a color for each state based on population density.
colors={}
statenames=[]
N = 255.00

green=(0/N,100/N,0/N)
lightBlue=(32/N,178/N,170/N)
turquoise=(0/N,206/N,209/N)
cadetBlue=(205/N,175/N,149/N)
orange=(255/N,69/N,0/N)
grey=(112/N,138.0/N,144.0/N)
red=(1,0,0)
for shapedict in m.myStates_info:
    statename = shapedict['NAME']
    #print "Statename:",statename
    #~ if statename in statenames: #skip the state if its already been added in the list, because shapefile has one state multiple times
        #~ print "Continuing"
        #~ continue
    # skip DC and Puerto Rico.
    if statename not in ['District of Columbia','Puerto Rico']:
        #~ print "Length of pop:",len(popdensity)
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
       
        
        #print "value:",pop,"statename:",statename
       
    statenames.append(statename)
        #check how many times alaska comes
    #~ if statename.lower() == 'alaska':
        #~ print "Alaska color is:",colors[statename]
        #~ print "States info:",shapedict
#print statenames
#print "colors=================",len(colors)
#print "alaska:",colors['Alaska']
# cycle through state names, color each one.
ax = plt.gca() # get current axes instance
#for nshape,seg in enumerate(m.states):
#print "Types:",type(m.states),type(m.states[0]),"\n",m.states[0],len(m.states[0]),len(m.states)
count=0
state_list=[]

for nshape,seg in enumerate(m.myStates):
    #~ if nshape==0:
        #~ print "seg==\n",len(m.states[0][0]),m.states[0][0]
    # skip DC and Puerto Rico.
    
    if statenames[nshape] not in ['District of Columbia','Puerto Rico']:
        #if statenames[nshape] not in state_list:
        state_list.append(statenames[nshape]) 
        color = rgb2hex(colors[statenames[nshape]]) 
        poly = Polygon(seg,facecolor=color,edgecolor='black')
        ax.add_patch(poly)
        count+=1
        #print "States:",statenames[nshape]
    #~ if statenames[nshape].lower()=='alaska': #testing
        #~ print "Adding color for:",statenames[nshape],"as:",color,"poly:",poly
#print "count:",count
#print "state list:",state_list,"len:",len(state_list)
            
# draw meridians and parallels.
#m.drawparallels(np.arange(25,65,20),labels=[1,0,0,0])
#m.drawmeridians(np.arange(-120,-40,20),labels=[0,0,0,1])
plt.title('State wise sentiment analysis',fontsize=18)



b1 = bar([0, 1, 2], [0.2, 0.3, 0.1], width=0.2, align="center",color=green)
b2 = bar([0, 1, 2], [0.2, 0.3, 0.1], width=0.2, align="center",color=lightBlue)
b3 = bar([0, 1, 2], [0.2, 0.3, 0.1], width=0.2, align="center",color=cadetBlue)
b4 = bar([0, 1, 2], [0.2, 0.3, 0.1], width=0.2, align="center",color=orange)
b5 = bar([0, 1, 2], [0.2, 0.3, 0.1], width=0.2, align="center",color=red)
plt.legend([b1,b2,b3,b4,b5], ["Happiest","Very happy","Happy","Fine","Sad :("],loc='lower left',fancybox=True,framealpha=0.0)

plt.show()
