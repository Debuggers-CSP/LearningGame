---
layout: default
title: Learning Game — Core Feedback & Action Plan
description: Student feedback organized by question, with concrete improvement plans by feature and dev area.
permalink: /learninggame/feedback
---

<style>
  :root{
    --bg1:#0b1020;
    --bg2:#0a1636;
    --card:#0f1b3a;
    --card2:#0f244a;
    --text:#e9eefc;
    --muted:#b8c4e6;
    --accent:#7aa2ff;
    --accent2:#47e6c3;
    --warn:#ffcc66;
    --border: rgba(255,255,255,.10);
    --shadow: 0 16px 40px rgba(0,0,0,.35);
    --radius: 18px;
    --mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
    --sans: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji";
  }

  .lg-wrap{
    font-family: var(--sans);
    color: var(--text);
    background: radial-gradient(1000px 650px at 15% 15%, rgba(122,162,255,.20), transparent 55%),
                radial-gradient(900px 600px at 80% 30%, rgba(71,230,195,.14), transparent 55%),
                linear-gradient(180deg, var(--bg1), var(--bg2));
    border: 1px solid var(--border);
    border-radius: 24px;
    padding: 28px;
    box-shadow: var(--shadow);
  }

  .lg-hero{
    display:flex; gap:18px; align-items:flex-start; justify-content:space-between;
    flex-wrap: wrap;
    padding: 18px 18px 14px;
    border-radius: var(--radius);
    background: linear-gradient(135deg, rgba(122,162,255,.14), rgba(71,230,195,.10));
    border: 1px solid var(--border);
  }

  .lg-title{
    margin:0;
    font-size: 1.9rem;
    letter-spacing: .2px;
  }
  .lg-sub{
    margin: 6px 0 0;
    color: var(--muted);
    line-height: 1.45;
    max-width: 70ch;
  }

  .lg-chiprow{ display:flex; gap:10px; flex-wrap:wrap; align-items:center; }
  .lg-chip{
    font-family: var(--mono);
    font-size: .85rem;
    padding: 6px 10px;
    border-radius: 999px;
    border: 1px solid var(--border);
    background: rgba(15,27,58,.55);
    color: var(--text);
    white-space: nowrap;
  }
  .lg-chip b{ color: var(--accent2); font-weight: 700; }

  .lg-grid{
    margin-top: 18px;
    display:grid;
    grid-template-columns: repeat(12, 1fr);
    gap: 16px;
  }
  .lg-card{
    grid-column: span 12;
    background: linear-gradient(180deg, rgba(15,27,58,.95), rgba(15,36,74,.92));
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 16px;
    box-shadow: 0 10px 22px rgba(0,0,0,.22);
  }
  @media (min-width: 980px){
    .lg-card.half{ grid-column: span 6; }
  }

  .lg-h2{
    margin: 0 0 10px;
    font-size: 1.25rem;
    letter-spacing: .2px;
  }
  .lg-h2 .tag{
    font-family: var(--mono);
    font-size: .85rem;
    color: var(--muted);
    margin-left: 8px;
  }

  details{
    border: 1px solid var(--border);
    border-radius: 14px;
    background: rgba(15,27,58,.55);
    padding: 12px 12px 10px;
    margin: 10px 0;
  }
  summary{
    cursor:pointer;
    list-style:none;
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap: 10px;
    font-weight: 650;
  }
  summary::-webkit-details-marker{ display:none; }
  .lg-kicker{
    color: var(--muted);
    font-size: .9rem;
    margin: 6px 0 0;
    line-height: 1.5;
  }

  .lg-list{
    margin: 10px 0 0;
    padding: 0;
    list-style: none;
    display:flex;
    flex-direction: column;
    gap: 10px;
  }
  .lg-item{
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 12px;
    background: linear-gradient(180deg, rgba(15,36,74,.60), rgba(15,27,58,.45));
  }
  .lg-quote{
    margin: 0;
    font-size: 1rem;
    line-height: 1.4;
  }
  .lg-quote::before{
    content:"“";
    color: rgba(122,162,255,.75);
    font-weight: 800;
    margin-right: 2px;
  }
  .lg-quote::after{
    content:"”";
    color: rgba(122,162,255,.75);
    font-weight: 800;
    margin-left: 2px;
  }
  .lg-impact{
    margin: 8px 0 0;
    color: var(--muted);
    line-height: 1.5;
    font-size: .95rem;
  }
  .lg-impact b{
    color: var(--accent);
    font-weight: 700;
  }

  .lg-pill{
    display:inline-block;
    margin-top: 10px;
    font-family: var(--mono);
    font-size: .83rem;
    padding: 5px 10px;
    border-radius: 999px;
    border: 1px solid var(--border);
    background: rgba(11,16,32,.55);
    color: var(--text);
  }
  .lg-pill.good{ color: var(--accent2); }
  .lg-pill.grow{ color: var(--warn); }

  .lg-plan{
    display:grid;
    grid-template-columns: 1fr;
    gap: 12px;
    margin-top: 8px;
  }
  @media (min-width: 980px){
    .lg-plan{ grid-template-columns: repeat(2, 1fr); }
  }
  .lg-planbox{
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 14px;
    background: rgba(15,27,58,.55);
  }
  .lg-planbox h3{
    margin: 0 0 6px;
    font-size: 1.05rem;
  }
  .lg-planbox .meta{
    font-family: var(--mono);
    font-size: .85rem;
    color: var(--muted);
    margin: 0 0 10px;
  }
  .lg-planbox ul{
    margin: 0;
    padding-left: 18px;
    color: var(--text);
  }
  .lg-planbox li{ margin: 6px 0; color: var(--muted); line-height: 1.45; }
  .lg-planbox li b{ color: var(--text); }

  .lg-footer{
    margin-top: 16px;
    padding-top: 10px;
    border-top: 1px dashed rgba(255,255,255,.18);
    color: var(--muted);
    font-size: .92rem;
    line-height: 1.55;
  }
