from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import shapefile as sh

m = Basemap(llcrnrlon=-0.5,llcrnrlat=39.8,urcrnrlon=4.,urcrnrlat=43.,
             resolution='i', projection='tmerc', lat_0 = 39.5, lon_0 = 1)

m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='#ddaa66',lake_color='aqua')
m.drawcoastlines()

#map.readshapefile('./states_21basic/states', 'florida')
#m.readshapefile('./cb_2013_us_state_500k/cb_2013_us_state_500k', 'florida')
r = sh.ReadFile('./cb_2013_us_state_500k/cb_2013_us_state_500k', 'florida')

plt.show()
