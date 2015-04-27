from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
# set up mill (plain like) map projection with perspective of satellite looking down at 50N, 100W.
# use low/crude resolution coastlines.
#m = Basemap(projection='mill',lat_0=45,lon_0=-100,resolution='c')
m = Basemap(projection='mill',llcrnrlat=-60,urcrnrlat=90,llcrnrlon=-160,urcrnrlon=-30,resolution='c')
# draw coastlines, country boundaries, fill continents.
#m.drawcoastlines(linewidth=0.25)
m.drawcoastlines() #draws boundaries of the countries
m.fillcontinents(color='coral')
#m.drawmapboundary()
#m.drawcountries() 
m.drawstates(color='blue')
plt.title("First basemap")
plt.show()
