#!/bin/bash
# /usr/local/bin/startscript.sh
sudo iwconfig wlan0 power off

while ! ( ifconfig wlan0 | grep "192.168.178.44" )
do
    echo WLAN wird verbunden
    # Warten auf Verbindung
done

sudo /etc/init.d/radiopi start
sleep 5
echo Radio ist gestartet
