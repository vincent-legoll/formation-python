# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 18:02:51 2015

@author: boileau
"""

import urllib2
import json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

jsonfile_url = "http://www.prevision-meteo.ch/services/json/Strasbourg"

urls = {}  # Dict to store available URLs
f = urllib2.urlopen(jsonfile_url)
json = json.load(f)  # Read JSON file

#class City(object):
#    
#    def __init__(self, json):
#        self.data = json
#        
#    def __repr__(self):
#        output = 'Object {} contains:\n  '.format(type(self).__name__)
#        output = output + '\n  '.join([data for data in self.data])
#        return output
#        
#    def info(self):
##        Print "Name: {}".for
#        print "<City info>"
#        for k, val in self.data['city_info'].iteritems():
#            print "  {:<9}: {:<8}".format(k, val)
#
#
#class Day(object):
#    
#    def __init__(self, city, day):
#        
#        self.data = city.data[day]
#        self.hd = self.data['hourly_data']
#        
#    def __repr__(self):
#        output = 'Object {} contains:\n  '.format(type(self).__name__)
#        output = output + '\n  '.join([data for data in self.data])
#        return output
#
#        
#city = City(json)
#print city
#city.info()
#
#day = Day(city, 'fcst_day_1')
#print day


day = json['fcst_day_1']  # point the current day data
day_hd = day['hourly_data']  # point to hourly data

# Get temperature
tempe = [[int(time.split('H')[0]), day_hd[time]['TMP2m']] for time in day_hd]
tempe.sort()  # Sort temperatures according to the hour of day
tt = np.array(tempe)  
t = tt.transpose()


# Plot T = T(hour)
fig = plt.figure()
fig.suptitle('Day temperature', fontsize=14, fontweight='bold')

ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
#ax.set_title('axes title')

ax.set_xlabel('Time [h]')
ax.set_ylabel('Temperature [deg. C]')

ax.plot(t[0], t[1])

# Add meteo icon to plot
icon = urllib2.urlopen(day['icon_big'])

axicon = fig.add_axes([0.8,0.8,0.1,0.1])
img = mpimg.imread(icon)
axicon.set_xticks([])
axicon.set_yticks([])
axicon.imshow(img)
