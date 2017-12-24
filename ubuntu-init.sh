#!/bin/bash
# Ask for admin password
sudo -v

echo "Initializing..."
apt-get update && apt-get upgrade -y

echo "Creating settings..."
echo "Install pathogen..."
mkdir -p ~/.vim/autoload ~/.vim/bundle && curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim

echo "Other superficial vim stuff..."
git clone https://github.com/scrooloose/nerdtree.git ~/.vim/bundle/nerdtree

cd ~/.vim/bundle && \
git clone --depth=1 https://github.com/vim-syntastic/syntastic.git
git clone https://github.com/jparr721/doot-doot.git ~

touch ~/.vimrc
ln -s ~/doot-doot/vimrc ~/.vimrc

echo "Load vim color scheme..."
cd ~/.vim/bundle && git clone https://github.com/ajmwagar/vim-deus.git

echo alias ll="ls -al" >> ~/.bashrc

sudo apt-get install -y python3

pip3 install wget

sudo python3 prov.py
