<h3>Radio Pi</h3>

<img src="bilder/RadioPiKY040_Steckplatine.png" width="400">

<h4>Installation</h4>
<ul>
<li>sudo cp radiopi/startscript.sh /usr/local/bin/startscript.sh</li>
<li>Startscript nach /usr/local/bin/startscript.sh kopieren</li>
<li>Dienst nach /etc/init.d/radiopi kopieren</li>
<li>Dienst starten mit /etc/init.d/radiopi start</li>  
</ul>
<h4>Update</h4>
<ul>
  <li><code>@reboot		hara	git -C /home/hara/radiopi/ https://github.com/HaraldRau/radiopi.git</code></li>
  <li>Zeile in <code>sudo nano /etc/crontab eintragen</code></li>
</ul>
