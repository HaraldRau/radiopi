from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

# Erlaubte Befehle (Whitelist)
ALLOWED_COMMANDS = {
    "mocp_play": "sudo mocp -p",
    "mocp_stop": "sudo mocp -P",
    "mp3_list": "ls /home/hara/musik/",
    "mocp_liste": "sudo mocp -c&sudo mocp -a /home/hara/musik/",
    "mocp_titel": "sudo mocp -Q%a&sudo mocp -Q%t",
    "mocp_next": "sudo mocp -f",
    "mocp_info": "sudo mocp -i",
    "halt": "sudo halt -p"
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
