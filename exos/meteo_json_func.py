#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Process a weather forecast json file to plot the time evolution of temperature
of a given day in a given city
"""

import urllib2
import json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


def get_city():
    """From user input, return a meteo json dictionary corresponding to city"""

    while True:  # Infinite loop to handle city name input
        city_name = raw_input("Entrer la ville :\n")
        jsonfile_url = "http://www.prevision-meteo.ch/services/json/"\
                       + city_name
        try:
            f = urllib2.urlopen(jsonfile_url)  # open url
            return json.load(f)
        except ValueError:  # Intercept json load error
            print "{} n'existe pas dans la base. Essayer un autre nom."\
                  .format(city_name)


def plot_day_tempe(city_json, day_key):
    """Plot Temperature vs hour from a json dictionary for a given day_key"""

    city_name = city_json['city_info']['name']
    day = city_json[day_key]
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
    title = u"{} {} à {}".format(day['day_long'], day['date'], city_name)
    fig.suptitle(title, fontsize=14, fontweight='bold')

    ax = fig.add_subplot(111)  # initialise a plot area
    fig.subplots_adjust(top=0.85)
    ax.set_title(u'Evolution horaire')
    ax.set_xlabel(u'Temps [h]')
    ax.set_ylabel(u'Température [deg. C]')

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
    """From user input, return the day key in json dictonary"""

    days = {day: data['day_long'] for day, data in city_json.iteritems()
            if day[:8] == "fcst_day"}  # Create {'fcst_day_#': week-day}
    question = "Choisir le jour :\n"
    days_list = []  # Build ['fcst_day_#', week-day] sorted list
    # This i-loop is required because "days" is not sorted:
    for i in range(5):
        key = "fcst_day_{}".format(i)
        days_list.append([key, days[key]])
        question = question + "{}) {}\n".format(i, days[key])
    while True:
        try:
            choice = int(raw_input(question))  # Prompt user for day index
            return days_list[choice][0]  # Return 'fcst_day_#'
        except:
            print "Entrée non valide."


if __name__ == '__main__':
    # This block is not executed if this file is imported as a module
    city_json = get_city()  # get json dict from user input
    day_key = get_day(city_json)  # get day key from user input
    plot_day_tempe(city_json, day_key)  # plot day temperature evolution
