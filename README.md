<h3>Radio Pi</h3>

<img src="bilder/RadioPiKY040_Steckplatine.png" width="400">

<h4>Installation</h4>
<ul>
<li>sudo cp radiopi/startscript.sh /usr/local/bin/startscript.sh</li>
<li>Startscript nach /usr/local/bin/startscript.sh kopieren</li>
<li>Dienst nach /etc/init.d/radiopi kopieren</li>
<li>Dienst starten mit /etc/init.d/radiopi start</li>  
</ul>
<h4>Autostart</h4>
<p>...in der Konsole:
<code>sudo nano /etc/rc.local</code>
ausführen und die Datei bearbeiten!</p>
<p><code>#!/bin/sh -e
# rc.local
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
# In order to enable or disable this script just change the execution
# bits.
# By default this script does nothing.
# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
fi
<b># diese Zeile eintragen</b>
/usr/local/bin/startscript.sh # WLAN abfragen und starten
exit 0
</code></p>
<h4>Auto-Update</h4>
<ul>
  <li><code>git -C /home/hara/radiopi/ pull https://github.com/HaraldRau/radiopi.git</code></li>
  <li>Zeile in <code>startscript.sh</code> eintragen</li>
</ul>
<h4>moc Msuik on Console</h4>
<h5>Befehle</h5>
<ul>
  <li>mocp -S Server starten</li>
  <li>mocp -c löscht die aktuelle Playliste</li>
  <li>mocp -a /pfad/zur/msuik fügt das Verzeichnis zur aktuellen Playliste hinzu</li>
  <li>mocp -p spielt die aktuelle Playliste ab</li>
  <li>mocp -f spielt den nächsten Titel ab</li>
  <li>mocp -x beendet den Server</li>
  <li>mocp -h gibt die Hilfe aus</li>
</ul>
