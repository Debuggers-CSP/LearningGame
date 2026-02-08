from flask import Flask, request, jsonify
import os
import subprocess
import sys
import tempfile

app = Flask(__name__)

MAX_CODE_CHARS = 2000
TIMEOUT_SECONDS = 2


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response


@app.route("/api/run-python", methods=["POST", "OPTIONS"])
def run_python():
    if request.method == "OPTIONS":
        return ("", 204)

    data = request.get_json(silent=True) or {}
    code = data.get("code", "")

    if not isinstance(code, str) or not code.strip():
        return jsonify({"ok": False, "error": "No code provided."}), 400

    if len(code) > MAX_CODE_CHARS:
        return jsonify({"ok": False, "error": "Code too long."}), 400

    temp_path = None
    try:
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as temp_file:
            temp_file.write(code)
            temp_path = temp_file.name

        result = subprocess.run(
            [sys.executable, temp_path],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
        )

        return jsonify({
            "ok": True,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode,
        })
    except subprocess.TimeoutExpired:
        return jsonify({"ok": False, "error": "Execution timed out."}), 408
    except Exception as exc:
        return jsonify({"ok": False, "error": str(exc)}), 500
    finally:
        if temp_path and os.path.exists(temp_path):
            try:
                os.remove(temp_path)
            except OSError:
                pass


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=False)
