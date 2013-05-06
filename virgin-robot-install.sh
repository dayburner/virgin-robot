#!/bin/bash
echo 'Copying wii.py to /'
cp wii.py /wii.py
echo 'Copying rc.local to /etc/rc.local'
cp rc.local /etc/rc.local
echo 'Updating apt-get'
apt-get update
echo 'Upgrading packages'
apt-get upgrade
echo 'Installing packages needed for robot'
apt-get install --no-install-recommends bluetooth
apt-get install python-cwiid python-rpi.gpio python-serial
echo 'Getting robot board files from github'
wget https://github.com/simonmonk/raspirobotboard/archive/master.zip
echo 'Unzip archive'
unzip master.zip
echo 'Remove zip file'
rm master.zip
cd raspirobotboard-master
echo 'Installing robot board files'
python setup.py install
cd ..
echo 'Cleaning up'
rm wii.py
rm rc.local
echo 'Rebooting...............'
reboot

