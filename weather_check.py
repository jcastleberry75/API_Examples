#!/usr/bin/env python3


__author__ = "Jay Castleberry"
__version__ = "2.0.0"
__license__ = "MIT"


import os
import platform
import requests
import schedule
from colorama import *


def colors():
    # Initialize and define colors
    init(autoreset=True)
    global yellow
    yellow = Style.BRIGHT + Fore.YELLOW
    global cyan
    cyan = Style.BRIGHT + Fore.CYAN
    global red
    red = Style.BRIGHT + Fore.RED
    global green
    green = Style.BRIGHT + Fore.GREEN
    global white
    white = Style.BRIGHT + Fore.WHITE


def clear_screen():
    found_os = platform.system()
    win_os = 'Windows'
    if found_os is win_os:
        os.system('cls')
    else:
        os.system('clear')


def alerts():
    f = requests.get('http://api.wunderground.com/api/0f662307d1743416/alerts/q/pws:KGAATLAN215.json')
    alertdata = f.json()
    x = alertdata
    print()
    print()
    alert = (x['alerts'])
    if len(alert) == 0:
        print(cyan + 'There are no weather alerts at this time')
        print()
    else:
        y = (alert[0])
        print(red + '######  ' + y['description'] + '  ######')
        print()
        print()
        print(cyan + 'Expires: ' + y['expires'])
        print(cyan + y['message'])


def conditions():
    g = requests.get('http://api.wunderground.com/api/0f662307d1743416/conditions/q/pws:KGAATLAN215.json')
    conditiondata = g.json()
    conditions = conditiondata['current_observation']
    print()
    print(yellow + '######  Atlanta Weather ######')
    print()
    print(cyan + conditions['observation_time'])
    print(cyan + 'Observation Location:  ' + conditions['observation_location']['city'])
    print(cyan + 'Personal Weather Station:  ' + conditions['station_id'])
    print()
    print(cyan + 'Skies:  ' + conditions['weather'])
    print(cyan + 'Winds:  ' + conditions['wind_string'])
    print(cyan + 'Visibility: ' + conditions['visibility_mi'] + ' miles')
    print(cyan + 'Current Temperature:  ' + conditions['temperature_string'])
    print(cyan + 'Today\'s Precipitation: ' + conditions['precip_today_metric'])
    print(cyan + 'Past Hour Precipitation: ' + conditions['precip_1hr_string'])


def getweather():
    clear_screen()
    conditions()
    alerts()

colors()
getweather()
schedule.every(5).minutes.do(getweather)

while True:
    schedule.run_pending()
