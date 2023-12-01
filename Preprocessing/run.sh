#!/bin/bash
cd "/media/eldrich-rikaze/New Volume/Style_transfer_assignment/Scratch__NN/raw_data" || exit

folder_name_arr=($(ls -d */))

cd "/media/eldrich-rikaze/New Volume/Style_transfer_assignment/Scratch__NN/" || exit
for element in "${folder_name_arr[@]}"; do

    python3 preprocessing.py "$element"
done
