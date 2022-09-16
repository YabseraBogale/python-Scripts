#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 10:08:16 2022
'Abyss Apocalypso', 9234865, '7fa06552cf94eb2f0387904fd716f14f'
@author: yabsera
"""

from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
import pandas as pd
import traceback
import time
import random
 
api_id = 9234865
api_hash = '7fa06552cf94eb2f0387904fd716f14f'
phone = '+251966114242'
client = TelegramClient(phone, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

### making user list
input_file = pd.read_csv('stmary.csv')
users=[]
row=0
while row < len(input_file):
    user = {}
    user['username'] = input_file['username'][row]
    user['full name'] = input_file['full name'][row]
    user['user id'] = input_file['user id'][row]
    user['phone number'] = "+" + str(input_file['phone number'][row])
    users.append(user)
    row+=1
target_channel = InputPeerChannel(1562041979,5791991286168741736)
user0=client.get_input_entity(users[6]['username'])
client(InviteToChannelRequest(target_channel,[user0]))
"""
    
target_group_entity = InputPeerChannel(target_group.id,target_group.access_hash)



"""















