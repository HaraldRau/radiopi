Das Problem könnte an mehreren Stellen liegen. Hier sind einige Dinge, die du überprüfen solltest:

### 1. **Pfad zu Python**
   Wenn du das Skript manuell mit `python /home/hara/radiopi/webinterface/server.py` startest, könnte es sein, dass `python` in deinem Terminal auf `python3` verweist. Dein Init-Skript könnte jedoch eine andere (ältere) Version von Python verwenden oder `python` ist nicht im `PATH`, wenn der Dienst läuft.

   **Lösung:** Ändere dein Init-Skript und nutze den absoluten Pfad zu Python:
   ```sh
   /usr/bin/python3 /home/hara/radiopi/webinterface/server.py
   ```
   Falls du dir nicht sicher bist, wo Python installiert ist, kannst du es mit folgendem Befehl herausfinden:
   ```sh
   which python3
   ```

### 2. **Berechtigungen & Umgebungsvariablen**
   Dienste laufen oft unter einem anderen Benutzer (z. B. `root` oder `nobody`). Prüfe, ob der Benutzer, unter dem der Dienst läuft, Zugriff auf `/home/hara/radiopi/webinterface/server.py` und dessen Abhängigkeiten hat.

   **Lösung:**
   - Teste, ob dein Skript läuft, wenn du es als `root` startest:
     ```sh
     sudo /usr/bin/python3 /home/hara/radiopi/webinterface/server.py
     ```
   - Falls nötig, setze Berechtigungen für das Skript:
     ```sh
     chmod +x /home/hara/radiopi/webinterface/server.py
     ```

### 3. **Fehlermeldungen prüfen**
   Es scheint, dass dein Init-Skript keine Fehler ausgibt. Um mehr über das Problem herauszufinden, leite die Ausgabe in eine Log-Datei um:
   ```sh
   /usr/bin/python3 /home/hara/radiopi/webinterface/server.py > /tmp/radiopi.log 2>&1
   ```
   Danach kannst du mit `cat /tmp/radiopi.log` nachsehen, ob dort Fehlermeldungen stehen.

### 4. **Port bereits belegt?**
   Falls dein Webserver bereits läuft oder ein anderer Dienst Port 8000 nutzt, kann dein Skript fehlschlagen.

   **Lösung:** Prüfe, ob Port 8000 bereits in Benutzung ist:
   ```sh
   netstat -tulnp | grep 8000
   ```
   Falls der Port belegt ist, kannst du ihn in `server.py` ändern:
   ```python
   app.run(host="0.0.0.0", port=8080, debug=False)
   ```

### 5. **Verwende `systemd` statt Init-Skript**
   Die klassische `init.d`-Methode ist veraltet. Ein `systemd`-Service wäre zuverlässiger. Erstelle eine Datei `/etc/systemd/system/radiopi.service` mit folgendem Inhalt:

   ```ini
   [Unit]
   Description=RadioPi Webserver
   After=network.target

   [Service]
   ExecStart=/usr/bin/python3 /home/hara/radiopi/webinterface/server.py
   WorkingDirectory=/home/hara/radiopi/webinterface
   Restart=always
   User=hara

   [Install]
   WantedBy=multi-user.target
   ```
   Dann aktiviere und starte den Dienst:
   ```sh
   sudo systemctl daemon-reload
   sudo systemctl enable radiopi
   sudo systemctl start radiopi
   sudo systemctl status radiopi
   ```

Falls dein Webserver nicht startet, kannst du mit `journalctl -u radiopi -n 50 --no-pager` nach Fehlern suchen.

Teste das mal und sag mir, was die Logs zeigen! 🚀
