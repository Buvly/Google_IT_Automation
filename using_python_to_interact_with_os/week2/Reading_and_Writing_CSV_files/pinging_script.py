#!/usr/bin/python3

import os

def ping_hosts():
    hosts = {"Google":"8.8.8.8", "Local_Host":"172.0.0.1"}

    for host, ip in hosts.items():
        pinging = os.system("ping -c 5 " + ip)
        if pinging == 0:
            print("Connection to {} is up".format(host))
        else:
            print("Connection to {} is down".format(host))
ping_hosts()

