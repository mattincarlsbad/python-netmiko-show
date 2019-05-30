#!/usr/bin/env python
from __future__ import print_function, unicode_literals

# Netmiko is the same as ConnectHandler
from netmiko import Netmiko
#from getpass import getpass

my_device = {
    "host": "10.0.0.1",
    "username": "admin",
    "password": "admin",
    "device_type": "arista_eos",
}

net_connect = Netmiko(**my_device)

output = net_connect.send_command("show version")
print(output)

net_connect.disconnect()
