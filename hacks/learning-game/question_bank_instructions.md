---
layout: default
title: Logic Core - AI Question Bank
permalink: /learninggame/pseudo-instructions
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
        border: 2px solid rgba(168, 85, 247, 0.4);
        padding: 40px;
        max-width: 950px;
        box-shadow: 0 0 60px rgba(168, 85, 247, 0.25);
        position: relative;
    }

    .instruction-card::before {
        content: "LOGIC CORE: DYNAMIC MODE // AI OVERRIDE ACTIVE";
        position: absolute; top: 15px; right: 25px;
        font-family: 'Courier New', monospace; font-size: 10px; color: #a855f7;
    }

    h1 { color: #a855f7; text-transform: uppercase; letter-spacing: 4px; text-shadow: 0 0 15px rgba(168,85,247,0.5); }
    .subtitle { color: #d8b4fe; font-family: 'Courier New', monospace; font-size: 14px; margin-bottom: 30px; }
    
    h2 { color: #fbbf24; margin-top: 35px; border-bottom: 1px solid rgba(251,191,36,0.3); padding-bottom: 8px; font-size: 20px; }
    
    .step { 
        background: rgba(168, 85, 247, 0.05); 
        border-left: 4px solid #a855f7; 
        padding: 20px; margin: 20px 0;
        border-radius: 0 12px 12px 0;
    }

    .pt-badge { 
        background: #10b981; color: white; padding: 4px 12px; border-radius: 999px; 
        font-size: 11px; font-weight: 900; text-transform: uppercase; margin-bottom: 10px; display: inline-block; 
    }

    pre { 
        background: #020617; padding: 15px; border-radius: 12px; border: 1px solid #1e293b; 
        color: #e9d5ff; font-family: 'Consolas', monospace; font-size: 13px; overflow-x: auto;
    }

    code { color: #fbbf24; font-weight: bold; }
    .file-path { color: #f472b6; font-family: monospace; font-weight: bold; }
</style>

<div class="instruction-card">
    <h1>🧠 Mission: Dynamic Pseudocode Bank</h1>
    <div class="subtitle">// ASSIGNED TO: CADET MERYL // PROTOCOL: AI-GENERATED LOGIC TASKS //</div>

    <p>Cadet Meryl, you must implement the <strong>Dynamic Logic Bank</strong>. Currently, station pseudocode tasks are hard-coded. You will build a system that uses an <strong>AI API</strong> to generate unique coding challenges, templates, and test cases. This fulfills all <strong>AP CSP Create PT</strong> requirements for full-stack integration.</p>

    <!-- STEP 1 -->
    <div class="step">
        <span class="pt-badge">Task 1: Database (Skill B: List)</span>
        <p>Open <span class="file-path">model/robop_user.py</span>. Add this class to the bottom. This table acts as your <strong>List</strong> by storing a collection of AI-generated coding tasks.</p>
<pre>
class LogicTask(db.Model):
    __tablename__ = "LogicTask"
    id = db.Column(db.Integer, primary_key=True)
    _sector_id = db.Column(db.Integer, unique=True, nullable=False)
    _prompt = db.Column(db.Text, nullable=False)    # e.g. "Create a loop..."
    _template = db.Column(db.Text, nullable=False)  # e.g. "function solve() {..."
    _test_args = db.Column(db.JSON, nullable=False) # e.g. [10, 20]
    _expected = db.Column(db.JSON, nullable=False)  # e.g. 30

    def __init__(self, sector, prompt, template, args, expected):
        self._sector_id = sector
        self._prompt = prompt
        self._template = template
        self._test_args = args
        self._expected = expected
</pre>
    </div>

    <!-- STEP 2 -->
    <div class="step">
        <span class="pt-badge">Task 2: AI Procedure (Skill B: 3rd Party API)</span>
        <p>Open <span class="file-path">api/robop_api.py</span>. Add this <strong>Procedure</strong> to call the AI. It uses 3rd-party intelligence to build a valid coding problem.</p>
<pre>
import requests, json

def fetch_ai_logic(sector_num):
    api_key = "YOUR_API_KEY"
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    # Logic: Ask AI for a JSON-formatted coding task
    prompt = f"Generate an AP CSP pseudocode task for Sector {sector_num}. Return ONLY JSON with keys: 'prompt', 'template', 'args' (list), and 'expected'."
    
    response = requests.post(url, headers={"Authorization": f"Bearer {api_key}"}, json={
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": prompt}],
        "response_format": {"type": "json_object"}
    })
    
    # Iteration: If the AI returns text, you can use a loop to clean the strings
    return json.loads(response.json()['choices'][0]['message']['content'])
</pre>
    </div>

    <!-- STEP 3 -->
    <div class="step">
        <span class="pt-badge">Task 3: The Route (Skill B: Selection)</span>
        <p>Still in <span class="file-path">api/robop_api.py</span>, add the <code>POST</code> route. It uses <b>Selection</b> to either fetch from the DB or trigger the AI generation.</p>
<pre>
@robop_api.route("/get_logic_task", methods=["POST"])
def get_logic_task():
    data = request.get_json()
    sid = data.get("sector_id")

    # SELECTION: Check if challenge is already in our DB List
    task = LogicTask.query.filter_by(_sector_id=sid).first()
    
    if not task:
        # PROCEDURE: Generate from AI if not found
        ai = fetch_ai_logic(sid)
        task = LogicTask(sid, ai['prompt'], ai['template'], ai['args'], ai['expected'])
        db.session.add(task)
        db.session.commit()

    return jsonify({
        "prompt": task._prompt,
        "template": task._template,
        "args": task._test_args,
        "expected": task._expected
    })
</pre>
    </div>

    <!-- STEP 4 -->
    <div class="step">
        <span class="pt-badge">Task 4: Frontend (Skill B: Input/Output)</span>
        <p>Open <span class="file-path">homescreen.md</span>. Update <code>renderPseudoCode</code> and <code>checkPseudo</code> to handle the AI data. This makes the UI fully dynamic.</p>
<pre>
async function renderPseudoCode() {
    // INPUT: Fetch the dynamic task
    const response = await fetch(`${window.API_URL}/get_logic_task`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ sector_id: currentSectorNum })
    });
    const task = await response.json();

    // Store the expected answer globally for the checker
    window.currentExpected = task.expected;
    window.currentArgs = task.args;

    // OUTPUT: Inject AI data into the modal
    mContent.innerHTML = `
        &lt;p&gt;${task.prompt}&lt;/p&gt;
        &lt;textarea id="pcCode"&gt;${task.template}&lt;/textarea&gt;
        &lt;button class="btn" onclick="checkPseudo()"&gt;Validate&lt;/button&gt;
    `;
}

// Update checkPseudo to use the window variables!
function checkPseudo() {
    const code = document.getElementById('pcCode').value;
    const fn = eval(`(${code})`);
    const result = fn(...window.currentArgs);
    
    if (JSON.stringify(result) === JSON.stringify(window.currentExpected)) {
        // SUCCESS logic here
    }
}
</pre>
    </div>

    <div style="background: rgba(16, 185, 129, 0.1); border: 1px solid #10b981; padding: 20px; border-radius: 12px; margin-top: 30px;">
        <h3 style="color: #10b981; margin-top: 0;">🚀 Individual Task Summary (Meryl)</h3>
        <p style="font-size: 14px; margin-bottom: 0;">Meryl, you have implemented a <strong>Procedure</strong> (<code>fetch_ai_logic</code>), a <strong>List</strong> (the <code>LogicTask</code> table), <strong>Selection</strong> (to avoid repeat AI calls), and <strong>Input/Output</strong> (communicating logic between the AI and the Station UI).</p>
    </div>

    <div style="text-align: center; margin-top: 40px; border-top: 1px solid rgba(148,163,184,0.2); padding-top: 20px;">
        <a href="{{ '/learninggame/home' | relative_url }}" style="color: #a855f7; text-decoration: none; font-weight: bold; text-transform: uppercase; font-size: 14px;">← Return to Station Deck</a>
    </div>
</div>