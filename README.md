<h3>Radio Pi</h3>

<img src="bilder/RadioPiKY040_Steckplatine.png" width="400">

<h4>Installation</h4>
<ul>
<li>sudo systemctl start radiopi</li>
<li>sudo systemctl start radiopi</li>  
</ul>
<h4>Update</h4>
<p><code>git -C /home/hara/radiopi/ pull https://github.com/HaraldRau/radiopi.git</code></p>
<h4>Nach Update</h4>
<p>.git/hooks/post-merge</p>
<p><code>sudo cp /home/hara/radiopi/config /home/hara/.moc/config</code></p>
<p><code>sudo cp /home/hara/radiopi/editplaylist /home/hara/.moc/editplaylist</code></p>
<p><code>sudo chmod +x /home/hara/.moc/editplaylist</code></p>
<h4>Dienste installieren</h4>
<p>sudo cp /home/hara/radiopi/scripte/radiopi.service /etc/systemd/system/radiopi.service</p>
<p>systemctl --user daemon-reload</p>
<p>systemctl --user enable radiopi</p>
<p>systemctl --user start radiopi</p>
<h4>moc Musik on Console</h4>
<h5>Befehle</h5>
<ul>
  <li>mocp -S Server starten</li>
  <li>mocp -c löscht die aktuelle Playliste</li>
  <li>mocp -a /pfad/zur/musik fügt das Verzeichnis zur aktuellen Playliste hinzu</li>
  <li>mocp -p spielt die aktuelle Playliste ab</li>
  <li>mocp -f spielt den nächsten Titel ab</li>
  <li>mocp -x beendet den Server</li>
  <li>mocp -h gibt die Hilfe aus</li>
</ul>
