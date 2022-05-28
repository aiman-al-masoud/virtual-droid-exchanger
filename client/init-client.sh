#!/bin/bash
# WARNING! this script ERASES AND OVERWRITES .bashrc !!!
mkdir $HOME/get-from-host $HOME/push-to-host
chmod +x start-client.sh
cp start-client.sh $PREFIX/bin/
echo "" > $HOME/.bashrc
echo 'start-client.sh > out.log 2> err.log' >> $HOME/.bashrc