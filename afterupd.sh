# !/bin/bash
echo "Aktionen nach git pull ausführen!"
sudo /home/hara/radiopi/radiopi /etc/init.d/radiopi
# sudo cp /home/hara/radiopi/config /root/.moc/config
# sudo cp /home/hara/radiopi/editplaylist /root/.moc/editplaylist
# sudo chmod +x /root/.moc/editplaylist
# sudo cp /home/hara/radiopi/startscript.sh /usr/local/bin/startscript.sh
sudo /etc/init.d/radiopi restart&
