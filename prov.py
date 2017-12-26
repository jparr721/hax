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
    print("Script not started as root. Running sudo..")
    args = ['sudo', sys.executable] + sys.argv + [os.environ]
    # the next line replaces the currently-running process with the sudo
    os.execlpe('sudo', *args)

print("Running. Your euid is"+euid)

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
    elif (gofile.endswith("tar")):
        tar = tarfile.open(gofile, "r:")
        tar.extractall("/usr/local/go")
        tar.close()

    os.system("export GOROOT=/usr/local/go")
    os.system("mkdir $HOME/server")
    os.system("export GOPATH=$HOME/server")
    os.system("export PATH=$GOPATH/bin:$GOROOT/bin:$PATH")

    print("Verifying install...")
    os.system("go version")
    os.system("sleep 2")
    os.system("go env")
    print("If there are any defects, please remove the install from /usr/local/go and try again manually...")
    os.system("sleep 2")

    # Grab some repos if needed.
    os.system("python3 brogrammer.py")

    # Pick up some systems
    print("Need a web server? A database? We got that too!")
    print("======================OPTIONS=======================")
    print("Web Servers:")
    print("1 - Apache\t\t2 - Nginx")
    print("\n")
    print("Databases:")
    print("3 - MySql\t\t4 - Postgres\t\t5 - MongoDB")
    options = list()
    options = input("Select options: (Comma separated ex. 1,2,3)")
    numbers = options.split(',')
    for opt in options:
        os.system(packageManager+opt)
