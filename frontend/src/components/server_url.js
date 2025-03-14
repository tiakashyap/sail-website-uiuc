const PROD_SERVER = "https://sail.cs.illinois.edu";
const TEST_SERVER = "http://10.192.104.68:5000";

// server URL based on the url of the window
const SERVER_URL = window.location.href.includes("sail.cs.illinois.edu") ? PROD_SERVER : TEST_SERVER;

export { PROD_SERVER, TEST_SERVER };
export default SERVER_URL;