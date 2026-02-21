from flask import Flask, request, jsonify
import json
import os
import requests
import subprocess
import sys
import tempfile
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

MAX_CODE_CHARS = 2000
TIMEOUT_SECONDS = 2
DEEPSEEK_TIMEOUT_SECONDS = 12


def normalize_output(text):
    if text is None:
        return ""
    normalized = str(text).replace("\r\n", "\n").replace("\r", "\n")
    lines = normalized.split("\n")
    return "\n".join(line.rstrip() for line in lines).strip()


def evaluate_with_deepseek(code, expected_output, stdout, stderr, returncode):
    api_key = os.getenv("DEEPSEEK_API_KEY", "").strip()
    if not api_key:
        return None

    debug_api = os.getenv("DEBUG_EVAL_API", "").strip().lower() in {"1", "true", "yes", "on"}

    model = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
    endpoint = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1").rstrip("/") + "/chat/completions"

    expected_clean = normalize_output(expected_output)
    actual_clean = normalize_output(stdout)

    system_prompt = (
        "You are a strict Python code evaluator. "
        "Return only valid JSON with keys: passed (boolean), reason (string), actualOutput (string), expectedOutput (string)."
    )
    user_prompt = (
        "Evaluate whether the submitted Python solution is correct.\n"
        f"Expected output:\n{expected_clean}\n\n"
        f"Program return code: {returncode}\n"
        f"Program stdout:\n{stdout or ''}\n\n"
        f"Program stderr:\n{stderr or ''}\n\n"
        f"Submitted code:\n{code}\n\n"
        "Rules:\n"
        "1) If return code is non-zero, passed must be false.\n"
        "2) Compare normalized output semantics to expected output.\n"
        "3) Keep reason concise."
    )

    payload = {
        "model": model,
        "temperature": 0,
        "response_format": {"type": "json_object"},
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    }

    try:
        response = requests.post(
            endpoint,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=DEEPSEEK_TIMEOUT_SECONDS,
        )
        if debug_api:
            print("[DeepSeek API] status:", response.status_code)
            print("[DeepSeek API] body:", response.text)
        if response.status_code >= 400:
            return None

        response_data = response.json()
        content = (
            response_data.get("choices", [{}])[0]
            .get("message", {})
            .get("content", "")
        )
        if debug_api:
            print("[DeepSeek API] parsed content:", content)
        if not content:
            return None

        parsed = json.loads(content)
        return {
            "passed": bool(parsed.get("passed", False)),
            "reason": str(parsed.get("reason", "")).strip(),
            "actualOutput": normalize_output(parsed.get("actualOutput", actual_clean)),
            "expectedOutput": normalize_output(parsed.get("expectedOutput", expected_clean)),
            "usedDeepSeekEvaluation": True,
        }
    except Exception:
        return None


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response


@app.errorhandler(HTTPException)
def handle_http_exception(exc):
    return jsonify({"ok": False, "error": exc.description}), exc.code


@app.errorhandler(Exception)
def handle_unexpected_exception(exc):
    return jsonify({"ok": False, "error": str(exc) or "Internal server error."}), 500


@app.route("/api/run-python", methods=["POST", "OPTIONS"])
def run_python():
    if request.method == "OPTIONS":
        return ("", 204)

    data = request.get_json(silent=True) or {}
    code = data.get("code")
    if code is None:
        code = data.get("submittedCode", "")
    expected_output = data.get("expectedOutput")

    if not isinstance(code, str) or not code.strip():
        return jsonify({"ok": False, "error": "No code provided."}), 400

    if len(code) > MAX_CODE_CHARS:
        return jsonify({"ok": False, "error": "Code too long."}), 400

    if expected_output is not None and not isinstance(expected_output, str):
        return jsonify({"ok": False, "error": "expectedOutput must be a string."}), 400

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

        stdout = result.stdout or ""
        stderr = result.stderr or ""

        if result.returncode != 0:
            return jsonify({
                "ok": False,
                "error": stderr.strip() or "Python execution failed.",
                "stdout": stdout,
                "stderr": stderr,
                "returncode": result.returncode,
                "passed": False if expected_output is not None else None,
            }), 200

        if expected_output is not None:
            expected_clean = normalize_output(expected_output)
            actual_clean = normalize_output(stdout)
            eval_result = evaluate_with_deepseek(
                code=code,
                expected_output=expected_clean,
                stdout=stdout,
                stderr=stderr,
                returncode=result.returncode,
            )

            if eval_result is not None:
                passed = bool(eval_result["passed"])
                expected_clean = eval_result["expectedOutput"]
                actual_clean = eval_result["actualOutput"]
                eval_reason = eval_result.get("reason", "")
                used_deepseek = True
            else:
                passed = actual_clean == expected_clean
                eval_reason = ""
                used_deepseek = False

            return jsonify({
                "ok": True,
                "stdout": stdout,
                "stderr": stderr,
                "returncode": result.returncode,
                "expectedOutput": expected_clean,
                "actualOutput": actual_clean,
                "passed": passed,
                "evaluationReason": eval_reason,
                "usedDeepSeekEvaluation": used_deepseek,
            })

        return jsonify({
            "ok": True,
            "stdout": stdout,
            "stderr": stderr,
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
