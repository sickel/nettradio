#!/usr/bin/python


import daemon as daemon

from buttons import read_buttons 

with daemon.DaemonContext():
    read_buttons()
