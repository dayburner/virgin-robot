#!/bin/bash
echo 'Getting files from github...'
wget https://github.com/dayburner/virgin-robot/archive/master.zip
echo 'Unzipping...'
unzip master.zip
echo 'Cleaning up...'
rm master.zip
echo 'Moving into virgin-robot-master dir...'
cd virgin-robot-master
echo 'Copy arduino sketch into dir...'
cp serial_sweep.ino /arduino_sketches/serial_sweep.ino
echo 'Copying wii.py to /'
sudo cp wii.py /wii.py
echo 'Copying rc.local to /etc/rc.local'
sudo cp rc.local /etc/rc.local
echo 'Copying update.sh to ~'
cp update.sh ~/update.sh
echo 'Updating apt-get...'
apt-get update
echo 'Upgrading packages...'
apt-get upgrade
echo 'Installing packages needed for robot...'
apt-get install --no-install-recommends bluetooth
apt-get install python-cwiid python-rpi.gpio python-serial arduino
echo 'Leaving virgin-robot-master dir...'
cd ..
echo 'Removing virgin-robot-master dir...'
sudo rm -r virgin-robot-master
echo 'Update complete'
