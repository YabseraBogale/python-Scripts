#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 16:31:21 2022

@author: yabsera
"""

from requests import get
import json
from bs4 import BeautifulSoup
from pprint import pprint


def url(num):
    nasaapi="https://api.nasa.gov/techport/api/projects/"+str(num)+"?api_key=DEMO_KEY"
    return nasaapi
data=get(url(17795)).json()['project']
pprint(data['description'])
