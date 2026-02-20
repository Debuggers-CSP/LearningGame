export const baseurl = "";

const IS_LOCALHOST = ["localhost", "127.0.0.1"].includes(window.location.hostname);

const ROBOP_LOCAL = "http://localhost:8320";
const ROBOP_PROD  = "https://robop.opencodingsociety.com";

export const pythonURI = IS_LOCALHOST
  ? ROBOP_LOCAL
  : ROBOP_PROD;

export const javaURI = IS_LOCALHOST
  ? "http://localhost:8585"
  : "https://spring.opencodingsociety.com";

export const fetchOptions = {
  method: "GET",
  mode: "cors",
  cache: "default",
  credentials: "include",
  headers: {
    "Content-Type": "application/json",
  },
};

export function withAuth(options = {}) {
  const token = localStorage.getItem("robop_jwt");

  const headers = {
    ...fetchOptions.headers,
    ...(options.headers || {}),
  };

  if (token) headers["Authorization"] = `Bearer ${token}`;

  return {
    ...fetchOptions,
    ...options,
    headers,
  };
}
