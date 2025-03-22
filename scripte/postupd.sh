# !/bin/bash
echo "Aktionen nach git pull ausführen!"
# sudo cp /home/hara/radiopi/scripte/radiopi /etc/init.d/radiopi ENTFÄLLT
# sudo cp /home/hara/radiopi/scripte/config /root/.moc/config
# sudo cp /home/hara/radiopi/scripte/editplaylist /root/.moc/editplaylist&chmod +x /root/.moc/editplaylist
# sudo cp /home/hara/radiopi/scripte/startscript.sh /usr/local/bin/startscript.sh
# sudo cp /home/hara/radiopi/scripte/webpi.service /etc/systemd/system/webpi.service&systemctl daemon-reload
sudo /etc/init.d/radiopi restart&
