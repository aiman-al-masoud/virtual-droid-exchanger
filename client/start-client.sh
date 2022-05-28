#!/bin/bash

# IP="127.0.0.1"  # for testing on host OS
IP="10.0.2.2" # deployed on VM
PORT="8000"
DEST_FOLDER=$HOME/get-from-host
SRC_FOLDER=$HOME/push-to-host

mkdir $DEST_FOLDER  $SRC_FOLDER

function download(){
    cd $DEST_FOLDER
    local PAGE="download-file"
    wget --quiet -O packet.zip http://${IP}:${PORT}/${PAGE}  2> buf.txt
    cat buf.txt
    rm buf.txt
    rm *log*
    unzip packet.zip
    cd -
}

function checkUpdates(){
    local PAGE="check-updates"
    wget  http://${IP}:${PORT}/${PAGE}  2> buf.txt
    cat check-updates
    rm *log*
    rm check-updates* buf.txt
}

function upload(){
    FILEPATH=$1
    local PAGE="upload-file"
    parts=($(echo ${FILEPATH} | tr "/" "\n"))
    FILENAME=${parts[-1]}
    curl -v -F FILEPATH=$FILEPATH -F upload=@$FILENAME "http://${IP}:${PORT}/${PAGE}"
}

function getFolderHash(){
    local FOLDER_PATH=$1
    zip tmp.zip $FOLDER_PATH > tmp.txt
    local res=$(sha1sum tmp.zip)
    rm tmp*
    echo $res
}


# MAIN

src_folder_hash=$(getFolderHash $SRC_FOLDER)

while true
do

    # check download 
    updated=$(checkUpdates)
    echo updated: $updated 

    if [ "$updated" = "True" ]; then
        yes | download
    fi

    # check upload 
    newHash=$(getFolderHash $SRC_FOLDER)
    if [ "$src_folder_hash" != "$newHash" ]; then

        # upload       
        cd $SRC_FOLDER
        for f in $(ls)
        do 
            upload $f
        done
        cd -
       
        src_folder_hash=$newHash
    fi 

    sleep 1
done













