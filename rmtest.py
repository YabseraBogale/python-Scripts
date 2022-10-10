#!/usr/bin/python3


import subprocess

command="rm hello.py"
check= subprocess.call(command,shell=True)
