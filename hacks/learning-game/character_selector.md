---
layout: default
title: Character Selection Protocol
permalink: /learninggame/character
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
        min-height: 100vh;
    }

    .instruction-card {
        background: rgba(15, 23, 42, 0.9);
        backdrop-filter: blur(20px);
        border-radius: 24px;
        border: 2px solid rgba(6, 182, 212, 0.4);
        padding: 40px;
        max-width: 900px;
        box-shadow: 0 0 60px rgba(6, 182, 212, 0.25);
        position: relative;
    }

    /* Tech UI Accents */
    .instruction-card::before {
        content: "STATUS: ENCRYPTED BEYOND PROTOCOL";
        position: absolute;
        top: 15px;
        right: 25px;
        font-family: monospace;
        font-size: 10px;
        color: #06b6d4;
        opacity: 0.6;
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

    ul { line-height: 1.6; color: #cbd5e1; }
    
    .nav-btn {
        display: inline-block;
        margin-top: 30px;
        padding: 15px 40px;
        background: linear-gradient(135deg, #06b6d4, #3b82f6);
        color: white;
        text-decoration: none;
        border-radius: 12px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 10px 20px rgba(6, 182, 212, 0.3);
        transition: 0.3s;
    }

    .nav-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 30px rgba(6, 182, 212, 0.5);
    }
</style>

<div class="instruction-card">
    <h1>🚀 Mission: Character Selector</h1>
    <div class="subtitle">// AUTHENTICATION SUCCESSFUL // REDIRECTING TO CADET CUSTOMIZATION //</div>

    <p>Cadet Shay, you have been assigned the <strong>Character Selection Feature</strong>. This page is the "hub" where users define their identity before entering the maze. To satisfy the <strong>AP CSP Create PT</strong>, you must build this using a Full-Stack approach.</p>

    <div class="step">
        <span class="pt-badge">Skill B: Database Persistence</span>
        <h2>1. Expand the Database (<code>model/robop_user.py</code>)</h2>
        <p>The <code>RobopUser</code> class needs new columns to hold the character data. Add these to the model:</p>
<pre>
# Add these columns to the RobopUser class
_character_name = db.Column(db.String(64), nullable=True)
_character_class = db.Column(db.String(64), nullable=True) # e.g. "Engineer"

# Important: Update to_dict() so the frontend can read these values
def to_dict(self):
    return {
        "uid": self._uid,
        "character_name": self._character_name,
        "character_class": self._character_class,
        # ... include your other existing fields here
    }
</pre>
    </div>

    <div class="step">
        <span class="pt-badge">Skill B: I/O Procedure</span>
        <h2>2. Build the API Communication (<code>api/robop_api.py</code>)</h2>
        <p>Implement a <code>POST</code> route that handles the "Input" (user choice) and provides "Output" (success message).</p>
<pre>
@robop_api.route("/update_character", methods=["POST"])
def update_character():
    uid = session.get("robop_uid")
    if not uid:
        return jsonify({"success": False, "message": "Unauthorized"}), 401
    
    data = request.get_json()
    user = RobopUser.query.filter_by(_uid=uid).first()
    
    # Selection Logic: Update the database object based on POST data
    user._character_name = data.get("name")
    user._character_class = data.get("class")
    
    db.session.commit()
    return jsonify({"success": True, "message": "Cadet profile synchronized!"}), 200
</pre>
    </div>

    <div class="step">
        <span class="pt-badge">Skill B: Iteration & Lists</span>
        <h2>3. Create the UI Logic (Frontend)</h2>
        <p>For the AP PT, you <strong>must</strong> use a List and Iteration. Do not hard-code 3 separate cards in HTML. Define them in a JavaScript array and loop through them to generate the UI.</p>
<pre>
// Define a List of cadet types
const cadetRoles = [
    { type: "Navigator", icon: "🛰️", trait: "Pathfinding +5" },
    { type: "Technician", icon: "🛠️", trait: "Logic +5" },
    { type: "Specialist", icon: "🧪", trait: "Science +5" }
];

// Iteration: Use a loop to render cards into an empty div
function renderRoles() {
    const container = document.getElementById('role-grid');
    cadetRoles.forEach(role => {
        // Build the HTML card here and append it!
    });
}
</pre>
    </div>

    <div class="step">
        <h2>4. Create PT Documentation Checklist</h2>
        <ul>
            <li><strong>Selection:</strong> Use <code>if</code> statements to validate that the user entered a name before clicking "Ready."</li>
            <li><strong>Iteration:</strong> The <code>forEach</code> loop above fulfills this requirement.</li>
            <li><strong>Input:</strong> The text input for the character name and the click event for the icon.</li>
            <li><strong>Output:</strong> The <code>fetch()</code> confirmation and the redirect to the Maze page.</li>
        </ul>
    </div>

    <div style="text-align: center; margin-top: 40px;">
        <a href="{{ '/learninggame/home' | relative_url }}" class="nav-btn">Development Bypass: Enter Maze →</a>
        <p style="margin-top: 25px; font-size: 11px; opacity: 0.5; font-family: monospace;">
            SHAY: Once you begin implementation, replace this instruction file with your actual UI code.
        </p>
    </div>
</div>