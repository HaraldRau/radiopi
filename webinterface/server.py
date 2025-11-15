from flask import Flask, render_template, request, jsonify
import os
import subprocess

app = Flask(__name__)

BASE_DIR = "/home/hara/musik"  # Startpunkt für Verzeichnis-Browser

# Erlaubte Befehle (Whitelist)
ALLOWED_COMMANDS = {
    "mocp_play": "mocp -p",
    "mocp_pause": "mocp -G",
    "mp3_list": "cat /home/hara/.moc/playlist.m3u | grep /home/ | sed 's|.*/||'",
    "mocp_titel": "mocp -Q%a&mocp -Q%t",
    "mocp_next": "mocp -f",
    "mocp_pre": "mocp -r",
    "mocp_info": "mocp -i",
    "mocp_for": "mocp --seek=10",
    "mocp_back": "mocp --seek=-10",
    "halt": "sudo halt -p",
    "status": "sudo systemctl status radiopi"
}

# === Player-Seite ===
@app.route("/")
def index():
    return render_template("index.html")

# === Verzeichnis-Browser-Seite ===
@app.route("/explorer")
def explorer():
    return render_template("verzeichnisbaum.html")
    
# === Rueckantwort ===

@app.route("/run", methods=["POST"])
def run_command():
    data = request.json  # JSON-Daten vom Client
    command_key = data.get("command")  # Befehl als key auslesen

    if command_key not in ALLOWED_COMMANDS:
        return jsonify({"error": "Nicht erlaubter Befehl!"}), 400

    try:
        output = subprocess.check_output(ALLOWED_COMMANDS[command_key], shell=True, text=True)
        return jsonify({"output": output})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)}), 500

# === Beispiel: API für Explorer (Ordnerlisten) ===
@app.route("/list-folders", methods=["GET"])
def list_folders():
    rel_path = request.args.get("path", "")
    if rel_path in (None, "undefined"):
        rel_path = ""

    current_path = os.path.normpath(os.path.join(BASE_DIR, rel_path))
    base_abs = os.path.abspath(BASE_DIR)
    curr_abs = os.path.abspath(current_path)

    if not curr_abs.startswith(base_abs):
        return jsonify({"error": "Pfad außerhalb erlaubt"}), 400

    try:
        items = os.listdir(curr_abs)
    except Exception as e:
        return jsonify({"error": str(e), "path": curr_abs}), 500

    folders = [f for f in items if os.path.isdir(os.path.join(curr_abs, f))]
    files = [f for f in items if os.path.isfile(os.path.join(curr_abs, f))]

    display_path = "" if curr_abs == base_abs else os.path.relpath(curr_abs, base_abs)
    return jsonify({"path": display_path, "folders": folders, "files": files})


# === API-Beispiel: Ausgabe des Pfads (später für mocp -a) ===
@app.route("/use-folder", methods=["POST"])
def use_folder():
    data = request.json
    rel_path = data.get("path", "")
    if not rel_path:
        return jsonify({"error": "Kein Pfad angegeben"}), 400

    folder_path = os.path.normpath(os.path.join(BASE_DIR, rel_path))
    base_abs = os.path.abspath(BASE_DIR)
    curr_abs = os.path.abspath(folder_path)

    if not curr_abs.startswith(base_abs):
        return jsonify({"error": "Pfad außerhalb erlaubt"}), 400

    return jsonify({"path": curr_abs})

# === API: Verzeichnis zur MOC-Playlist hinzufügen ===
@app.route("/add-folder", methods=["POST"])
def add_folder():
    data = request.json
    rel_path = data.get("path", "")
    if not rel_path:
        return jsonify({"error": "Kein Pfad angegeben"}), 400

    folder_path = os.path.normpath(os.path.join(BASE_DIR, rel_path))
    base_abs = os.path.abspath(BASE_DIR)
    curr_abs = os.path.abspath(folder_path)

    if not curr_abs.startswith(base_abs):
        return jsonify({"error": "Pfad außerhalb erlaubt"}), 400

    try:
        # Füge kompletten Ordner zur Playlist hinzu
        cmd = f'mocp -s && mocp -c && mocp -a "{curr_abs}" && mocp -p'
        subprocess.check_output(cmd, shell=True, text=True)
        return jsonify({"output": f"Ordner hinzugefügt: {curr_abs}"})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)}), 500
   

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
