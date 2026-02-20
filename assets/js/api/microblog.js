import { pythonURI, withAuth } from "./config.js";

function base() {
  return pythonURI; 
}

async function requestJson(url, options) {
  const response = await fetch(url, options);

  const text = await response.text().catch(() => "");
  if (!response.ok) {
    throw new Error(`HTTP ${response.status}: ${text || response.statusText}`);
  }

  return text ? JSON.parse(text) : {};
}

export async function fetchPosts(pagePath) {
  const robopURI = await base();
  let apiUrl = `${robopURI}/api/microblog`;
  if (pagePath) apiUrl += `?pagePath=${encodeURIComponent(pagePath)}`;

  return await requestJson(apiUrl, withAuth({ method: "GET" }));
}

export async function createPost(postData) {
  const robopURI = await base();
  const apiUrl = `${robopURI}/api/microblog`;

  return await requestJson(apiUrl, withAuth({
    method: "POST",
    body: JSON.stringify(postData),
  }));
}

export async function updatePost(postData) {
  const robopURI = await base();
  const apiUrl = `${robopURI}/api/microblog`;

  return await requestJson(apiUrl, withAuth({
    method: "PUT",
    body: JSON.stringify(postData),
  }));
}

export async function createReply(replyData) {
  const robopURI = await base();
  const apiUrl = `${robopURI}/api/microblog/reply`;

  return await requestJson(apiUrl, withAuth({
    method: "POST",
    body: JSON.stringify(replyData),
  }));
}

export async function fetchReplies(postId) {
  const robopURI = await base();
  const apiUrl = `${robopURI}/api/microblog/reply?postId=${encodeURIComponent(postId)}`;

  return await requestJson(apiUrl, withAuth({ method: "GET" }));
}

export async function reactToPost(postId, reactionType) {
  const robopURI = await base();
  const apiUrl = `${robopURI}/api/microblog/reaction`;

  return await requestJson(apiUrl, withAuth({
    method: "POST",
    body: JSON.stringify({ postId, reactionType }),
  }));
}
