#!/usr/bin/python
'''
Some scripts to provision servers.
Current Supported Distros:
Ubuntu,
Arch,
CentOS (soon)

Made by Jarred
'''

import os, platform

distro = platform.linux_distribution()

def beginInstall(distro):
    if distro == "arch":
        print("OS Detected: "+distro)
    elif distro == "ubuntu"

if __name__ == "__main__":
    beginInstall(distro[0])
