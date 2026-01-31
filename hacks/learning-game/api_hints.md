---
layout: default
title: Neural Link - AI Hint Protocol
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

    .instruction-card::before {
        content: "3RD-PARTY AI STATUS: READY // NEURAL LINK: STANDBY";
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
    .file-path { color: #f472b6; font-family: monospace; font-weight: bold; }
</style>

<div class="instruction-card">
    <h1>🤖 Mission: AI Neural Link (Hints)</h1>
    <div class="subtitle">// INSTRUCTIONAL OVERRIDE FOR CADET CYRUS // OBJECTIVE: FULL-STACK AI INTEGRATION //</div>

    <p>Cadet Cyrus, your task is to implement the <strong>Station AI Neural Link</strong>. You will replace the old hard-coded hints with a system that uses an <strong>External 3rd Party AI</strong> to generate unique hints based on the actual question text on the user's screen. This data is then saved in our database to satisfy the Create PT requirements.</p>

    <!-- STEP 1 -->
    <div class="step">
        <span class="pt-badge">Task 1: Database (Skill B: List)</span>
        <p>Open <span class="file-path">model/robop_user.py</span>. Add this class at the very bottom. This table satisfies your <strong>List</strong> requirement by storing a collection of hint strings in JSON format.</p>
<pre>
class StationHint(db.Model):
    """Satisfies the 'List' requirement for the Create PT"""
    __tablename__ = "StationHint"
    id = db.Column(db.Integer, primary_key=True)
    _module_key = db.Column(db.String(64), unique=True, nullable=False) # e.g. "s1_m0"
    _hint_collection = db.Column(db.JSON, nullable=False) # Stores the list of AI hints

    def __init__(self, key, hints):
        self._module_key = key
        self._hint_collection = hints
</pre>
    </div>

    <!-- STEP 2 -->
    <div class="step">
        <span class="pt-badge">Task 2: AI Caller (Skill B: 3rd Party API)</span>
        <p>Open <span class="file-path">api/robop_api.py</span>. Add this <strong>Procedure</strong> at the bottom. This uses an AI (like Groq or OpenAI) to generate hints based on the question text.</p>
<pre>
import requests

def call_ai_api(question_text):
    # Setup your 3rd Party Link (Use Groq or OpenAI)
    api_key = "YOUR_API_KEY_HERE"
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    # Logic: Ask AI to help with the specific question
    prompt = f"Provide a list of 3 short hints for: {question_text}. Return ONLY a JSON list."
    
    response = requests.post(url, headers={"Authorization": f"Bearer {api_key}"}, json={
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": prompt}]
    })
    
    # Iteration: The AI returns a list we can iterate through later
    return response.json()['choices'][0]['message']['content']
</pre>
    </div>

    <!-- STEP 3 -->
    <div class="step">
        <span class="pt-badge">Task 3: The Route (Skill B: Selection)</span>
        <p>Still in <span class="file-path">api/robop_api.py</span>, add the <code>POST</code> route. It uses <strong>Selection</strong> (if/else) to decide whether to fetch from the DB or trigger the AI Procedure.</p>
<pre>
@robop_api.route("/get_hint", methods=["POST"])
def get_hint():
    data = request.get_json()
    key = data.get("module_key")
    q_text = data.get("question") # Grabs the question from the screen
    idx = data.get("attempt") 

    # SELECTION: Check if we have already saved these hints in our List
    entry = StationHint.query.filter_by(_module_key=key).first()
    
    if not entry:
        # If not in DB, call the 3rd Party AI Procedure
        new_hints = call_ai_api(q_text)
        entry = StationHint(key, new_hints) 
        db.session.add(entry)
        db.session.commit()

    # Output the specific hint requested
    return jsonify({"hint": entry._hint_collection[idx]})
</pre>
    </div>

    <!-- STEP 4 -->
    <div class="step">
        <span class="pt-badge">Task 4: Frontend (Skill B: Input/Output)</span>
        <p>Open <span class="file-path">gameteacher.md</span>. Replace your entire <code>toggleHint()</code> function. This captures the text from the screen and sends it to the AI.</p>
<pre>
let hintCounter = 0; // Local click tracker

async function toggleHint() {
    const bubble = document.getElementById('help-bubble');
    
    // ROTE LOGIC: Grab the question text automatically from the UI
    const qText = document.getElementById('moduleContent').innerText;

    // INPUT: Send the screen text and module key to the backend
    const response = await fetch(`${window.API_URL}/get_hint`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
            module_key: `s${currentSectorNum}_m${currentQuestion}`,
            question: qText,
            attempt: hintCounter 
        })
    });

    const data = await response.json();
    
    // OUTPUT: Display the AI result in the UI bubble
    bubble.innerText = data.hint;
    bubble.style.display = 'block';
    
    if (hintCounter < 2) hintCounter++; // Increment tracker
}
</pre>
    </div>

    <div style="background: rgba(16, 185, 129, 0.1); border: 1px solid #10b981; padding: 20px; border-radius: 12px; margin-top: 30px;">
        <h3 style="color: #10b981; margin-top: 0;">✅ Ready for the Professor</h3>
        <p style="font-size: 14px; margin-bottom: 0;">Cyrus, you now have: a <strong>Procedure</strong> (<code>call_ai_api</code>), a <strong>List</strong> (<code>_hint_collection</code>), <strong>Selection</strong> (<code>if not entry</code>), and <strong>Input/Output</strong> (the <code>POST</code> request). This is a perfect Full-Stack individual task.</p>
    </div>

    <div style="text-align: center; margin-top: 40px; border-top: 1px solid rgba(6,182,212,0.2); padding-top: 20px;">
        <a href="{{ '/learninggame/home' | relative_url }}" style="color: #06b6d4; text-decoration: none; font-weight: bold; text-transform: uppercase; font-size: 14px;">← Return to Station Deck</a>
    </div>
</div>