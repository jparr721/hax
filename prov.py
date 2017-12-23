#!/usr/bin/python
'''
Some scripts to provision servers or just a linux box.
Current Supported Distros:
Ubuntu,
Arch,
CentOS (soon)

Made by Jarred
'''

import os
import platform
import sys
import wget
import zipfile
import tarfile

# I'll figure out how to make this auto update
goUrl = "https://storage.googleapis.com/golang/go1.9.2.linux-amd64.tar.gz"

# Make sure it's running in sudo
euid = os.geteuid()
if euid != 0:
    print "Script not started as root. Running sudo.."
    args = ['sudo', sys.executable] + sys.argv + [os.environ]
    # the next line replaces the currently-running process with the sudo
    os.execlpe('sudo', *args)

print 'Running. Your euid is', euid

print("Provisionator, the only provisioning tool you need!")
print("1 - Ubuntu Server")
print("2 - Ubuntu Desktop")
print("3 - Arch Linux")
selection = int(input("Please select an option: "))

if (selection == 1 or selection == 2):
    packageManager = "apt-get update && apt-get install -y "
elif (selection == 3):
    packageManager = "pacman -S "

def beginInstall(packageManager, selection):
    if (selection == 1):
        print("Running Ubuntu Server Provision")
        serverInstall()
    elif (selection == 2):
        print("Running Ubuntu Desktop Provision")
    elif (selection == 3):
        print("Running Arch Linux Provision")

def serverInstall():
    # Grab the goods

    # Install golang (iz very nice)
    os.system("mkdir /usr/local/go")
    gofile = wget.download(goUrl, bar=bar_thermometer)
    if (gofile.endswith("tar.gz")):
        tar = tarfile.open(gofile, "r:gz")
        tar.extractall("/usr/local/go")
        tar.close()
    elif (gofile.endswith("tar"))
        tar = tarfile.open(gofile, "r:")
        tar.extractall("/usr/local/go")
        tar.close()

    os.system("export GOROOT=/usr/local/go")
    os.system("mkdir $HOME/server")
    os.system("export GOPATH=$HOME/server")
    os.system("export PATH=$GOPATH/bin:$GOROOT/bin:$PATH)

if __name__ == "__main__":
    beginInstall(distro[0])
