#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 13:00:11 2022

@author: yabsera
"""

import crypt
def testpass(cryptpass):
    salt=cryptpass[0:2]
    dictfile=open('dictinory.txt',r)
    for word in dictfile,readlines():
        word=word.strip('\n')
        crytpword=crypt.crypt(word,salt)
        if(cryptword==cryptpass):
            print("[+] Found password",word,"\n")
            return word
    return "[-] Not Found password \n"
def main():
    passfile=open("password.txt")
    for line in passfile.readlines():
        if ":" in line:
            user=line.split(":")[0]
            cryptpass=line.split(":")[1].strip("\n")
            print("[*] Test for user",user)
            testpass(cryptpass)
if __name__=="__main__":
    main()