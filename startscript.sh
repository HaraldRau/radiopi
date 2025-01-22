#!/bin/bash
# /usr/local/bin/startscript.sh
sudo iwconfig wlan0 power off
cd /home/hara/radiopi/
git pull https://github.com/HaraldRau/radiopi.git
while ! ( ifconfig wlan0 | grep -q "192.168.178.44" )
do
    echo "WLAN wird verbunden"
    # Warten auf Verbindung
    sleep 1
done
sudo /etc/init.d/radiopi start
sleep 1
echo "Radio ist gestartet"
