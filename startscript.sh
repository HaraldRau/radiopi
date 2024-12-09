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

=======================================================================NEU============================================================================================

#!/bin/bash
# /usr/local/bin/startscript.sh

# WLAN-Energiesparmodus deaktivieren (optional)
sudo iwconfig wlan0 power off

# Überprüfen, ob eine Verbindung zur gewünschten IP-Adresse besteht
while ! (ifconfig wlan0 | grep -q "192.168.178.44")
do
    echo "WLAN wird verbunden..."
    sleep 2
done

# Sobald verbunden, den Radiopi-Dienst starten
echo "WLAN-Verbindung steht, starte RadioPi..."
sudo systemctl start radiopi

# Warten, um sicherzustellen, dass der Dienst läuft
sleep 5
sudo systemctl status radiopi

echo "RadioPi ist gestartet."
