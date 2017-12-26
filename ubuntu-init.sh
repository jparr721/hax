#!/bin/bash
# Ask for admin password
sudo -v

echo "Initializing..."
apt-get update && apt-get upgrade -y

echo "Creating settings..."
echo "Install pathogen..."
mkdir -p ~/.vim/autoload ~/.vim/bundle && curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim

echo "Adding syntax checking"
cd ~/.vim/bundle && \
git clone --depth=1 https://github.com/vim-syntastic/syntastic.git
mkdir ~/_install
git clone https://github.com/jparr721/doot-doot.git ~/_install

touch ~/.vimrc
ln -s ~/doot-doot/vimrc ~/.vimrc

echo "Load vim color scheme..."
cd ~/.vim/bundle && git clone https://github.com/ajmwagar/vim-deus.git

echo alias ll="ls -al" >> ~/.bashrc

sudo apt-get install -y python3

sudo pip3 install wget

sudo python3 prov.py
