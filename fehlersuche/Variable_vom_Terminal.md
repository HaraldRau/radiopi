Fast – aber nicht ganz! 😊

Mit `os.system()` kannst du zwar einen Befehl ausführen, **aber**: Die **Ausgabe** des Befehls wird nur im Terminal angezeigt – **nicht** als Rückgabewert zurückgegeben. `os.system()` gibt **nur den Exit-Code** des Befehls zurück.

Wenn du die Ausgabe eines Befehls in eine **Variable** schreiben möchtest, benutzt du besser das Modul `subprocess`.

### Beispiel mit `subprocess`:
```python
import subprocess

liste = subprocess.check_output(['mocp' ,'-i']).decode('utf-8')
print(liste[18:25])
```

### Erklärung:
- `subprocess.check_output()` führt den Befehl aus und gibt die Ausgabe zurück.
- `.decode('utf-8')` wandelt die **Byte-Ausgabe** in einen normalen String um.

### Optional: Wenn du die Ausgabe zeilenweise willst
```python
liste = subprocess.check_output(['mocp' ,'-i']).decode('utf-8').splitlines()
print(zeile[1])
```

Willst du eine Alternative mit `os.popen()` sehen? Die geht auch, ist aber veraltet.
