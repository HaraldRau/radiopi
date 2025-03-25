Danke für die Fehlermeldung! Die gute Nachricht: `mocp -S` startet grundsätzlich erfolgreich (`status=0/SUCCESS`). Das Problem ist aber, dass **`mocp` sofort wieder beendet wird**, und `systemd` denkt dann, es ist abgestürzt und versucht ständig, es neu zu starten → dadurch bekommst du den Fehler:  
> `Start request repeated too quickly`  
→ Das nennt man einen **"Restart-Loop"** und endet in `start-limit-hit`.

---

## 🔧 Lösung: `Type=forking` + kein `Restart=always`

### Warum passiert das?

- `mocp -S` **startet einen Hintergrunddienst** (den MOC-Server) und **beendet sich selbst sofort wieder**.
- systemd erwartet standardmäßig (`Type=simple`), dass der Prozess aktiv bleibt.  
  → Da `mocp -S` aber direkt endet, denkt systemd: „Oh nein, abgestürzt!“, und startet es neu.

---

## ✅ Richtige Konfiguration für `mocp`

### Bearbeite `/etc/systemd/system/mocplay.service`:
```ini
[Unit]
Description=MOC Player
After=network.target sound.target

[Service]
Type=forking
User=hara
ExecStart=/usr/bin/mocp -S
ExecStop=/usr/bin/mocp -x
Restart=no
WorkingDirectory=/home/hara

[Install]
WantedBy=multi-user.target
```

### Dann:
```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl reset-failed
sudo systemctl start mocplay
```

---

### 🔍 Was du mit dieser Konfiguration erreichst:

- `Type=forking`: systemd weiß, dass der Prozess sich selbst in den Hintergrund forkt.
- `Restart=no`: verhindert die Restart-Schleife.
- `User=hara`: führt `mocp` als User `hara` aus (wichtig!).

---

Wenn du willst, kann ich dir auch ein komplettes Beispiel mit Logging bauen (z. B. Ausgabe in `/home/hara/moc.log`). Sag Bescheid!
