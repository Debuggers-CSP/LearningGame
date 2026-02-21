---
layout: opencs
title: Character Selection Protocol
permalink: /learninggame/character
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

  body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #020617 0%, #0f172a 50%, #1e1b4b 100%);
    min-height: 100vh;
    width: 100%;
    overflow-x: hidden;
    overflow-y: auto;
    position: relative;
    padding: 24px;
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

  .learninggame-root{
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    position: relative;
    z-index: 2;
  }

  .container {
    position: relative;
    width: min(900px, 95vw);
    background: rgba(15, 23, 42, 0.85);
    backdrop-filter: blur(20px);
    border-radius: 24px;
    border: 2px solid rgba(6,182,212,0.4);
    box-shadow: 0 0 60px rgba(6,182,212,0.25);
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }

  .title-section {
    width: 100%;
    background: rgba(15,23,42,0.95);
    padding: 14px 18px;
    border-bottom: 2px solid rgba(6,182,212,0.3);
    flex-shrink: 0;
  }

  .title-header { display: flex; align-items: center; justify-content: center; gap: 10px; margin-bottom: 6px; }
  .title { color: #06b6d4; font-size: 22px; font-weight: 900; text-transform: uppercase; letter-spacing: 4px; }
  .subtitle { text-align: center; color: rgba(103,232,249,0.7); font-size: 12px; font-family: 'Courier New', monospace; }

  .content {
    padding: 18px;
  }

  .section {
    background: rgba(2, 6, 23, 0.5);
    border: 2px solid rgba(16,185,129,0.3);
    border-radius: 20px;
    padding: 18px;
  }

  .section-title {
    color: #fbbf24;
    font-size: 14px;
    font-weight: 900;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 12px;
  }

  .helper {
    color: rgba(226,232,240,0.9);
    font-size: 12px;
    line-height: 1.55;
    margin-bottom: 14px;
  }

  #character-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
    gap: 14px;
  }

  .character-card {
    background: rgba(15, 23, 42, 0.65);
    border: 1px solid rgba(6, 182, 212, 0.25);
    border-radius: 16px;
    padding: 14px;
    cursor: pointer;
    transition: all 0.2s ease;
    position: relative;
    overflow: hidden;
  }

  .character-card:hover {
    transform: translateY(-3px);
    border-color: rgba(251, 191, 36, 0.55);
    box-shadow: 0 0 22px rgba(251, 191, 36, 0.22);
  }

  .character-card.selected {
    border-color: rgba(6,182,212,0.9);
    box-shadow: 0 0 30px rgba(6,182,212,0.35);
    background: rgba(6, 182, 212, 0.10);
  }

  .character-img {
    width: 100%;
    height: 180px;
    object-fit: contain;
    background: rgba(2,6,23,0.35);
    border: 1px solid rgba(6,182,212,0.18);
    border-radius: 12px;
    padding: 8px;
    margin-bottom: 10px;
  }

  .character-name {
    color: #06b6d4;
    font-size: 14px;
    font-weight: 900;
    letter-spacing: 0.5px;
    margin-bottom: 6px;
  }

  .character-trait {
    color: #fbbf24;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 6px;
  }

  .character-desc {
    color: rgba(226,232,240,0.85);
    font-size: 12px;
    line-height: 1.45;
  }

  .input-wrap {
    margin-top: 16px;
    background: rgba(15, 23, 42, 0.6);
    border: 1px solid rgba(6, 182, 212, 0.25);
    border-radius: 14px;
    padding: 14px;
  }

  .label {
    display: block;
    color: rgba(103,232,249,0.8);
    font-weight: 900;
    letter-spacing: 2px;
    font-size: 11px;
    text-transform: uppercase;
    margin-bottom: 8px;
  }

  #character-name-input {
    width: 100%;
    padding: 12px 12px;
    border-radius: 10px;
    border: 1px solid rgba(6,182,212,0.35);
    background: rgba(2, 6, 23, 0.7);
    color: white;
    outline: none;
    font-size: 14px;
  }
  #character-name-input:focus {
    border-color: rgba(6,182,212,0.9);
    box-shadow: 0 0 0 3px rgba(6,182,212,0.15);
  }

  #error-message {
    color: #ef4444;
    margin-top: 10px;
    display: none;
    font-size: 12px;
    font-weight: 800;
  }

  .btn-row {
    display: flex;
    justify-content: center;
    margin-top: 14px;
  }

  #submit-btn {
    padding: 14px 22px;
    background: linear-gradient(135deg, #06b6d4, #3b82f6);
    color: white;
    border: none;
    border-radius: 12px;
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-size: 13px;
    cursor: pointer;
    box-shadow: 0 10px 20px rgba(6, 182, 212, 0.25);
    transition: 0.2s ease;
  }
  #submit-btn:hover { transform: translateY(-2px); box-shadow: 0 14px 26px rgba(6, 182, 212, 0.35); }
  #submit-btn:disabled { opacity: 0.6; cursor: not-allowed; transform: none; box-shadow: none; }
