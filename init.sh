#!bin/bash

echo "You must be root to run the init script"
sudo -v

# Sets up a very basic environment before running install scripts
# Right now this only supports arch and ubuntu. I'll add CentOS later.

# Get default package manager
if [ -f /etc/os-release ];
then
  . /etc/os-release
  OS=$NAME
  if [ OS = "Ubuntu" ];
  then
    PACMAN="apt-get update && apt-get install "
  elif [ OS = "Arch Linux" ];
  then
    PACMAN="pacman -S "
elif type lsb_release >/dev/null 2>&1;
then
  OS=$(lsb_release -si)
  VER=$(lsb_release -sr) # Super important for ubuntu
  PACMAN="apt-get update && apt-get install -y "
elif [ -f /etc/lsb-release ];
then
  # In case this version doesn't use lsb_release
  . /etc/lsb_release
  OS=$DISTRIB_ID
  VER=$DISTRIB_RELEASE
  PACMAN="apt-get update && apt-get install -y "
elif [ -f /etc/debian_version ];
then
  # For older debian versions
  OS=Debian
  VER=$(cat /etc/debian_version)
  PACMAN="apt-get update && apt-get install -y "
# Maybe I'll add redhat later


# Install a few base packages
eval "$PACMAN git vim python3"

# Execute install scripts (assumes same dir)
python3 prov.py
