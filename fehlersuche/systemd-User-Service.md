Ah, verstehe! Dein Dienst startet `mocp -S`, und du möchtest, dass dieser unter dem Benutzer `hara` läuft, anstatt als Root. Dafür gibt es mehrere Lösungen:

### **1. `su -c` verwenden (empfohlen)**
Falls du den Befehl als Root startest, kannst du `su` benutzen, um ihn unter dem User `hara` auszuführen:
```bash
su - hara -c "mocp -S"
```
Das startet `mocp -S` im Kontext des Benutzers `hara`.

Falls `hara` eine Login-Shell benötigt, kannst du auch:
```bash
sudo -u hara bash -c "mocp -S"
```

---

### **2. `sudo -u` (falls `hara` sudo-Rechte hat)**
Falls dein Benutzer `hara` in `/etc/sudoers` so konfiguriert ist, dass er Befehle ohne Passwort ausführen darf, kannst du:
```bash
sudo -u hara mocp -S
```

Falls `hara` kein sudo hat, kannst du das in der Datei `/etc/sudoers` (mit `visudo`) erlauben:
```
hara ALL=(ALL) NOPASSWD: /usr/bin/mocp
```
Dann kannst du den Befehl ohne Passwort starten.

---

### **3. Als systemd-User-Service (dauerhaft)**
Falls du möchtest, dass `mocp -S` automatisch als `hara` läuft, kannst du einen systemd-User-Dienst anlegen:

1. Erstelle die Datei:  
   ```
   mkdir -p /home/hara/.config/systemd/user
   nano /home/hara/.config/systemd/user/mocp.service
   ```

2. Inhalt der Datei:
   ```ini
   [Unit]
   Description=MOC Player Service
   After=network.target

   [Service]
   ExecStart=/usr/bin/mocp -S
   Restart=always
   User=hara
   WorkingDirectory=/home/hara

   [Install]
   WantedBy=default.target
   ```

3. Aktivieren und starten:
   ```bash
   systemctl --user daemon-reload
   systemctl --user enable mocp
   systemctl --user start mocp
   ```

Falls du `systemctl --user` als Root starten willst, dann:
```bash
sudo -u hara systemctl --user start mocp
```

Das sollte sicherstellen, dass `mocp` immer als User `hara` läuft. 🚀