</style>

<div class="stars" id="stars"></div>

<div class="learninggame-root">
  <div class="container">
    <div class="title-section">
      <div class="title-header">
        <div style="font-size: 20px;">🚀</div>
        <div class="title">Character Selection</div>
      </div>
      <div class="subtitle">Cadet Identity Protocol // Choose Your Suit</div>
    </div>

    <div class="content">
      <div class="section">
        <div class="section-title">Select Your Suit</div>
        <div class="helper">
          Choose a class, then enter your cadet name. Your selection will carry into the maze.
        </div>

        <div id="character-grid"></div>

        <div class="input-wrap">
          <label class="label">Cadet Name</label>
          <input type="text" id="character-name-input" placeholder="Type your cadet name..." />
          <p id="error-message"></p>

          <div class="btn-row">
            <button id="submit-btn">Ready to Enter Maze →</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<script>
  // Stars background (match homescreen)
  const starsContainer = document.getElementById('stars');
  for (let i = 0; i < 140; i++) {
    const star = document.createElement('div');
    star.className = 'star';
    star.style.left = Math.random() * 100 + '%';
    star.style.top = Math.random() * 100 + '%';
    star.style.animationDelay = Math.random() * 3 + 's';
    star.style.opacity = Math.random() * 0.7 + 0.25;
    starsContainer.appendChild(star);
  }

  const characters = [
    {
      name: "Axiom Space Suit",
      image: "{{ '/images/learninggame/axiom.png' | relative_url }}",
      trait: "Advanced Commercial Design",
      description: "Modern next-gen suit technology"
    },
    {
      name: "Gemini G4c Space Suit",
      image: "{{ '/images/learninggame/gemini.png' | relative_url }}",
      trait: "Classic NASA Engineering",
      description: "Proven reliability and durability"
    },
    {
      name: "Orlan Space Suit",
      image: "{{ '/images/learninggame/orlan.png' | relative_url }}",
      trait: "Modular Russian Design",
      description: "Flexible and adaptable systems"
    },
    {
      name: "Feitian Space Suit",
      image: "{{ '/images/learninggame/feitian.png' | relative_url }}",
      trait: "Advanced Chinese Technology",
      description: "Cutting-edge innovation"
    }
  ];

  let selectedCharacter = null;

  function renderCharacters() {
    const grid = document.getElementById('character-grid');
    grid.innerHTML = '';

    characters.forEach((character) => {
      const card = document.createElement('div');
      card.className = 'character-card';

      card.innerHTML = `
        <img class="character-img" src="${character.image}" alt="${character.name}">
        <div class="character-name">${character.name}</div>
        <div class="character-trait">${character.trait}</div>
        <div class="character-desc">${character.description}</div>
      `;

      card.addEventListener('click', function() {
        selectCharacter(character.name);
      });

      grid.appendChild(card);
    });

    syncSelectedUI();
  }

  function selectCharacter(name) {
    selectedCharacter = name;
    syncSelectedUI();
  }

  function syncSelectedUI() {
    const cards = document.querySelectorAll('.character-card');
    cards.forEach((card, idx) => {
      const isSelected = characters[idx].name === selectedCharacter;
      card.classList.toggle('selected', isSelected);
    });
  }

  document.getElementById('submit-btn').addEventListener('click', function() {
    const characterName = document.getElementById('character-name-input').value.trim();
    const errorMessage = document.getElementById('error-message');

    if (!characterName) {
      errorMessage.textContent = "⚠️ Please enter your cadet name.";
      errorMessage.style.display = 'block';
      return;
    }

    if (!selectedCharacter) {
      errorMessage.textContent = "⚠️ Please select a suit class.";
      errorMessage.style.display = 'block';
      return;
    }

    errorMessage.style.display = 'none';

    this.disabled = true;
    this.textContent = "Saving...";

    // Generate or retrieve player ID
    let playerId = localStorage.getItem('playerId');
    if (!playerId) {
      playerId = 'player_' + Date.now() + '_' + Math.random().toString(36).slice(2, 11);
      localStorage.setItem('playerId', playerId);
    }

    fetch('http://127.0.0.1:8320/api/update_character', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include',
      body: JSON.stringify({
        name: characterName,
        class: selectedCharacter
      })
    })
    .then(res => res.json())
    .then(data => {
      if (!data.success) throw new Error(data.error || 'Failed to save character');

      this.textContent = "✓ Profile Created!";
      this.style.background = 'linear-gradient(135deg, #10b981, #059669)';

      setTimeout(() => {
        window.location.href = "{{ '/learninggame/home' | relative_url }}";
      }, 900);
    })
    .catch(err => {
      errorMessage.textContent = "❌ Failed to save: " + err.message;
      errorMessage.style.display = 'block';
      this.disabled = false;
      this.textContent = "Ready to Enter Maze →";
    });
  });

  window.addEventListener('DOMContentLoaded', renderCharacters);
</script>
