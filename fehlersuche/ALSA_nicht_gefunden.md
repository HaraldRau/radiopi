Ja, dein Verdacht ist absolut plausibel: Der Fehler **„ALSA not available“ beim Start von `mocp -S`** kann sehr gut daran liegen, dass dein Dienst **`radiopi` vor dem vollständigen Initialisieren von ALSA gestartet wurde**.

---

### 💥 Typische Ursachen

1. **Zu früher Dienststart** – `radiopi` startet **nach `network.target`**, aber **nicht explizit nach `alsa-restore.service` oder `sound.target`**. Wenn `mocp` noch keinen Zugriff auf ALSA hat, schlägt der Start fehl.

2. **User-Dienst startet zu früh** – systemd-Userdienste wie deiner (für den Benutzer `hara`) können schneller starten als systemweite Dienste.

3. **Nicht persistente ALSA-Konfiguration** – falls `alsactl restore` noch nicht fertig war oder fehlgeschlagen ist, stehen Audiogeräte möglicherweise noch nicht bereit.

4. **USB-Audio-Gerät** – Falls du ein USB-Audio-Device nutzt, dauert die Initialisierung manchmal länger, vor allem bei Kaltstarts.

---

### ✅ Lösung: Dienst-Start verzögern, bis Sound verfügbar ist

Passe deine Service-Datei an, damit `radiopi` wirklich **erst nach ALSA** startet.

#### 🔧 Ergänze die Abhängigkeit zu `sound.target` und `alsa-restore.service`:

```ini
[Unit]
Description=RadioPi Webserver
After=network.target sound.target alsa-restore.service
Requires=sound.target

[Service]
ExecStart=python /home/hara/radiopi/radio.py
WorkingDirectory=/home/hara/radiopi
Restart=always
User=hara

[Install]
WantedBy=multi-user.target
```

> `After=` sorgt für die Reihenfolge.  
> `Requires=` sorgt dafür, dass `sound.target` beim Start von `radiopi` ebenfalls gestartet werden muss.

---

### 🔁 Neu laden und aktivieren

Nach Änderung:

```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl restart radiopi.service
```

---

### 🧪 Bonus: Startverzögerung als Fallback

Falls du ganz sicher gehen willst (z. B. bei USB-Soundkarten), kannst du im Python-Code am Anfang sowas ergänzen:

```python
import subprocess
import time

# Warte auf Soundgerät
for i in range(10):
    try:
        subprocess.check_call("aplay -l", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        break
    except subprocess.CalledProcessError:
        time.sleep(1)
```

Das wartet bis zu 10 Sekunden auf das Vorhandensein von Audiogeräten.

---

### ❓ Kurz zusammengefasst:
| Mögliche Ursache                        | Lösung                      |
|----------------------------------------|-----------------------------|
| `radiopi` startet zu früh              | `After=sound.target`        |
| ALSA noch nicht bereit                 | `Requires=sound.target`     |
| USB-Audiogerät braucht länger          | Startverzögerung im Code    |
| `alsa-restore.service` läuft spät      | `After=alsa-restore.service`|

---

Wenn du magst, kann ich dir auch ein Template für den Fall machen, dass `radiopi` als **User-Service** laufen soll (`~/.config/systemd/user/`) – je nachdem, wie du dein Setup lieber strukturierst.
