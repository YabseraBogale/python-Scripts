#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 16:36:13 2022

@author: yabsera
"""

import nmap
s=nmap.PortScanner()
print(s.scan('192.168.1.1','1-1023'))