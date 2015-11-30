#!/usr/bin/env python
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


def get_city(city):
    """Return a meteo json dictionary corresponding to city"""

    jsonfile_url = "http://www.prevision-meteo.ch/services/json/" + city

    f = urllib2.urlopen(jsonfile_url)  # open url
    return json.load(f)  # Read JSON file


def plot_day_tempe(day):
    """Plot Temperature vs hour from a day dictionary"""

    day_hd = day['hourly_data']  # point to hourly data

    # Get tempe = [[h1, T1], [h2, T2], ...] list
    # where h1 is the time in hour and T2 is the temperature in deg. C
    tempe = []
    for hour, data in day_hd.iteritems():
        # get first part of time in "00H00" format and remove "H00"
        # get temperature at 2m above ground 'TMP2m'
        tempe.append([int(hour[:-3]), data['TMP2m']])
    # Alternative form using list comprehension:
    # tempe = [[int(hour[:-3]), data['TMP2m']] for hour, data in day_hd.iteritems()]

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

    axicon = fig.add_axes([0.8, 0.8, 0.15, 0.15])
    img = mpimg.imread(icon)  # initialise image
    axicon.set_xticks([])  # Remove axes ticks
    axicon.set_yticks([])
    axicon.imshow(img)  # trigger the image show
    plt.show()  # trigger the figure show


def get_day(city_json):
    """From user input, return the key for day in json dictonary"""

    days = {day: data['day_long'] for day, data in city_json.iteritems()
            if day[:8] == "fcst_day"}  # Create {'fcst_day_#': week-day}
    question = "Choix du jour :\n"
    days_list = []  # Build ['fcst_day_#', week-day] sorted list
    # This i-loop is required because "days" is not sorted:
    for i in range(5):
        key = "fcst_day_{}".format(i)
        days_list.append([key, days[key]])
        question = question + "{}) {}\n".format(i, days[key])
    choice = int(raw_input(question))
    return days_list[choice][0]


city_json = get_city('Strasbourg')  # get json dict from city name
day = get_day(city_json)  # get day key from user input
plot_day_tempe(city_json[day])  # plot day temperature evolution
