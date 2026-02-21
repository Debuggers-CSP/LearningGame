---
layout: opencs
title: Maze - Ending Page
authors: Rishabh
permalink: /learninggame/ending/
disable_login_script: true
---

<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }

  /* Hide the global top header (the "Class of 2026" + wifi symbol bar) */
  body > header,
  body > nav,
  #header,
  .site-header,
  .top-bar,
  .topbar,
  .navbar,
  .navbar-container {
    display: none !important;
  }

  :root {
    --panel: rgba(15, 23, 42, 0.85);
    --panel-subtle: rgba(2, 6, 23, 0.55);
    --border-cyan: rgba(6,182,212,0.4);
    --border-emerald: rgba(16,185,129,0.3);
    --text: #e2e8f0;
    --muted: rgba(103,232,249,0.65);
    --warn: #fbbf24;
    --ok: #10b981;
    --bad: #ef4444;
  }

  body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #020617 0%, #0f172a 50%, #1e1b4b 100%);
    min-height: 100vh;
    width: 100%;
    overflow-x: hidden;
    overflow-y: auto;
    position: relative;
    padding: 24px;
    color: var(--text);
  }

  /* Background layers */
  .stars { position: fixed; inset: 0; overflow: hidden; z-index: 0; pointer-events: none; }
  .star { position: absolute; width: 2px; height: 2px; background: white; border-radius: 50%; animation: twinkle 3s infinite; }
  @keyframes twinkle { 0%, 100% { opacity: 0.3; } 50% { opacity: 1; } }

  body::before {
    content: '';
    position: fixed; top: 10%; left: 10%;
    width: 500px; height: 500px;
    background: radial-gradient(circle, rgba(6,182,212,0.15), transparent 70%);
    filter: blur(80px);
    z-index: 0;
    pointer-events: none;
  }
  body::after {
    content: '';
    position: fixed; bottom: 10%; right: 10%;
    width: 500px; height: 500px;
    background: radial-gradient(circle, rgba(168,85,247,0.15), transparent 70%);
    filter: blur(80px);
    z-index: 0;
    pointer-events: none;
  }

  .ending-root {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    position: relative;
    z-index: 2;
  }

  #endingPage {
    width: min(1200px, 96vw);
    min-height: calc(100vh - 48px);
    display: flex;
    flex-direction: column;
    gap: 18px;
  }

  .panel {
    background: var(--panel);
    backdrop-filter: blur(20px);
    border-radius: 24px;
    border: 2px solid var(--border-cyan);
    box-shadow: 0 0 60px rgba(6,182,212,0.22);
    overflow: hidden;
  }

  .title-section {
    width: 100%;
    background: rgba(15,23,42,0.95);
    padding: 14px 18px;
    border-bottom: 2px solid rgba(6,182,212,0.3);
  }

  .title-header { display: flex; align-items: center; justify-content: center; gap: 10px; margin-bottom: 6px; }
  .title { color: #06b6d4; font-size: 22px; font-weight: 900; text-transform: uppercase; letter-spacing: 4px; }
  .subtitle { text-align: center; color: var(--muted); font-size: 12px; font-family: 'Courier New', monospace; }

  .content {
    padding: 18px;
  }

  .summary-grid {
    display: grid;
    gap: 14px;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  }

  .card {
    background: var(--panel-subtle);
    border: 2px solid var(--border-emerald);
    border-radius: 20px;
    padding: 16px;
  }

  .card h2 {
    margin: 0 0 10px 0;
    font-size: 13px;
    color: var(--warn);
    letter-spacing: 1px;
    text-transform: uppercase;
  }

  .row { display: flex; justify-content: space-between; gap: 10px; padding: 6px 0; font-size: 12px; border-bottom: 1px solid rgba(148,163,184,0.12); }
  .row:last-child { border-bottom: none; }

  .status-pill {
    padding: 5px 12px;
    border-radius: 999px;
    background: rgba(6,182,212,0.12);
    border: 1px solid rgba(6,182,212,0.35);
    color: #dbeafe;
    font-weight: 800;
    font-size: 11px;
    white-space: nowrap;
  }

  .badge-grid { display: grid; gap: 10px; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); }
  .badge {
    background: rgba(2, 6, 23, 0.45);
    border: 1px solid rgba(6,182,212,0.28);
    border-radius: 14px;
    padding: 10px;
    font-size: 12px;
  }
  .badge.missing { opacity: 0.55; border-style: dashed; }

  table { width: 100%; border-collapse: collapse; font-size: 12px; }
  th, td { text-align: left; padding: 8px 6px; border-bottom: 1px solid rgba(148,163,184,0.14); }
  th { color: rgba(103,232,249,0.55); font-weight: 700; }

  .hidden { display: none; }

  /* Debug layout */
  .layout-grid {
    display: grid;
    grid-template-columns: 1.75fr 1fr;
    gap: 14px;
    margin-top: 14px;
    align-items: start;
  }
  @media (max-width: 980px) { .layout-grid { grid-template-columns: 1fr; } }

  .btn-row { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 10px; }

  .btn {
    padding: 10px 16px;
    border-radius: 12px;
    border: none;
    cursor: pointer;
    font-weight: 900;
    text-transform: uppercase;
    font-size: 11px;
    letter-spacing: 0.5px;
    transition: 0.2s ease;
  }
  .btn:hover { transform: translateY(-2px); }
  .btn-primary { background: linear-gradient(135deg, #06b6d4 0%, #3b82f6 100%); color: white; }
  .btn-ghost { background: transparent; border: 1px solid rgba(6,182,212,0.3); color: var(--text); }
  .btn-toggle { background: rgba(2,6,23,0.5); border: 1px solid rgba(6,182,212,0.25); color: var(--text); }
  .btn-toggle.active { border-color: rgba(16,185,129,0.7); box-shadow: 0 0 12px rgba(16,185,129,0.18); }

  .level-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 5px 10px;
    border-radius: 999px;
    border: 1px solid rgba(6,182,212,0.25);
    background: rgba(2,6,23,0.35);
    font-size: 11px;
    color: rgba(103,232,249,0.55);
  }
  .level-pill.active { border-color: rgba(16,185,129,0.7); color: #bbf7d0; }

  .code-block {
    background: rgba(2,6,23,0.55);
    border: 1px solid rgba(6,182,212,0.25);
    border-radius: 14px;
    padding: 14px;
    color: #e2e8f0;
    font-family: 'Courier New', monospace;
    font-size: 12px;
    white-space: pre-wrap;
    min-height: 120px;
    margin: 12px 0;
  }

  textarea {
    width: 100%;
    min-height: 140px;
    background: rgba(2, 6, 23, 0.7);
    color: #e2e8f0;
    border: 1px solid rgba(6,182,212,0.25);
    border-radius: 14px;
    padding: 12px;
    font-family: 'Courier New', monospace;
    font-size: 12px;
    outline: none;
  }
  textarea:focus { border-color: rgba(6,182,212,0.85); box-shadow: 0 0 0 3px rgba(6,182,212,0.14); }

  .status { margin-top: 10px; min-height: 18px; font-weight: 900; font-size: 12px; }
  .status.ok { color: var(--ok); }
  .status.err { color: var(--bad); }

  .locked { opacity: 0.55; pointer-events: none; }

  .chat-log {
    min-height: 200px;
    max-height: 300px;
    overflow-y: auto;
    background: rgba(2,6,23,0.45);
    border: 1px solid rgba(6,182,212,0.2);
    border-radius: 14px;
    padding: 14px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    font-size: 12px;
  }

  .chat-bubble { padding: 8px 10px; border-radius: 12px; max-width: 90%; line-height: 1.45; }
  .chat-user { background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16,185,129,0.3); align-self: flex-end; color: #d1fae5; }
  .chat-ai { background: rgba(59, 130, 246, 0.12); border: 1px solid rgba(59,130,246,0.25); align-self: flex-start; color: #e2e8f0; white-space: pre-line; }

  .chat-input { display: flex; gap: 8px; margin-top: 10px; }
  .chat-input input {
    flex: 1;
    background: rgba(2,6,23,0.7);
    color: #e2e8f0;
    border: 1px solid rgba(6,182,212,0.25);
    border-radius: 12px;
    padding: 10px 12px;
    font-size: 12px;
    outline: none;
  }
  .chat-input input:focus { border-color: rgba(6,182,212,0.85); box-shadow: 0 0 0 3px rgba(6,182,212,0.14); }
</style>

<div class="stars" id="stars"></div>

<div class="ending-root">
  <div id="endingPage">
    <!-- Summary Panel -->
    <div class="panel">
      <div class="title-section">
        <div class="title-header">
          <div style="font-size: 20px;">🏁</div>
          <div class="title">Final Stop Summary</div>
        </div>
        <div class="subtitle">Loading player progress from the backend…</div>
      </div>

      <div class="content">
        <div style="display:flex; justify-content: space-between; align-items:center; gap: 12px; margin-bottom: 14px;">
          <div style="color: rgba(103,232,249,0.65); font-family: 'Courier New', monospace; font-size: 12px;">
            Protocol status // live sync
          </div>
          <div class="status-pill" id="liveStatus">Live</div>
        </div>

        <div class="summary-grid">
          <div class="card" id="summaryLoading">
            <h2>Loading</h2>
            <div class="helper-text">Fetching player, badges, and score data.</div>
          </div>

          <div class="card hidden" id="summaryError">
            <h2>Error</h2>
            <div id="errorMessage">Unable to load data.</div>
          </div>

          <div class="card hidden" id="playerCard">
            <h2>Player</h2>
            <div class="row"><span>Name:</span> <strong id="playerName">-</strong></div>
            <div class="row"><span>ID:</span> <strong id="playerId">-</strong></div>
            <div class="row"><span>Class:</span> <strong id="playerClass">-</strong></div>
            <div class="row"><span>Joined:</span> <strong id="playerCreated">-</strong></div>
          </div>

          <div class="card hidden" id="scoreCard">
            <h2>Score Summary</h2>
            <div class="row"><span>Total Score:</span> <strong id="totalScore">0</strong></div>
            <div class="row"><span>Last Updated:</span> <strong id="scoreUpdated">-</strong></div>
          </div>

          <div class="card hidden" id="badgeCard">
            <h2>Badges Earned</h2>
            <div class="badge-grid" id="badgeGrid"></div>
          </div>

          <div class="card hidden" id="attemptsCard">
            <h2>Attempts & Completion</h2>
            <table>
              <thead>
                <tr>
                  <th>Stop</th>
                  <th>Attempts</th>
                  <th>Score</th>
                  <th>Completed At</th>
                </tr>
              </thead>
              <tbody id="attemptRows"></tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- Debug Panel -->
    <div class="panel">
      <div class="title-section">
        <div class="title-header">
          <div style="font-size: 20px;">🛠️</div>
          <div class="title">Debug Track</div>
        </div>
        <div class="subtitle">Action-Based Challenges + Hint Coach</div>
      </div>

      <div class="content">
        <div class="layout-grid">
          <div class="card">
            <h2>Choose Your Debug Level</h2>
            <div class="btn-row" id="debugLevelButtons">
              <button type="button" class="btn btn-toggle" data-level="beginner">🟢 Beginner</button>
              <button type="button" class="btn btn-toggle" data-level="intermediate">🟡 Intermediate</button>
              <button type="button" class="btn btn-toggle" data-level="hard">🔴 Hard</button>
              <button type="button" class="btn btn-primary" id="startDebug">Start Challenge</button>
            </div>
            <div style="margin-top: 10px; display: flex; gap: 10px; flex-wrap: wrap;">
              <span class="level-pill" id="levelStatus">Level: not selected</span>
              <span class="level-pill" id="badgeStatus">Badges: none</span>
            </div>

            <div style="margin-top: 14px;">
              <div style="color: rgba(103,232,249,0.65); font-family: 'Courier New', monospace; font-size: 12px; margin-bottom: 8px;">
                Debug the Code (Your Level)
              </div>
              <div id="debugProblemTitle" style="color: rgba(226,232,240,0.9); font-size: 12px; line-height: 1.55;">
                Select a level, then click Start Challenge to load your problem.
              </div>

              <pre class="code-block" id="debugCode">No problem loaded yet.</pre>
              <div id="debugPrompt" style="color: rgba(103,232,249,0.65); font-size: 12px; margin-bottom: 8px;"></div>
              <div style="color: rgba(226,232,240,0.75); font-size: 12px; margin-bottom: 8px;">
                Paste corrected code only. Sentences will be rejected.
              </div>

              <textarea id="debugAnswer" placeholder="Paste corrected code here..."></textarea>
              <div class="btn-row">
                <button class="btn btn-primary" id="submitDebug">Submit Fix</button>
                <button class="btn btn-ghost" id="clearDebug">Clear</button>
              </div>
              <div class="status" id="debugStatus"></div>
            </div>
          </div>

          <div class="card">
            <h2>Hint Coach Chatbot</h2>
            <div style="color: rgba(226,232,240,0.85); font-size: 12px; line-height: 1.55;">
              ChatBot provides 3 short hints first, then reveals the answer. If you paste code, it can run it in a sandbox and report output.
            </div>
            <div style="color: rgba(103,232,249,0.65); font-size: 12px; margin-top: 6px;">
              Guardrail: The answer is revealed only after 3 hints.
            </div>

            <div class="chat-log" id="chatLog" style="margin-top: 10px;">
              <div class="chat-bubble chat-ai">ChatBot: Tell me the level and what you think the bug is.</div>
            </div>

            <div class="chat-input">
              <input id="chatInput" type="text" placeholder="Ask for help (e.g., 'Where is the bug?')" />
              <button class="btn btn-primary" id="sendChat">Send</button>
            </div>

            <div style="margin-top: 14px; color: rgba(226,232,240,0.8); font-size: 12px; line-height: 1.55;">
              Algorithms process actions in order, loop per action, use decisions, update results, and output the final result.
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

  <script src="https://cdn.socket.io/4.7.5/socket.io.min.js"></script>
  <script>
    (function () {
      var params = new URLSearchParams(window.location.search);
      // Allow override via URL parameter, otherwise defaults to port 3000
      var apiPort = params.get('apiPort') || '3000';
      var API_BASE = window.location.protocol + '//' + window.location.hostname + ':' + apiPort;
      // Make backend optional - only use if explicitly enabled
      var useBackend = params.get('useBackend') === 'true' || false;
      
      var playerId = localStorage.getItem('learninggame_player_id') || localStorage.getItem('player_id') || params.get('playerId') || params.get('id');
      if (playerId) {
        try { localStorage.setItem('learninggame_player_id', playerId); } catch (e) { }
      }

    var summaryLoading = document.getElementById('summaryLoading');
    var summaryError = document.getElementById('summaryError');
    var errorMessage = document.getElementById('errorMessage');
    var playerCard = document.getElementById('playerCard');
    var scoreCard = document.getElementById('scoreCard');
    var badgeCard = document.getElementById('badgeCard');
    var attemptsCard = document.getElementById('attemptsCard');
    var liveStatus = document.getElementById('liveStatus');

    var playerName = document.getElementById('playerName');
    var playerIdEl = document.getElementById('playerId');
    var playerClass = document.getElementById('playerClass');
    var playerCreated = document.getElementById('playerCreated');
    var totalScore = document.getElementById('totalScore');
    var scoreUpdated = document.getElementById('scoreUpdated');
    var badgeGrid = document.getElementById('badgeGrid');
    var attemptRows = document.getElementById('attemptRows');

    function setLoading(isLoading) {
      if (isLoading) summaryLoading.classList.remove('hidden');
      else summaryLoading.classList.add('hidden');
    }

    function setError(message) {
      summaryError.classList.remove('hidden');
      errorMessage.textContent = message;
    }

    function showCards() {
      playerCard.classList.remove('hidden');
      scoreCard.classList.remove('hidden');
      badgeCard.classList.remove('hidden');
      attemptsCard.classList.remove('hidden');
    }

    function formatDate(value) {
      if (!value) return '-';
      var date = new Date(value);
      if (isNaN(date.getTime())) return value;
      return date.toLocaleString();
    }

    function fetchJson(url) {
      return fetch(url).then(function (res) {
        if (!res.ok) throw new Error('Request failed (' + res.status + ')');
        return res.json();
      });
    }

    function renderBadges(badges) {
      var allBadges = ['Stop 1 Badge', 'Stop 2 Badge', 'Stop 3 Badge', 'Stop 4 Badge', 'Stop 5 Badge'];
      var earnedMap = {};
      (badges || []).forEach(function (badge) {
        earnedMap[badge.badgeName] = badge;
      });
      badgeGrid.innerHTML = '';
      allBadges.forEach(function (name) {
        var badge = earnedMap[name];
        var div = document.createElement('div');
        div.className = 'badge' + (badge ? '' : ' missing');
        div.innerHTML = '<strong>' + name + '</strong><br>' + (badge ? 'Earned: ' + formatDate(badge.earnedAt) : 'Not earned');
        badgeGrid.appendChild(div);
      });
    }

    function renderAttempts(items) {
      attemptRows.innerHTML = '';
      if (!items || !items.length) {
        var emptyRow = document.createElement('tr');
        emptyRow.innerHTML = '<td colspan="4">No attempts recorded yet.</td>';
        attemptRows.appendChild(emptyRow);
        return;
      }
      items.forEach(function (item) {
        var row = document.createElement('tr');
        row.innerHTML =
          '<td>' + item.stopId + '</td>' +
          '<td>' + item.attempts + '</td>' +
          '<td>' + item.score + '</td>' +
          '<td>' + formatDate(item.completedAt) + '</td>';
        attemptRows.appendChild(row);
      });
    }

    function updateUI(playerData, badgeData, scoreData) {
      playerName.textContent = (playerData.player && playerData.player.display_name) || 'Unknown';
      playerIdEl.textContent = (playerData.player && playerData.player.id) || playerId;
      playerClass.textContent = (playerData.player && playerData.player.character_class) || '-';
      playerCreated.textContent = formatDate(playerData.player && playerData.player.created_at);

      totalScore.textContent = (scoreData.summary && scoreData.summary.totalScore != null) ? scoreData.summary.totalScore : 0;
      scoreUpdated.textContent = formatDate(scoreData.summary && scoreData.summary.updatedAt);

      renderBadges(badgeData.badges || []);
      renderAttempts(scoreData.perStop || []);
    }

      function loadAll() {
        if (!useBackend) {
          setLoading(false);
          setError('Backend is disabled. Add ?useBackend=true to URL to enable.');
          return;
        }
        if (!playerId) {
          setLoading(false);
          setError('Missing player id. Start the game to generate one.');
          return;
        }
        setLoading(true);
        summaryError.classList.add('hidden');

      var safeId = encodeURIComponent(playerId);
      Promise.all([
        fetchJson(API_BASE + '/player/' + safeId),
        fetchJson(API_BASE + '/player/' + safeId + '/badges'),
        fetchJson(API_BASE + '/player/' + safeId + '/score')
      ])
        .then(function (results) {
          updateUI(results[0], results[1], results[2]);
          showCards();
        })
        .catch(function () {
          setError('Failed to load player data. Ensure backend is running on ' + API_BASE);
        })
        .finally(function () {
          setLoading(false);
        });
    }

    function setupLiveUpdates() {
      if (!useBackend) {
        liveStatus.textContent = 'Offline';
        return;
      }
      try {
        var socket = io(API_BASE, {
          transports: ['websocket'],
          reconnection: false,
          timeout: 5000
        });
        socket.on('connect', function () { liveStatus.textContent = 'Live'; });
        socket.on('stateUpdate', function () { loadAll(); });
        socket.on('disconnect', function () { liveStatus.textContent = 'Offline'; });
        socket.on('connect_error', function () { liveStatus.textContent = 'Offline'; });
      } catch (e) {
        liveStatus.textContent = 'Offline';
      }
    }

    loadAll();
    setupLiveUpdates();
    if (useBackend) setInterval(loadAll, 15000);
  })();
</script>

<script>
  (function () {
    function byId(id) { return document.getElementById(id); }

    var debugLevelButtons = document.querySelectorAll('#debugLevelButtons [data-level]');
    var startDebug = byId('startDebug');
    var levelStatus = byId('levelStatus');
    var badgeStatus = byId('badgeStatus');
    var debugProblemTitle = byId('debugProblemTitle');
    var debugCode = byId('debugCode');
    var debugPrompt = byId('debugPrompt');
    var debugStatus = byId('debugStatus');
    var debugAnswer = byId('debugAnswer');
    var submitDebug = byId('submitDebug');
    var clearDebug = byId('clearDebug');
    var chatLog = byId('chatLog');
    var chatInput = byId('chatInput');
    var sendChat = byId('sendChat');

    function safeGetItem(key, fallback) {
      try { return localStorage.getItem(key); } catch (e) { return fallback; }
    }

    function safeSetItem(key, value) {
      try { localStorage.setItem(key, value); } catch (e) { }
    }

    var DEBUG_PROBLEMS = {
      beginner: [
        {
          id: 'b1',
          title: 'Beginner #1: Missing Colon',
          code: "def greet(name)\n    print('Hello ' + name)\n\ngreet('Ada')",
          prompt: 'Fix the syntax error and paste the corrected code.',
          expectedOutput: "Hello Ada",
          hints: [
            'Look at the function definition line for missing syntax.',
            'Python needs a colon after function headers.',
            'Make sure the print line is indented under the function.'
          ],
          answer: "def greet(name):\n    print('Hello ' + name)\n\ngreet('Ada')"
        }
      ],
      intermediate: [
        {
          id: 'i1',
          title: 'Intermediate #1: Off-by-One Loop',
          code: "nums = [2, 4, 6, 8]\nfor i in range(0, len(nums)):\n    print(nums[i])\nprint('done')",
          prompt: 'The loop should skip the first item and print only 4, 6, 8. Paste corrected code.',
          expectedOutput: "4\n6\n8\ndone",
          hints: [
            'The loop currently starts at index 0.',
            'To skip the first item, start the range at 1.',
            'Keep the end as len(nums) so you still include the last item.'
          ],
          answer: "nums = [2, 4, 6, 8]\nfor i in range(1, len(nums)):\n    print(nums[i])\nprint('done')"
        }
      ],
      hard: [
        {
          id: 'h1',
          title: 'Hard #1: Guard the Empty List',
          code: "def average(scores):\n    total = 0\n    for s in scores:\n        total += s\n    return total / len(scores)\n\nprint(average([]))",
          prompt: 'Handle the empty-list edge case and paste corrected code.',
          expectedOutput: "0",
          hints: [
            'Division by zero happens when the list is empty.',
            'Check len(scores) before dividing.',
            'Return 0 for the empty case.'
          ],
          answer: "def average(scores):\n    if not scores:\n        return 0\n    total = 0\n    for s in scores:\n        total += s\n    return total / len(scores)\n\nprint(average([]))"
        }
      ]
    };

      var selectedDebugLevel = safeGetItem('learninggame_debug_level', '') || '';
      var debugStarted = false;
      var currentDebugProblem = null;

    function getDebugBadges() {
      return JSON.parse(safeGetItem('learninggame_debug_badges', '[]') || '[]');
    }

    function saveDebugBadges(badges) {
      safeSetItem('learninggame_debug_badges', JSON.stringify(badges));
    }

    function renderDebugBadges() {
      var badges = getDebugBadges();
      badgeStatus.textContent = badges.length ? ('Badges earned: ' + badges.length + ' (' + badges.join(', ') + ')') : 'Badges: none';
    }

    function updateLevelStatus() {
      levelStatus.textContent = selectedDebugLevel ? ('Level: ' + selectedDebugLevel) : 'Level: not selected';
      if (selectedDebugLevel) levelStatus.classList.add('active');
      else levelStatus.classList.remove('active');

      for (var i = 0; i < debugLevelButtons.length; i += 1) {
        var btn = debugLevelButtons[i];
        if (btn.dataset.level === selectedDebugLevel) btn.classList.add('active');
        else btn.classList.remove('active');
      }
    }

    function setDebugLockState(locked) {
      if (debugAnswer) debugAnswer.disabled = locked;
      if (submitDebug) submitDebug.disabled = locked;
      if (clearDebug) clearDebug.disabled = locked;
    }

    function setDebugProblem(problem) {
      currentDebugProblem = problem;
      if (debugProblemTitle) debugProblemTitle.textContent = (problem && problem.title) ? problem.title : 'No problem loaded.';
      if (debugCode) debugCode.textContent = (problem && problem.code) ? problem.code : 'No problem loaded yet.';
      if (debugPrompt) debugPrompt.textContent = (problem && problem.prompt) ? problem.prompt : '';
    }

    function loadDebugProblem(level) {
      var problems = DEBUG_PROBLEMS[level] || [];
      var problem = problems[0] || null;
      setDebugProblem(problem);
    }

      function startDebugChallenge() {
        if (!selectedDebugLevel) {
          debugStatus.className = 'status err';
          debugStatus.textContent = 'Choose a level before starting.';
          return;
        }
        debugStarted = true;
        chatHintCount = 0;
        safeSetItem('learninggame_debug_level', selectedDebugLevel);
        loadDebugProblem(selectedDebugLevel);
        setDebugLockState(false);
        debugStatus.className = 'status ok';
        debugStatus.textContent = 'Challenge started: ' + selectedDebugLevel + '.';
        if (startDebug) startDebug.textContent = 'Restart Level';
      }

      function validateDebugAnswer(answer) {
        if (!currentDebugProblem) return false;
        var text = String(answer || '').toLowerCase();
        return isLikelyCode(text);
      }

    function completeDebugLevel() {
      var badges = getDebugBadges();
      var label = selectedDebugLevel.charAt(0).toUpperCase() + selectedDebugLevel.slice(1);
      if (badges.indexOf(label) === -1) {
        badges.push(label);
        saveDebugBadges(badges);
      }
      renderDebugBadges();
    }

    function appendChatBubble(text, type) {
      var bubble = document.createElement('div');
      bubble.className = 'chat-bubble ' + type;
      bubble.textContent = text;
      chatLog.appendChild(bubble);
      chatLog.scrollTop = chatLog.scrollHeight;
    }

    var chatHintCount = 0;
    function rolePrefix() { return 'ChatBot:'; }

    function isLikelyCode(text) {
      if (!text) return false;
      var t = text.toLowerCase();
      return (t.indexOf('def ') >= 0 || t.indexOf('print(') >= 0 || t.indexOf('for ') >= 0 || t.indexOf('return ') >= 0 || t.indexOf(':\n') >= 0);
    }

    function getHintOrAnswer() {
      if (!currentDebugProblem) {
        return rolePrefix() + ' Start a level and click Start Challenge so I can give hints.';
      }
      var hints = currentDebugProblem.hints || [];
      if (chatHintCount < 3 && chatHintCount < hints.length) {
        var hint = hints[chatHintCount];
        chatHintCount += 1;
        return rolePrefix() + ' Hint ' + chatHintCount + ' of 3: ' + hint;
      }
      return rolePrefix() + ' Answer (code):\n' + (currentDebugProblem.answer || 'No answer available.');
    }

    function getPythonRunnerBase() {
      var params = new URLSearchParams(window.location.search);
      var override = params.get('pythonRunner') || localStorage.getItem('python_runner_base');
      if (override) return override;
      return window.location.protocol + '//' + window.location.hostname + ':5001';
    }

      function runPythonRequest(code, callback) {
        var base = getPythonRunnerBase();
        fetch(base + '/api/run-python', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ code: code })
        })
          .then(function (response) {
            return response.json().then(function (data) {
              return { ok: response.ok, data: data };
            });
          })
          .then(function (result) {
            if (!result.ok || !result.data) {
              callback({ ok: false, error: 'Execution failed.' });
              return;
            }
            if (!result.data.ok) {
              callback({ ok: false, error: result.data.error || 'Execution failed.', data: result.data });
              return;
            }
            callback({ ok: true, data: result.data });
          })
          .catch(function () {
            callback({ ok: false, error: 'Python runner is offline at ' + base + '. Start python_backend/app.py on port 5001.' });
          });
      }

    function runPythonCode(code, callback) {
      runPythonRequest(code, function (result) {
        if (!result.ok) {
          callback(rolePrefix() + ' ' + result.error);
          return;
        }
        var stdout = result.data.stdout || '';
        var stderr = result.data.stderr || '';
        var replyParts = [];
        if (stdout.trim()) replyParts.push('Output:\n' + stdout.trim());
        if (stderr.trim()) replyParts.push('Error:\n' + stderr.trim());
        if (!replyParts.length) replyParts.push('No output.');
        callback(rolePrefix() + ' ' + replyParts.join('\n'));
      });
    }

    function chatbotReply(message) {
      var text = String(message || '').toLowerCase();
      if (isLikelyCode(text)) return rolePrefix() + ' Running your code...';
      if (!selectedDebugLevel) return rolePrefix() + ' Select a level first, then ask for a hint.';
      return getHintOrAnswer();
    }

      for (var i = 0; i < debugLevelButtons.length; i += 1) {
        debugLevelButtons[i].addEventListener('click', function (event) {
          selectedDebugLevel = event.currentTarget.dataset.level || '';
          updateLevelStatus();
          debugStatus.className = 'status';
          debugStatus.textContent = '';
          debugStarted = false;
          chatHintCount = 0;
          setDebugLockState(true);
          setDebugProblem(null);
          if (startDebug) startDebug.textContent = 'Start Challenge';
        });
      }

    if (startDebug) startDebug.addEventListener('click', startDebugChallenge);

      if (submitDebug) {
        submitDebug.addEventListener('click', function () {
          if (!debugStarted || !currentDebugProblem) {
            debugStatus.className = 'status err';
            debugStatus.textContent = 'Start the challenge to load a problem first.';
            return;
          }
          var answer = (debugAnswer && debugAnswer.value) ? debugAnswer.value.trim() : '';
          if (!answer) {
            debugStatus.className = 'status err';
            debugStatus.textContent = 'Paste your corrected code before submitting.';
            return;
          }
          if (!isLikelyCode(answer)) {
            debugStatus.className = 'status err';
            debugStatus.textContent = 'Code only. Please paste corrected Python code.';
            return;
          }
          debugStatus.className = 'status';
          debugStatus.textContent = 'Running code...';
          runPythonRequest(answer, function (result) {
            if (!result.ok) {
              debugStatus.className = 'status err';
              debugStatus.textContent = result.error || 'Execution failed.';
              return;
            }
            var stderr = result.data.stderr || '';
            if (stderr.trim()) {
              debugStatus.className = 'status err';
              debugStatus.textContent = 'Error: ' + stderr.trim();
              return;
            }
            var expected = currentDebugProblem && currentDebugProblem.expectedOutput ? String(currentDebugProblem.expectedOutput).trim() : '';
            var actual = (result.data.stdout || '').trim();
            if (expected && actual !== expected) {
              debugStatus.className = 'status err';
              debugStatus.textContent = 'Output mismatch. Expected:\n' + expected + '\nGot:\n' + (actual || '(no output)');
              return;
            }
            debugStatus.className = 'status ok';
            debugStatus.textContent = 'Correct ✅ Output matches. Badge earned for this level.';
            completeDebugLevel();
          });
        });
      }

    if (clearDebug) {
      clearDebug.addEventListener('click', function () {
        if (debugAnswer) debugAnswer.value = '';
        debugStatus.textContent = '';
        debugStatus.className = 'status';
      });
    }

    if (sendChat) {
      sendChat.addEventListener('click', function () {
        var message = chatInput.value.trim();
        if (!message) return;
        appendChatBubble(message, 'chat-user');
        chatInput.value = '';

        if (isLikelyCode(message)) {
          appendChatBubble(chatbotReply(message), 'chat-ai');
          runPythonCode(message, function (reply) { appendChatBubble(reply, 'chat-ai'); });
          return;
        }
        appendChatBubble(chatbotReply(message), 'chat-ai');
      });
    }

    updateLevelStatus();
    renderDebugBadges();
    setDebugLockState(true);
    setDebugProblem(null);
  })();
</script>
