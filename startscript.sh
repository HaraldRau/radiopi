#!/bin/bash
# /usr/local/bin/startscript.sh
sudo iwconfig wlan0 power off
while ! ( ifconfig wlan0 | grep -q "192.168.178.44" )
do
    echo "WLAN wird verbunden"
    # Warten auf Verbindung
    sleep 1
done
git -C /home/hara/radiopi/ pull https://github.com/HaraldRau/radiopi.git
sleep 1
sudo /etc/init.d/radiopi start
sleep 1
echo "Radio ist gestartet"
