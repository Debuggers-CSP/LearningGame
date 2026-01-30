---
layout: default
title: Neural Link - Hint Protocol
permalink: /learninggame/hints-instructions
---

<style>
    /* SPACE CADET THEME UI */
    body {
        background: linear-gradient(135deg, #020617 0%, #0f172a 50%, #1e1b4b 100%);
        color: white;
        font-family: 'Segoe UI', Tahoma, sans-serif;
        margin: 0;
        padding: 40px 20px;
        display: flex;
        justify-content: center;
    }

    .instruction-card {
        background: rgba(15, 23, 42, 0.9);
        backdrop-filter: blur(20px);
        border-radius: 24px;
        border: 2px solid rgba(6, 182, 212, 0.4);
        padding: 40px;
        max-width: 950px;
        box-shadow: 0 0 60px rgba(6, 182, 212, 0.25);
        position: relative;
    }

    /* Tech UI Accents */
    .instruction-card::before {
        content: "NEURAL LINK STATUS: ACTIVE // ENCRYPTED";
        position: absolute;
        top: 15px;
        right: 25px;
        font-family: 'Courier New', monospace;
        font-size: 10px;
        color: #10b981;
    }

    h1 { color: #06b6d4; text-transform: uppercase; letter-spacing: 4px; text-shadow: 0 0 15px rgba(6,182,212,0.5); margin-bottom: 5px; }
    .subtitle { color: #67e8f9; font-family: 'Courier New', monospace; font-size: 14px; margin-bottom: 30px; }
    
    h2 { color: #fbbf24; margin-top: 35px; border-bottom: 1px solid rgba(251,191,36,0.3); padding-bottom: 8px; font-size: 20px; }
    
    .step { 
        background: rgba(6, 182, 212, 0.05); 
        border-left: 4px solid #06b6d4; 
        padding: 20px; 
        margin: 20px 0;
        border-radius: 0 12px 12px 0;
    }

    .pt-badge { 
        background: #10b981; 
        color: white; 
        padding: 4px 12px; 
        border-radius: 999px; 
        font-size: 11px; 
        font-weight: 900; 
        text-transform: uppercase;
        margin-bottom: 10px; 
        display: inline-block; 
    }

    pre { 
        background: #020617; 
        padding: 15px; 
        border-radius: 12px; 
        border: 1px solid #1e293b; 
        color: #a5f3fc;
        font-family: 'Consolas', 'Courier New', monospace;
        font-size: 13px;
        overflow-x: auto;
    }

    code { color: #fbbf24; font-weight: bold; }
    
    .warning-box {
        background: rgba(239, 68, 68, 0.1);
        border: 1px solid #ef4444;
        padding: 15px;
        border-radius: 12px;
        color: #f87171;
        font-size: 13px;
        margin-top: 20px;
    }
</style>

<div class="instruction-card">
    <h1>🤖 Mission: Dynamic AI Hints</h1>
    <div class="subtitle">// ASSIGNED TO: CADET CYRUS // PROTOCOL: FULL-STACK API //</div>

    <p>Cadet Cyrus, your task is to implement the <strong>Neural Link Hint System</strong>. Currently, hints are static and hard-coded. You must move them to a database and use a 3rd-party API (or your own backend service) to fetch them dynamically. This ensures you satisfy the <strong>AP CSP Create PT</strong> requirements for Procedures, Lists, and Logic.</p>

    <div class="step">
        <span class="pt-badge">Skill B: Backend Storage</span>
        <h2>1. Store Hints in the DB (<code>model/robop_user.py</code>)</h2>
        <p>To avoid hard-coding, we need a table to store the hints for every module. Add this class to the bottom of <code>robop_user.py</code>:</p>
<pre>
class StationHint(db.Model):
    """Dynamic storage for Station hints - Satisfies 'List' requirement"""
    __tablename__ = "StationHint"
    id = db.Column(db.Integer, primary_key=True)
    _module_key = db.Column(db.String(64), nullable=False) # e.g. "s1_m1"
    _hint_list = db.Column(db.JSON, nullable=False)        # Stores a list of 3 hints

    def __init__(self, key, hints):
        self._module_key = key
        self._hint_list = hints
</pre>
    </div>

    <div class="step">
        <span class="pt-badge">Skill B: The API Procedure</span>
        <h2>2. Build the Logic Terminal (<code>api/robop_api.py</code>)</h2>
        <p>Create a <code>POST</code> route that receives a module key and returns a hint. This counts as your <strong>Procedure</strong> with <strong>Input/Output</strong>.</p>
<pre>
@robop_api.route("/get_hint", methods=["POST"])
def get_hint():
    data = request.get_json()
    module_key = data.get("module_key")
    current_attempt = data.get("attempt") # 0, 1, 2...

    # Fetch hint list from DB
    hint_entry = StationHint.query.filter_by(_module_key=module_key).first()
    
    # SELECTION LOGIC: Determine what to return based on attempt count
    if hint_entry and current_attempt < len(hint_entry._hint_list):
        return jsonify({"hint": hint_entry._hint_list[current_attempt]})
    else:
        return jsonify({"hint": "No more hints! Try your best."})
</pre>
    </div>

    <div class="step">
        <span class="pt-badge">Skill B: Iteration & Output</span>
        <h2>3. Connect the UI (<code>gameteacher.md</code>)</h2>
        <p>In your <code>toggleHint()</code> function, you must use <code>fetch()</code> to call your API. Use <strong>Iteration</strong> if you need to process multiple hints.</p>
<pre>
async function toggleHint() {
    const bubble = document.getElementById('help-bubble');
    
    // Logic to track how many times the user clicked the button
    if (!window.hintCount) window.hintCount = 0;

    // INPUT: POST to your new API
    const response = await fetch(`${window.API_URL}/get_hint`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
            module_key: `s${currentSectorNum}_m${currentQuestion}`,
            attempt: window.hintCount 
        })
    });

    const data = await response.json();
    
    // OUTPUT: Display the dynamic result
    bubble.innerText = data.hint;
    bubble.style.display = 'block';
    window.hintCount++;
}
</pre>
    </div>

    <div class="warning-box">
        <strong>⚠️ CRITICAL PT REMINDER:</strong> Cyrus, do not use the <code>teacherData</code> object inside <code>gameteacher.md</code> for your actual hints. That is a <strong>hard-coded data structure</strong> and will lose you points. All your hints MUST come from the database fetch.
    </div>

    <div style="text-align: center; margin-top: 40px;">
        <p style="font-size: 12px; opacity: 0.6; font-family: monospace;">
            CYRUS: Follow these steps to implement your feature. Once implemented, this instruction page can be removed.
        </p>
        <a href="{{ '/learninggame/home' | relative_url }}" style="color: #06b6d4; text-decoration: none; font-weight: bold; text-transform: uppercase; font-size: 14px;">← Return to Station Deck</a>
    </div>
</div>