// 🌹 ROSE SPHERE - Configuration
const firebaseConfig = {
    apiKey: "AIzaSyBB4aIL-7cXL_FbsHT2Jj-T70EmF9Chc0A",
    authDomain: "comk-4302e.firebaseapp.com",
    databaseURL: "https://comk-4302e-default-rtdb.firebaseio.com",
    projectId: "comk-4302e",
    storageBucket: "comk-4302e.firebasestorage.app",
    messagingSenderId: "817565218754",
    appId: "1:817565218754:web:874fad2b98ee5789b5c85b",
    measurementId: "G-DR25TWGM6M"
};
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.database();
const CLOUD_NAME = "dt0tkbtzw";
const UPLOAD_PRESET = "xk20_k";
const ADMIN_EMAILS = ['jasim28v@gmail.com'];
const DICEBEAR_URL = "https://api.dicebear.com/7.x/bottts-neutral/svg";
const COVER_COLORS = [
    "linear-gradient(135deg, #ec4899, #f472b6)",
    "linear-gradient(135deg, #db2777, #ec4899)",
    "linear-gradient(135deg, #be185d, #db2777)",
    "linear-gradient(135deg, #f472b6, #f9a8d4)",
    "linear-gradient(135deg, #ec4899, #a855f7)",
    "linear-gradient(135deg, #fda4af, #f472b6)",
    "linear-gradient(135deg, #e11d48, #ec4899)",
    "linear-gradient(135deg, #f9a8d4, #fbcfe8)",
    "linear-gradient(135deg, #c026d3, #ec4899)",
    "linear-gradient(135deg, #fb7185, #f472b6)"
];
const APP_NAME = "ROSE SPHERE";
const APP_VERSION = "3.0.0";
console.log('🌹 %c'+APP_NAME+' v'+APP_VERSION+' Ready', 'color: #ec4899; font-size: 16px; font-weight: bold;');
