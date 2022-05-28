#!/bin/bash
mkdir $HOME/get-from-host $HOME/push-to-host
chmod +x start-client.sh
cp start-client.sh $PREFIX/bin/
echo "" >> $HOME/.bashrc
echo start-client.sh >> $HOME/.bashrc