# !/bin/bash
echo "Aktionen nach git pull ausführen!"
cp /home/hara/radiopi/scripte/config /home/hara/.moc/config
# cp /home/hara/radiopi/scripte/editplaylist /home/hara/.moc/editplaylist
# chmod +x /home/hara/.moc/editplaylist
# sudo cp /home/hara/radiopi/scripte/webpi.service /etc/systemd/system/webpi.service
# sudo cp /home/hara/radiopi/scripte/radiopi.service /etc/systemd/system/radiopi.service
sudo systemctl restart webpi
sudo systemctl restart radiopi