</style>

<div class="lg-wrap">

  <div class="lg-hero">
    <div>
      <h1 class="lg-title">Learning Game — Core Feedback & Action Plan</h1>
      <p class="lg-sub">
        Feedback is grouped by the three reflection questions:
        <b>Favorite Section</b>, <b>Glow</b>, and <b>Grow</b>.
        Each entry includes a quick note on how we can use it to improve the project,
        plus a separate roadmap with actionable steps by <b>feature</b> and <b>development area</b>.
      </p>
    </div>
    <div class="lg-chiprow">
      <div class="lg-chip"><b>24</b> favorite-section responses</div>
      <div class="lg-chip"><b>24</b> glow responses</div>
      <div class="lg-chip"><b>24</b> grow responses</div>
    </div>
  </div>

  <div class="lg-grid">
    <!-- FAVORITE SECTION -->
    <!-- ========================= -->
<!-- SUMMARY BY QUESTION -->
<!-- ========================= -->

<section class="lg-card">
  <h2 class="lg-h2">Summary of Main Themes</h2>

  <!-- FAVORITE SECTION SUMMARY -->
  <div class="lg-planbox">
    <h3>What was your favorite section?</h3>
    <ul>
      <li><b>AI Features (Generate Answer, Chatbot, AI Correction)</b> were the most frequently mentioned and seen as the most impressive part of the project.</li>
      <li><b>The Maze</b> was praised for being interactive, fun, and a unique navigation method.</li>
      <li><b>Robot Code / Coding Practice</b> stood out as engaging and educational.</li>
      <li><b>Pseudocode & Theory Sections</b> helped reinforce exam-style understanding.</li>
      <li><b>Badges & Gamification</b> made the experience motivating and rewarding.</li>
      <li><b>Overall Game Design</b> felt immersive and reminded students of AP CSP preparation.</li>
    </ul>
  </div>

  <!-- GLOW SUMMARY -->
  <div class="lg-planbox">
    <h3>List one GLOW</h3>
    <ul>
      <li><b>Clean, professional UI</b> was consistently praised.</li>
      <li><b>Easy navigation</b> made the experience smooth and intuitive.</li>
      <li><b>Interactive and game-like format</b> made studying feel engaging rather than passive.</li>
      <li><b>AI integration through APIs</b> felt modern and impressive.</li>
      <li><b>Different difficulty levels</b> supported learners at various stages.</li>
      <li><b>Presentation & structure of sections</b> helped students understand concepts clearly.</li>
    </ul>
  </div>

  <!-- GROW SUMMARY -->
  <div class="lg-planbox">
    <h3>List one GROW</h3>
    <ul>
      <li><b>More tutorials and explained solutions</b> were requested after incorrect answers.</li>
      <li><b>Clearer organization and smoother progression</b> would improve the overall learning flow.</li>
      <li><b>Simpler explanations</b> for beginners would make the system more accessible.</li>
      <li><b>More transparency about the AI feature</b> (how it works, how to use it better).</li>
      <li><b>Improved reliability during demos</b>, especially when network/model access fails.</li>
      <li><b>“Take it to the next level”</b> — students want deeper features and more advanced functionality.</li>
    </ul>
  </div>
