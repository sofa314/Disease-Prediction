// firebase-config.js
// Use CDN URLs for Firebase imports
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.23.0/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/9.23.0/firebase-auth.js";

const firebaseConfig = {
  apiKey: "AIzaSyB-rG_xvwkpg25WiXoAdusO-829XkEcqDo",
  authDomain: "login-pa-c229f.firebaseapp.com",
  projectId: "login-pa-c229f",
  storageBucket: "login-pa-c229f.appspot.com", // Corrected from .app to .appspot.com
  messagingSenderId: "536993605448",
  appId: "1:536993605448:web:91ceab44586a01d997757d",
  measurementId: "G-0E70VLF4KF"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

export { auth };
