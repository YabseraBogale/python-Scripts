#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 20:49:51 2022

@author: yabsera
"""

import subprocess

command="ls"
check=subprocess.check_output(command,shell=True)
print(type(check))