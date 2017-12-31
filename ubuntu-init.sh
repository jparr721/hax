#!/bin/bash

# Make sure being ran as root
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root to install properly"
    exit 1
fi

# Install dependencies to make
# running other scripts go smoothly

sudo apt-get update && sudo apt-get install -y python3 python3-pip

pip3 install psycopg2 config wget

wget https://storage.googleapis.com/golang/go1.9.2.linux-amd64.tar.gz

echo "Extracting go to /usr/local/go..."
sudo tar -xvf go1.9.2.linux-amd64.tar.gz
sudo mv go /usr/local

echo "Establishing go paths"
export GOROOT=/usr/local/go

export GOPATH=$HOME/www

export PATH=$GOPATH/bin:$GOROOT/bin:$PATH

echo "Verifying install..."
echo "If go version does not show up, something is wrong"
go version
sleep(2)

echo "Verifying environment variables"
go env
sleep(2)
