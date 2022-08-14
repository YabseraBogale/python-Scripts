#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 10:44:32 2022

@author: yabsera
"""

from requests import get
import json
from pprint import pprint
url='https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
station =get(url).json()['items']
pprint(station)