#!/usr/bin/python3
'''
Jeeves
- A tool to manage dependencies for services installed manually

Supported Distros:
* Ubuntu
* Arch
* CentOS

Made by Jarred
'''

import os
import platform
import sys
import wget
import zipfile
import tarfile
import argparse

os.system("mkdir /var/log/jeeves")

installfileLocation = '/var/log/jeeves'

def freshInstall():
    print("Running fresh install...")
    os.system("touch jeeves.txt /var/log/jeeves")

def update():
    # Read log file for dependencies
    print("Updating dependencies")

def usage():
    print("jeeves server setup utility and dependency manager")
    print("\nOptions must be a mode specifier")
    print("-f Fresh -u Update -d Delete -i Installed")
    print("Fresh: jeeves -f [options] [package names] | [logfile]")
    print("\t-u Ubuntu -a Arch -c CentOS")
    print("Update: jeeves -u [options] [logfile] | [names]") # Update existing packages
    print("\t-a Add a new package -m Maintain package(s)")
    print("Delete: jeeves -d [options] [logfile] | [names]")
    print("\t-a Remove all -s Remove single -m Remove multiple")
    print("jeeves v0.1.0")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Jeeves, the dependency tracker")
    parser.add_argument("-f", "--fresh", action="freshInstall",
                        help="Fresh install. This removes previous data and re installs")
    parser.add_argument("-u", "--update", action="append",
                        help="Updates all packages, or selected")
    parser.add_argument("-d", "--delete", action="append")