</section>
    <section class="lg-card half">
      <h2 class="lg-h2">What was your favorite section? <span class="tag">raw student quotes</span></h2>
      <details open>
        <summary>
          AI / Generate Answer / AI Bot <span class="lg-pill good">most-mentioned theme</span>
        </summary>
        <p class="lg-kicker">Students repeatedly called out the AI features as the most memorable and useful part.</p>
        <ul class="lg-list">
          <li class="lg-item">
            <p class="lg-quote">The generate answer section</p>
            <p class="lg-impact"><b>How we use this:</b> Keep AI support as a core loop, but add clearer “why this is correct” reasoning so it teaches, not just answers.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">I really like AI chat bot</p>
            <p class="lg-impact"><b>How we use this:</b> Expand the chatbot into guided tutoring: hints → explanation → example → practice question.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">Ai correction</p>
            <p class="lg-impact"><b>How we use this:</b> Add an “error diagnosis” mode that explains the mistake pattern (logic, bounds, off-by-one, etc.).</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">The Ai bot was my favorite section</p>
            <p class="lg-impact"><b>How we use this:</b> Add quick prompts (buttons) for common asks: “give a hint”, “show pseudocode”, “explain in plain English”.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">Generate Answer Section</p>
            <p class="lg-impact"><b>How we use this:</b> Add “confidence + source-of-truth” UI: show which rubric concept it maps to (selection, iteration, list).</p>
          </li>
        </ul>
      </details>
      <details>
        <summary>
          Maze / Navigation / Interactivity <span class="lg-pill good">high engagement</span>
        </summary>
        <p class="lg-kicker">The maze was praised as a fun way to move through learning content.</p>
        <ul class="lg-list">
          <li class="lg-item">
            <p class="lg-quote">The maze</p>
            <p class="lg-impact"><b>How we use this:</b> Turn navigation into a “progress map” with locked/unlocked nodes and visible mastery.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">The maze was a cool way to navigate between the questions</p>
            <p class="lg-impact"><b>How we use this:</b> Add breadcrumbs and “Return to last question” to prevent users from feeling lost.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">I liked the maze because it made it interactive</p>
            <p class="lg-impact"><b>How we use this:</b> Add micro-rewards in the maze (mini badges, streak bonuses, mystery hint tiles).</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">the questions in the maze</p>
            <p class="lg-impact"><b>How we use this:</b> Label question tiles with topic tags (lists, procedures, Boolean logic) so students can target weak areas.</p>
          </li>
        </ul>
      </details>
      <details>
        <summary>
          Robot Code / Simulation / “Theory” <span class="lg-pill good">core feature strength</span>
        </summary>
        <p class="lg-kicker">Students liked the coding/practice components, especially robot-related content.</p>
        <ul class="lg-list">
          <li class="lg-item">
            <p class="lg-quote">Robot code</p>
            <p class="lg-impact"><b>How we use this:</b> Add more structured levels (beginner → intermediate → challenge) with clear goals per level.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">robot code stimulation</p>
            <p class="lg-impact"><b>How we use this:</b> Improve clarity: rename to “robot code simulation” and add a short “what you’re learning” panel.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">The theory</p>
            <p class="lg-impact"><b>How we use this:</b> Convert theory pages into interactive checkpoints (1–2 quick questions per concept).</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">Practicing coding</p>
            <p class="lg-impact"><b>How we use this:</b> Add “practice sets” with timed mode and review mode + automatic “next best question”.</p>
          </li>
        </ul>
      </details>
      <details>
        <summary>
          Badges / Cadet Academy / Theme (misc favorites) <span class="lg-pill good">motivation + identity</span>
        </summary>
        <p class="lg-kicker">Gamification and themed sections helped motivation and memorability.</p>
        <ul class="lg-list">
          <li class="lg-item">
            <p class="lg-quote">I love the design of the badges</p>
            <p class="lg-impact"><b>How we use this:</b> Add badge “criteria” tooltips and a badge gallery to encourage completion.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">The badge functionality made it fun, also liked that you can get prompted the answers if you don’t know them</p>
            <p class="lg-impact"><b>How we use this:</b> Tie badges to learning behaviors (attempts, retries, reviewing explanations), not just completion.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">Cadet academy</p>
            <p class="lg-impact"><b>How we use this:</b> Make Cadet Academy the “onboarding hub” with a 2-minute tutorial + first badge path.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">Sudo code</p>
            <p class="lg-impact"><b>How we use this:</b> Standardize naming to “Pseudocode” everywhere; add side-by-side examples (English ↔ pseudocode ↔ code).</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">The one where china had space.</p>
            <p class="lg-impact"><b>How we use this:</b> If this refers to a story/module, we’ll clarify titles and add a “Modules” index so students can find it again.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">It remind me about my CSP ap exam studying experience</p>
            <p class="lg-impact"><b>How we use this:</b> Lean into “exam-mode”: quick drills, rubric tagging, and summary sheets per unit.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">Everything</p>
            <p class="lg-impact"><b>How we use this:</b> Protect the overall breadth while improving the “learning path” so it feels cohesive, not scattered.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">Explanation</p>
            <p class="lg-impact"><b>How we use this:</b> This signals explanations matter—expand the feedback loop after answers (what/why/how).</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">Game</p>
            <p class="lg-impact"><b>How we use this:</b> Keep the game identity strong; add a clear “start here” path for first-time users.</p>
          </li>
        </ul>
      </details>
    </section>
    <!-- GLOW -->
    <section class="lg-card half">
      <h2 class="lg-h2">List one GLOW <span class="tag">what students liked</span></h2>
      <details open>
        <summary>
          UI / Theme / Navigation <span class="lg-pill good">consensus strength</span>
        </summary>
        <p class="lg-kicker">The biggest “glow” cluster: clean, professional UI + easy navigation.</p>
        <ul class="lg-list">
          <li class="lg-item">
            <p class="lg-quote">How easy it was to navigate</p>
            <p class="lg-impact"><b>How we use this:</b> Preserve the nav structure; any new features must fit the same simple mental model.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">Very clean UI</p>
            <p class="lg-impact"><b>How we use this:</b> Keep spacing/typography consistent; add a small design system (buttons, cards, alerts).</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">Very professional and is useful for quick review</p>
            <p class="lg-impact"><b>How we use this:</b> Add “Quick Review” mode: 10 questions, instant grading, recap at the end.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">UI</p>
            <p class="lg-impact"><b>How we use this:</b> Add optional accessibility toggles (larger text, reduced motion, high contrast).</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">I like the UI and Theme</p>
            <p class="lg-impact"><b>How we use this:</b> Expand theme consistency: same icon set, same section headers, same badge style.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">I like the page layout and design and the gaming aspect</p>
            <p class="lg-impact"><b>How we use this:</b> Strengthen gamification: streaks, progress bars, “next mission” prompts.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">It was very smooth</p>
            <p class="lg-impact"><b>How we use this:</b> Track performance budgets (load time, API latency) and fix slow paths first.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">Nice idea, interactive way of learning for exam looks fun.</p>
            <p class="lg-impact"><b>How we use this:</b> Add “AP CSP exam tags” and a recommended weekly practice schedule.</p>
          </li>
        </ul>
      </details>
      <details>
        <summary>
          AI Features / APIs <span class="lg-pill good">feature differentiator</span>
        </summary>
        <p class="lg-kicker">Many students highlighted AI as the coolest/most modern part.</p>
        <ul class="lg-list">
          <li class="lg-item">
            <p class="lg-quote">The chat bot</p>
            <p class="lg-impact"><b>How we use this:</b> Add topic-aware prompts: the bot should know which module the user is in.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">Use of latest ai models through api</p>
            <p class="lg-impact"><b>How we use this:</b> Add reliability features: retries, graceful fallbacks, and transparent “AI unavailable” states.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">the ai autofill and helping is really cool</p>
            <p class="lg-impact"><b>How we use this:</b> Add “show steps” to autofill; require one user attempt before revealing full answer.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">Ai was cool</p>
            <p class="lg-impact"><b>How we use this:</b> Add a short “AI 101” help panel: what it does, how to ask, and what to double-check.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">I loved all of the ai features in this game</p>
            <p class="lg-impact"><b>How we use this:</b> Bundle AI tools into one “Study Assistant” page with consistent buttons and outputs.</p>
          </li>
        </ul>
      </details>
      <details>
        <summary>
          Difficulty Levels / Teaching Value / Presentation <span class="lg-pill good">learning impact</span>
        </summary>
        <p class="lg-kicker">Students liked the range of difficulties and found sections helpful for learning.</p>
        <ul class="lg-list">
          <li class="lg-item">
            <p class="lg-quote">different difficulties for different users, and the UI</p>
            <p class="lg-impact"><b>How we use this:</b> Add a placement quiz that auto-recommends a starting difficulty.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">Sections were really helpful in teaching us</p>
            <p class="lg-impact"><b>How we use this:</b> Add “learning objectives” at the top of each section, then a short mastery check at the end.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">The students were great presenters</p>
            <p class="lg-impact"><b>How we use this:</b> Turn the demo script into an in-app guided tour so new users get the same clarity.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">It was great !</p>
            <p class="lg-impact"><b>How we use this:</b> Keep polishing the “wow” factor while removing confusion points called out in the Grow section.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">Shay was incredible, absolutely stunning and flawless in every way and the character selection was good.</p>
            <p class="lg-impact"><b>How we use this:</b> This suggests character selection is memorable—add more character personality + clear benefit (each character = different learning path/theme).</p>
          </li>
        </ul>
      </details>
    </section>
    <!-- GROW -->
    <section class="lg-card">
      <h2 class="lg-h2">List one GROW <span class="tag">what to improve</span></h2>
      <details open>
        <summary>
          Clarity / Explanations / Tutorials <span class="lg-pill grow">priority improvements</span>
        </summary>
        <p class="lg-kicker">Top theme: users want more explanation, better tutorials, and clearer flow.</p>
        <ul class="lg-list">
          <li class="lg-item">
            <p class="lg-quote">Tutorials/explained solutions if you get something wrong</p>
            <p class="lg-impact"><b>How we use this:</b> Add post-answer feedback: correct/incorrect → explanation → common mistake → one similar practice question.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">provide more explanations</p>
            <p class="lg-impact"><b>How we use this:</b> Build “Explain” as a first-class UI button next to every question and AI response.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">Make it a bit easier to inderstand</p>
            <p class="lg-impact"><b>How we use this:</b> Simplify language, add examples, and include a “what this means” tooltip for key terms.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">Make it Easier</p>
            <p class="lg-impact"><b>How we use this:</b> Add a “Beginner path” with smaller steps, more hints, and slower progression.</p>
          </li>
        </ul>
      </details>
      <details>
        <summary>
          Organization / Flow / Story Progression <span class="lg-pill grow">cohesion</span>
        </summary>
        <p class="lg-kicker">Students want the experience to feel more connected and logically sequenced.</p>
        <ul class="lg-list">
          <li class="lg-item">
            <p class="lg-quote">Maybe more fluid flow of events- story progression</p>
            <p class="lg-impact"><b>How we use this:</b> Create a “main questline” path that guides users through features in a recommended order.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">Organization could be better</p>
            <p class="lg-impact"><b>How we use this:</b> Add a central dashboard: modules, progress, recommended next step, and recent activity.</p>
          </li>
        </ul>
      </details>
      <details>
        <summary>
          Reliability / Network / Demo Stability <span class="lg-pill grow">must-fix</span>
        </summary>
        <p class="lg-kicker">The project needs to degrade gracefully when network/model access fails.</p>
        <ul class="lg-list">
          <li class="lg-item">
            <p class="lg-quote">Demo didn’t work with model because we didn’t had network</p>
            <p class="lg-impact"><b>How we use this:</b> Add offline-safe fallbacks (cached examples, local hints) + a clear “AI unavailable” message instead of breaking the demo.</p>
          </li>
        </ul>
      </details>
      <details>
        <summary>
          “Take it to the next level” + “Learn more about AI” <span class="lg-pill grow">stretch goals</span>
        </summary>
        <p class="lg-kicker">Users want deeper AI transparency and feature depth.</p>
        <ul class="lg-list">
          <li class="lg-item">
            <p class="lg-quote">I would love to learn more about the AI feature</p>
            <p class="lg-impact"><b>How we use this:</b> Add an “AI feature tour” page: what it can do, examples, limitations, and best prompts.</p>
          </li>
          <li class="lg-item">
            <p class="lg-quote">Take to the next level</p>
            <p class="lg-impact"><b>How we use this:</b> Translate this into measurable upgrades: more content coverage, better progression, analytics, and reliability.</p>
          </li>
        </ul>
      </details>
    </section>
    <!-- ACTION PLAN -->
    <section class="lg-card">
      <h2 class="lg-h2">Actionable Steps <span class="tag">plans by feature × development area</span></h2>
      <div class="lg-plan">
        <!-- ROBOT CODE -->
        <div class="lg-planbox">
          <h3>Feature: Robot Code / Simulation</h3>
          <p class="meta">UI • Frontend • Backend • APIs</p>
          <ul>
            <li><b>UI:</b> Add a “Goal Panel” (what to do + success criteria) and a “Hint Ladder” (hint → stronger hint → solution).</li>
            <li><b>Frontend:</b> Build level selection (Beginner/Intermediate/Challenge) and persist last level played in local storage.</li>
            <li><b>Backend:</b> Store level attempts and outcomes for progress tracking (attempt count, completion, time-to-solve).</li>
            <li><b>APIs:</b> Create endpoints for <span style="font-family:var(--mono)">/levels</span>, <span style="font-family:var(--mono)">/attempt</span>, and <span style="font-family:var(--mono)">/progress</span> so the UI can load content dynamically.</li>
          </ul>
        </div>
        <!-- PSEUDOCODE -->
        <div class="lg-planbox">
          <h3>Feature: Pseudocode</h3>
          <p class="meta">UI • Frontend • Content • Feedback Loop</p>
          <ul>
            <li><b>UI:</b> Add side-by-side panels: “Plain English” ↔ “Pseudocode” ↔ “Code” with consistent formatting.</li>
            <li><b>Frontend:</b> Add a “Why this is correct” collapsible section after submission (especially for incorrect answers).</li>
            <li><b>Content:</b> Tag each question by concept (selection/iteration/list/procedure/boolean) to match AP CSP framing.</li>
            <li><b>Feedback loop:</b> After wrong answers, show: correct solution + common mistake + 1 similar practice question.</li>
          </ul>
        </div>
        <!-- AI / GENERATE ANSWER / CHATBOT -->
        <div class="lg-planbox">
          <h3>Feature: AI (Generate Answer + Chatbot)</h3>
          <p class="meta">UI • Frontend • Backend • APIs • Reliability</p>
          <ul>
            <li><b>UI:</b> Standardize buttons: “Hint”, “Explain”, “Show Steps”, “Try Another”, “Rubric Tag”.</li>
            <li><b>Frontend:</b> Add context injection so the bot knows the current module + question + difficulty.</li>
            <li><b>Backend:</b> Add rate limiting, logging, and response normalization (always return <span style="font-family:var(--mono)">success/text/error</span>).</li>
            <li><b>APIs:</b> Add graceful fallbacks: if AI fails, return cached help text + suggest next steps (retry, check network).</li>
            <li><b>Reliability:</b> Add an “AI unavailable” UI state so demos don’t break when there’s no network.</li>
          </ul>
        </div>
        <!-- MAZE / NAVIGATION -->
        <div class="lg-planbox">
          <h3>Feature: Maze / Navigation</h3>
          <p class="meta">UI • Frontend • Database • Progression</p>
          <ul>
            <li><b>UI:</b> Add breadcrumbs + “Return to last question” + a visible progress map (completed/locked/next).</li>
            <li><b>Frontend:</b> Add filters for tiles by topic tag and difficulty (so organization feels clearer).</li>
            <li><b>Database:</b> Track per-tile completion and mastery score to drive personalized recommendations.</li>
            <li><b>Progression:</b> Create a “main questline” path (recommended order) to satisfy story/flow feedback.</li>
          </ul>
        </div>
        <!-- BADGES / GAMIFICATION -->
        <div class="lg-planbox">
          <h3>Feature: Badges / Gamification</h3>
          <p class="meta">UI • Frontend • Backend • Database</p>
          <ul>
            <li><b>UI:</b> Add badge tooltips (criteria + how to earn) and a badge gallery page.</li>
            <li><b>Frontend:</b> Add progress bars toward each badge (e.g., “3/5 practice sets completed”).</li>
            <li><b>Backend:</b> Ensure badge awarding is idempotent and consistent (no duplicates, no missed awards).</li>
            <li><b>Database:</b> Store badge timestamps + earned-by reason (completion vs streak vs retries) for analytics.</li>
          </ul>
        </div>
        <!-- ONBOARDING / HELP -->
        <div class="lg-planbox">
          <h3>Feature: Onboarding (Cadet Academy / Help)</h3>
          <p class="meta">UI • Frontend • Content</p>
          <ul>
            <li><b>UI:</b> Add a 2-minute guided tour (stepper) that introduces Maze → Questions → AI Help → Badges.</li>
            <li><b>Frontend:</b> Add a “Start Here” dashboard with a recommended first mission + quick review option.</li>
            <li><b>Content:</b> Add short “What you’ll learn” objectives at the top of each module.</li>
          </ul>
        </div>
      </div>
      <div class="lg-footer">
        <b>How we’ll measure success:</b> improved clarity (fewer “confused” comments), smoother flow (higher completion rate per session),
        and stronger reliability (AI/network issues handled without breaking demos). We’ll prioritize tutorials/explanations + organization first,
        then deepen AI transparency and progression systems.
      </div>
    </section>
  </div>
</div>