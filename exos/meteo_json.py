# -*- coding: utf-8 -*-
"""
Process a weather forecast json file to plot the time evolution of today's
temperature in Strasbourg
"""

import urllib2
import json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

jsonfile_url = "http://www.prevision-meteo.ch/services/json/Strasbourg"

f = urllib2.urlopen(jsonfile_url)  # open url
json = json.load(f)  # Read JSON file

day = json['fcst_day_1']  # point the current day data
day_hd = day['hourly_data']  # point to hourly data

# Get temperature:
# get first part of time in 00H00 format
# get temperature at 2m above ground
tempe = [[int(time.split('H')[0]), day_hd[time]['TMP2m']] for time in day_hd]
tempe.sort()  # Sort temperatures according to the hour of day
t = np.array(tempe).transpose()  # Transpose list of (hour, tempe)

# Plot T = T(hour)
fig = plt.figure()  # initialise figure
title = "{} {}".format(day['day_long'], day['date'])
fig.suptitle(title, fontsize=14, fontweight='bold')

ax = fig.add_subplot(111)  # initialise a plot area
fig.subplots_adjust(top=0.85)
ax.set_title('Day temperature')
ax.set_xlabel('Time [h]')
ax.set_ylabel('Temperature [deg. C]')

ax.plot(t[0], t[1])  # plot t[1] (tempe) as a function of t[0] (hour)

# Add meteo icon to plot
icon = urllib2.urlopen(day['icon_big'])  # Open weather icon

axicon = fig.add_axes([0.8,0.8,0.15,0.15])
img = mpimg.imread(icon)  # initialise image
axicon.set_xticks([])  # Remove axes ticks
axicon.set_yticks([])
axicon.imshow(img)  # trigger the image show
