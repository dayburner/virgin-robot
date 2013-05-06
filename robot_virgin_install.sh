#!/bin/bash
apt-get update
apt-get upgrade
apt-get install --no-install-recommends bluetooth
apt-get install python-cwiid python-rpi.gpio python-serial
wget https://github.com/simonmonk/raspirobotboard/archive/master.zip
unzip master.zip
cd raspirobotboard-master
python setup.py install
cp wii.py /wii.py
cp rc.local /etc/rc.local
cp interfaces /etc/network/interfaces
reboot

