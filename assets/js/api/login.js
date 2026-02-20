import { baseurl, pythonURI, fetchOptions, withAuth } from './config.js';

console.log("login.js loaded");

document.addEventListener('DOMContentLoaded', async function () {
  console.log("Base URL:", baseurl);

  // ✅ pythonURI is now a string
  const apiBase = pythonURI;

  getCredentials(apiBase)
    .then(data => {
      console.log("Credentials data:", data);
      window.user = data;

      const loginArea = document.getElementById('loginArea');
      if (!loginArea) return;

      if (data) {
        loginArea.innerHTML = `
          <div class="dropdown">
            <button class="dropbtn page-link" style="border:none; background:none; cursor:pointer; color:inherit; font-size:inherit; font-family:inherit; padding:0;">${data.name}</button>
            <div class="dropdown-content hidden">
              ${
                data.roles && Array.isArray(data.roles) && data.roles.length > 0
                  ? `<div class="roles-list" style="padding: 8px 16px; color: #888; font-size: 0.95em;">
                      Roles: ${data.roles.map(role => role.name).join(", ")}
                     </div>
                     <hr style="margin: 4px 0;">`
                  : ''
              }
              <a href="${baseurl}/profile">Profile</a>
              <a href="${baseurl}/logout">Logout</a>
            </div>
          </div>
        `;

        const dropdownButton = loginArea.querySelector('.dropbtn');
        const dropdownContent = loginArea.querySelector('.dropdown-content');

        dropdownButton.addEventListener('click', (event) => {
          event.preventDefault();
          dropdownContent.classList.toggle('hidden');
        });

        document.addEventListener('click', (event) => {
          if (!dropdownButton.contains(event.target) && !dropdownContent.contains(event.target)) {
            dropdownContent.classList.add('hidden');
          }
        });

        updateNavigation(true);
      } else {
        loginArea.innerHTML = `<a href="${baseurl}/login">Login</a>`;
        updateNavigation(false);
      }

      loginArea.style.opacity = "1";
    })
    .catch(err => {
      console.error("Error fetching credentials: ", err);
      const loginArea = document.getElementById('loginArea');
      if (loginArea) loginArea.innerHTML = `<a href="${baseurl}/login">Login</a>`;
      updateNavigation(false);
    });
});

function getCredentials(apiBase) {
  const isLearningGame = window.location.pathname.startsWith("/learninggame/");
  const URL = isLearningGame ? `${apiBase}/api/robop/me` : `${apiBase}/api/id`;

  return fetch(URL, withAuth({ method: "GET" }))
    .then(async (r) => {
      if (!r.ok) return null;
      const data = await r.json();

      // Normalize shapes:
      // /api/id returns {uid,name,role,...}
      // /api/robop/me returns {success:true, user:{...}}
      if (data?.user) return data.user;     // robop
      return data;                          // user.py
    })
    .catch(() => null);
}


async function updateNavigation(isLoggedIn) {
  const trigger = document.querySelector('.trigger');
  if (!trigger) return;

  const links = trigger.querySelectorAll('.page-link');

  if (!isLoggedIn) {
    links.forEach(link => {
      const href = link.getAttribute('href');
      if (href && (href.includes('/navigation/blogs') || href.includes('/navigation/courses'))) {
        link.setAttribute('href', `${baseurl}/navigation/blogs/`);
        link.textContent = 'Blogs';
      }
    });
    return;
  }

  try {
    const response = await fetch(`${apiBase}/api/user/class`, withAuth({ method: "GET" }));

    if (!response.ok) {
      updateNavLink(links, `${baseurl}/navigation/courses/`, 'Courses');
      return;
    }

    const data = await response.json();
    const classes = data.class || [];

    const courseMap = {
      'CSSE': { name: 'CSSE', url: `${baseurl}/navigation/courses/csse` },
      'CSP':  { name: 'APCSP', url: `${baseurl}/navigation/courses/csp` },
      'CSA':  { name: 'APCSA', url: `${baseurl}/navigation/courses/csa` }
    };

    const userCourses = classes.filter(cls => courseMap[cls]).map(cls => courseMap[cls]);

    if (userCourses.length === 1) {
      updateNavLink(links, userCourses[0].url, userCourses[0].name);
    } else {
      updateNavLink(links, `${baseurl}/navigation/courses/`, 'Courses');
    }

  } catch (error) {
    updateNavLink(links, `${baseurl}/navigation/courses/`, 'Courses');
  }
}

function updateNavLink(links, url, text) {
  links.forEach(link => {
    const href = link.getAttribute('href');
    if (href && (href.includes('/navigation/blog') || href.includes('/navigation/courses'))) {
      link.setAttribute('href', url);
      link.textContent = text;
    }
  });
}
