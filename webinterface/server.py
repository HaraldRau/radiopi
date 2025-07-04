from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

# Erlaubte Befehle (Whitelist)
ALLOWED_COMMANDS = {
    "mocp_play": "mocp -p",
    "mocp_pause": "mocp -G",
    "mp3_list": "cat /home/hara/.moc/playlist.m3u | grep /home/ | sed 's|.*/||'",
    "mocp_liste": "bash /home/hara/radiopi/scripte/playliste",
    "mocp_titel": "mocp -Q%a&mocp -Q%t",
    "mocp_next": "mocp -f",
    "mocp_pre": "mocp -r",
    "mocp_info": "mocp -i",
    "mocp_for": "mocp --seek=10",
    "mocp_back": "mocp --seek=-10",
    "halt": "sudo halt -p",
    "status": "sudo systemctl status radiopi"
}

@app.route("/")
def index():
    return render_template("index.html")

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
