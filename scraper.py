#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════╗
║  🌹 ROSE SPHERE - Premium Social Platform  🌹        ║
║     Ultimate Edition - 9 Files - 1700+ Lines         ║
║                                                        ║
║  🔥  Firebase: comk-4302e                             ║
║  ☁️   Cloudinary: dt0tkbtzw / xk20_k                 ║
║  👤  Avatars: DiceBear Bottts Neutral                 ║
║  💖  Design: Rose Pink Gradient Glass                 ║
║  👑  Admin: jasim28v@gmail.com                        ║
║  📸  Chat: Send Images + Copy + Last Seen             ║
║  👤  Edit Profile: Modal UI                           ║
║  📤  Share: Multi-Platform Modal                      ║
║  📹  Upload: Professional UI                          ║
║  📱  Video: Portrait + Landscape Support              ║
╚══════════════════════════════════════════════════════════╝
"""

import os
import sys

# ═══════════════════════════════════════════════════════════
# 🌹 CONFIGURATION - الإعدادات
# ═══════════════════════════════════════════════════════════

FIREBASE_CONFIG = {
    "apiKey": "AIzaSyBB4aIL-7cXL_FbsHT2Jj-T70EmF9Chc0A",
    "authDomain": "comk-4302e.firebaseapp.com",
    "databaseURL": "https://comk-4302e-default-rtdb.firebaseio.com",
    "projectId": "comk-4302e",
    "storageBucket": "comk-4302e.firebasestorage.app",
    "messagingSenderId": "817565218754",
    "appId": "1:817565218754:web:874fad2b98ee5789b5c85b",
    "measurementId": "G-DR25TWGM6M"
}

CLOUD_NAME = "dt0tkbtzw"
UPLOAD_PRESET = "xk20_k"
DICEBEAR_URL = "https://api.dicebear.com/7.x/bottts-neutral/svg"

# 🌹 Rose Pink Gradient Colors
COVER_COLORS_JS = """[
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
]"""

ADMIN_EMAILS_JS = "['jasim28v@gmail.com']"

# ═══════════════════════════════════════════════════════════
# 🌹 UTILITY - دوال مساعدة
# ═══════════════════════════════════════════════════════════

TOTAL_LINES = 0

def write(filename, content):
    global TOTAL_LINES
    os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else '.', exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    lines = content.count('\n') + 1
    TOTAL_LINES += lines
    print(f"  ✅ {filename} ({lines} سطر)")

def section(title):
    print(f"\n{'='*60}")
    print(f"  🌹 {title}")
    print(f"{'='*60}")

# ═══════════════════════════════════════════════════════════
# 🌹 1. firebase-config.js
# ═══════════════════════════════════════════════════════════

def build_config():
    return f"""// 🌹 ROSE SPHERE - Configuration
const firebaseConfig = {{
    apiKey: "{FIREBASE_CONFIG['apiKey']}",
    authDomain: "{FIREBASE_CONFIG['authDomain']}",
    databaseURL: "{FIREBASE_CONFIG['databaseURL']}",
    projectId: "{FIREBASE_CONFIG['projectId']}",
    storageBucket: "{FIREBASE_CONFIG['storageBucket']}",
    messagingSenderId: "{FIREBASE_CONFIG['messagingSenderId']}",
    appId: "{FIREBASE_CONFIG['appId']}",
    measurementId: "{FIREBASE_CONFIG['measurementId']}"
}};
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.database();
const CLOUD_NAME = "{CLOUD_NAME}";
const UPLOAD_PRESET = "{UPLOAD_PRESET}";
const ADMIN_EMAILS = {ADMIN_EMAILS_JS};
const DICEBEAR_URL = "{DICEBEAR_URL}";
const COVER_COLORS = {COVER_COLORS_JS};
const APP_NAME = "ROSE SPHERE";
const APP_VERSION = "3.0.0";
console.log('🌹 %c'+APP_NAME+' v'+APP_VERSION+' Ready', 'color: #ec4899; font-size: 16px; font-weight: bold;');
"""

# ═══════════════════════════════════════════════════════════
# 🌹 2. auth.html - تسجيل الدخول والاشتراك
# ═══════════════════════════════════════════════════════════

def build_auth():
    return r"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>🌹 ROSE SPHERE | دخول</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        *{margin:0;padding:0;box-sizing:border-box}
        body{min-height:100vh;background:linear-gradient(135deg, #1a0a14, #3b0a2e, #1a0a14);display:flex;align-items:center;justify-content:center;font-family:'Segoe UI',sans-serif;overflow:hidden}
        .bg-orb{position:fixed;border-radius:50%;filter:blur(100px);opacity:0.3;animation:orbFloat 15s infinite alternate}
        .bg-orb:nth-child(1){width:350px;height:350px;background:#ec4899;top:-80px;left:-80px}
        .bg-orb:nth-child(2){width:300px;height:300px;background:#db2777;bottom:-80px;right:-80px;animation-delay:5s}
        .bg-orb:nth-child(3){width:250px;height:250px;background:#f472b6;top:50%;left:50%;animation-delay:10s}
        @keyframes orbFloat{0%{transform:translate(0,0) scale(1)}100%{transform:translate(40px,-40px) scale(1.2)}}
        .card{position:relative;z-index:1;width:90%;max-width:420px;background:rgba(255,255,255,0.05);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);border-radius:32px;padding:36px 24px;border:1px solid rgba(236,72,153,0.2);box-shadow:0 30px 60px rgba(236,72,153,0.2);animation:fadeUp 0.8s ease}
        @keyframes fadeUp{from{opacity:0;transform:translateY(40px)}to{opacity:1;transform:translateY(0)}}
        .logo{width:70px;height:70px;margin:0 auto 20px;background:linear-gradient(135deg, #ec4899, #f472b6);border-radius:20px;display:flex;align-items:center;justify-content:center;font-size:36px;border:1px solid rgba(236,72,153,0.3);box-shadow:0 15px 40px rgba(236,72,153,0.4)}
        h1{text-align:center;font-size:36px;font-weight:900;background:linear-gradient(to bottom, #fff, #f472b6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:4px}
        .sub{text-align:center;color:rgba(255,255,255,0.5);font-size:13px;margin-bottom:20px}
        .tabs{display:flex;gap:4px;background:rgba(255,255,255,0.06);border-radius:40px;padding:4px;margin-bottom:24px}
        .tab{flex:1;padding:12px;background:none;border:none;color:rgba(255,255,255,0.5);cursor:pointer;border-radius:40px;font-size:14px;transition:all 0.3s;font-weight:500}
        .tab.active{background:linear-gradient(135deg, #ec4899, #f472b6);color:#fff;box-shadow:0 8px 20px rgba(236,72,153,0.4)}
        .form{display:none;animation:fadeIn 0.4s ease}
        .form.active{display:block}
        @keyframes fadeIn{from{opacity:0}to{opacity:1}}
        input{width:100%;padding:15px 18px;margin:8px 0;border-radius:50px;background:rgba(255,255,255,0.05);border:1px solid rgba(236,72,153,0.2);color:#fff;font-size:14px;outline:none;transition:all 0.4s}
        input:focus{border-color:rgba(236,72,153,0.6);box-shadow:0 0 20px rgba(236,72,153,0.2);background:rgba(255,255,255,0.08)}
        input::placeholder{color:rgba(255,255,255,0.3)}
        button{width:100%;padding:15px;margin-top:18px;background:linear-gradient(135deg, #ec4899, #f472b6);border:none;border-radius:50px;color:#fff;font-weight:bold;font-size:15px;cursor:pointer;transition:all 0.3s;box-shadow:0 10px 30px rgba(236,72,153,0.4)}
        button:hover{transform:translateY(-2px);box-shadow:0 20px 40px rgba(236,72,153,0.6)}
        button:active{transform:scale(0.97)}
        button:disabled{opacity:0.5;pointer-events:none}
        .msg{text-align:center;color:#fca5a5;font-size:13px;margin-top:12px;min-height:20px}
        .msg.success{color:#4ade80}
        .or-divider{text-align:center;margin:20px 0;color:rgba(255,255,255,0.3);font-size:12px;position:relative}
        .or-divider::before,.or-divider::after{content:'';position:absolute;top:50%;width:40%;height:1px;background:rgba(255,255,255,0.1)}
        .or-divider::before{right:0}.or-divider::after{left:0}
        .google-btn{width:100%;padding:12px;margin-top:8px;background:rgba(255,255,255,0.1);border:1px solid rgba(236,72,153,0.2);border-radius:50px;color:#fff;font-weight:500;font-size:14px;cursor:pointer;transition:all 0.3s;display:flex;align-items:center;justify-content:center;gap:10px}
        .google-btn:hover{background:rgba(236,72,153,0.2)}
    </style>
</head>
<body>
    <div class="bg-orb"></div><div class="bg-orb"></div><div class="bg-orb"></div>
    <div class="card">
        <div class="logo">🌹</div>
        <h1>ROSE SPHERE</h1>
        <p class="sub">عالمك الوردي الخاص 🌸</p>
        <div class="tabs">
            <button class="tab active" id="tabLogin" onclick="switchTab('login')">دخول</button>
            <button class="tab" id="tabRegister" onclick="switchTab('register')">اشتراك</button>
        </div>
        <div id="formLogin" class="form active">
            <input type="email" id="loginEmail" placeholder="📧 البريد الإلكتروني" autocomplete="email">
            <input type="password" id="loginPass" placeholder="🔒 كلمة المرور" autocomplete="current-password">
            <button id="btnLogin" onclick="doLogin()">🌹 تسجيل الدخول</button>
            <div class="or-divider">أو</div>
            <button class="google-btn" onclick="loginWithGoogle()"><i class="fab fa-google"></i> الدخول عبر Google</button>
            <div class="msg" id="loginMsg"></div>
        </div>
        <div id="formRegister" class="form">
            <input type="text" id="regName" placeholder="👤 اسم المستخدم" autocomplete="username">
            <input type="email" id="regEmail" placeholder="📧 البريد الإلكتروني" autocomplete="email">
            <input type="password" id="regPass" placeholder="🔒 كلمة المرور (6 أحرف على الأقل)" autocomplete="new-password">
            <button id="btnRegister" onclick="doRegister()">💖 إنشاء حساب</button>
            <div class="msg" id="regMsg"></div>
        </div>
    </div>
    <script src="firebase-config.js"></script>
    <script>
        function switchTab(type){
            document.getElementById('tabLogin').classList.remove('active');
            document.getElementById('tabRegister').classList.remove('active');
            document.getElementById('formLogin').classList.remove('active');
            document.getElementById('formRegister').classList.remove('active');
            document.getElementById('loginMsg').innerText = '';
            document.getElementById('regMsg').innerText = '';
            if(type === 'login'){
                document.getElementById('tabLogin').classList.add('active');
                document.getElementById('formLogin').classList.add('active');
            } else {
                document.getElementById('tabRegister').classList.add('active');
                document.getElementById('formRegister').classList.add('active');
            }
        }
        async function doLogin(){
            const email = document.getElementById('loginEmail').value.trim();
            const password = document.getElementById('loginPass').value;
            const msg = document.getElementById('loginMsg');
            const btn = document.getElementById('btnLogin');
            if(!email || !password){msg.innerText = '❌ الرجاء ملء جميع الحقول';return;}
            btn.disabled = true; btn.innerHTML = '⏳ جاري الدخول...'; msg.innerText = ''; msg.className = 'msg';
            try {
                const result = await auth.signInWithEmailAndPassword(email, password);
                await db.ref('users/' + result.user.uid + '/lastSeen').set(Date.now());
                window.location.replace('index.html');
            } catch(error) {
                btn.disabled = false; btn.innerHTML = '🌹 تسجيل الدخول';
                msg.innerText = error.code === 'auth/user-not-found' ? '❌ لا يوجد حساب بهذا البريد' : error.code === 'auth/wrong-password' || error.code === 'auth/invalid-credential' ? '❌ كلمة المرور غير صحيحة' : error.code === 'auth/too-many-requests' ? '❌ محاولات كثيرة' : error.code === 'auth/user-disabled' ? '❌ هذا الحساب محظور' : '❌ خطأ: ' + error.message;
            }
        }
        async function doRegister(){
            const username = document.getElementById('regName').value.trim();
            const email = document.getElementById('regEmail').value.trim();
            const password = document.getElementById('regPass').value;
            const msg = document.getElementById('regMsg');
            const btn = document.getElementById('btnRegister');
            if(!username || !email || !password){msg.innerText = '❌ الرجاء ملء جميع الحقول';return;}
            if(username.length < 3){msg.innerText = '❌ اسم المستخدم 3 أحرف على الأقل';return;}
            if(password.length < 6){msg.innerText = '❌ كلمة المرور 6 أحرف على الأقل';return;}
            if(!email.includes('@') || !email.includes('.')){msg.innerText = '❌ بريد إلكتروني غير صالح';return;}
            btn.disabled = true; btn.innerHTML = '⏳ جاري إنشاء الحساب...'; msg.innerText = ''; msg.className = 'msg';
            try {
                const userCredential = await auth.createUserWithEmailAndPassword(email, password);
                const uid = userCredential.user.uid;
                const avatarUrl = DICEBEAR_URL + '?seed=' + uid;
                const coverColor = COVER_COLORS[Math.floor(Math.random() * COVER_COLORS.length)];
                const userData = {username, email, bio: '🌸 مرحباً! أنا جديد في Rose Sphere', avatarUrl, hasCustomAvatar: false, coverColor, followers: {}, following: {}, totalLikes: 0, isVerified: false, verifiedAt: null, verifiedBy: null, banned: false, banReason: '', createdAt: Date.now(), lastSeen: Date.now(), posts: {}, website: '', location: ''};
                await db.ref('users/' + uid).set(userData);
                msg.innerText = '✅ تم إنشاء الحساب بنجاح! جاري التوجيه...';
                msg.className = 'msg success';
                setTimeout(() => window.location.replace('index.html'), 800);
            } catch(error) {
                btn.disabled = false; btn.innerHTML = '💖 إنشاء حساب'; msg.className = 'msg';
                msg.innerText = error.code === 'auth/email-already-in-use' ? '❌ البريد الإلكتروني مستخدم بالفعل' : error.code === 'auth/weak-password' ? '❌ كلمة المرور ضعيفة جداً' : '❌ خطأ: ' + (error.message || 'غير معروف');
            }
        }
        async function loginWithGoogle(){
            const provider = new firebase.auth.GoogleAuthProvider();
            try {
                const result = await auth.signInWithPopup(provider);
                const user = result.user;
                const snap = await db.ref('users/' + user.uid).get();
                if (!snap.exists()) {
                    const avatarUrl = DICEBEAR_URL + '?seed=' + user.uid;
                    await db.ref('users/' + user.uid).set({username: user.displayName || user.email.split('@')[0], email: user.email, bio: '🌸 مرحباً! أنا جديد في Rose Sphere', avatarUrl, hasCustomAvatar: false, coverColor: COVER_COLORS[Math.floor(Math.random() * COVER_COLORS.length)], followers: {}, following: {}, totalLikes: 0, isVerified: false, banned: false, createdAt: Date.now(), lastSeen: Date.now(), posts: {}, website: '', location: ''});
                }
                await db.ref('users/' + user.uid + '/lastSeen').set(Date.now());
                window.location.replace('index.html');
            } catch(error) {
                document.getElementById('loginMsg').innerText = '❌ خطأ في تسجيل الدخول';
            }
        }
        document.querySelectorAll('input').forEach(input => {
            input.addEventListener('keydown', function(e) {
                if(e.key === 'Enter') {
                    e.preventDefault();
                    document.getElementById('formLogin').classList.contains('active') ? doLogin() : doRegister();
                }
            });
        });
        auth.onAuthStateChanged(user => { if(user) window.location.replace('index.html'); });
    </script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 🌹 3. index.html - الرئيسية
# ═══════════════════════════════════════════════════════════

def build_index():
    return r"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>🌹 ROSE SPHERE | الرئيسية</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root{--glass:rgba(255,255,255,0.03);--border:rgba(236,72,153,0.15);--accent:#ec4899;--accent2:#f472b6;--bg:#1a0a14}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:#fff;height:100vh;overflow:hidden;-webkit-tap-highlight-color:transparent;user-select:none}
        #loaderScreen{position:fixed;inset:0;z-index:9999;background:linear-gradient(135deg, #1a0a14, #3b0a2e, #1a0a14);display:flex;align-items:center;justify-content:center;flex-direction:column;gap:16px}
        .spinner-big{width:50px;height:50px;border:4px solid rgba(236,72,153,0.2);border-top-color:var(--accent);border-radius:50%;animation:spin 0.8s linear infinite}
        @keyframes spin{to{transform:rotate(360deg)}}
        #mainApp{display:none;height:100vh;position:relative}
        .topbar{position:fixed;top:0;left:0;right:0;z-index:100;display:flex;justify-content:space-between;align-items:center;padding:12px 20px;background:rgba(26,10,20,0.7);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border-bottom:1px solid var(--border)}
        .logo-icon{width:36px;height:36px;background:linear-gradient(135deg,var(--accent),var(--accent2));border-radius:10px;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:14px;box-shadow:0 8px 20px rgba(236,72,153,0.4)}
        .tabs{display:flex;gap:4px;background:var(--glass);border-radius:30px;padding:3px}
        .tab{background:none;border:none;color:rgba(255,255,255,0.5);padding:7px 16px;cursor:pointer;border-radius:25px;font-size:13px;font-weight:500;transition:all 0.3s}
        .tab.active{background:rgba(236,72,153,0.3);color:#fff}
        .videos-wrap{height:100vh;overflow-y:scroll;scroll-snap-type:y mandatory;scrollbar-width:none;-ms-overflow-style:none}
        .videos-wrap::-webkit-scrollbar{display:none}
        .vid-card{height:100vh;scroll-snap-align:start;position:relative;background:#000}
        .vid-card video{width:100%;height:100%;object-fit:contain;background:#000}
        .vid-info{position:absolute;bottom:90px;left:14px;right:80px;z-index:20;text-shadow:0 2px 10px rgba(0,0,0,0.8)}
        .author-row{display:flex;align-items:center;gap:10px;margin-bottom:6px}
        .author-avatar{width:46px;height:46px;border-radius:50%;overflow:hidden;cursor:pointer;border:2px solid rgba(236,72,153,0.5);box-shadow:0 8px 20px rgba(0,0,0,0.4)}
        .author-avatar img{width:100%;height:100%;object-fit:cover}
        .author-name{font-weight:700;font-size:15px;cursor:pointer;display:flex;align-items:center;gap:6px}
        .verify-badge{display:inline-flex;align-items:center;justify-content:center;width:18px;height:18px;border-radius:50%;background:linear-gradient(135deg, #ec4899, #f472b6);box-shadow:0 0 10px rgba(236,72,153,0.5);font-size:9px;color:#fff;flex-shrink:0;margin:0 4px;vertical-align:middle}
        .btn-follow{background:linear-gradient(135deg,var(--accent),var(--accent2));padding:5px 14px;border-radius:20px;font-size:11px;font-weight:700;border:none;color:#fff;cursor:pointer;box-shadow:0 4px 15px rgba(236,72,153,0.4)}
        .caption{font-size:14px;margin-bottom:5px;line-height:1.4}
        .side-btns{position:absolute;right:14px;bottom:130px;display:flex;flex-direction:column;gap:22px;z-index:20}
        .sbtn{display:flex;flex-direction:column;align-items:center;gap:3px;background:none;border:none;color:#fff;cursor:pointer;font-size:10px;transition:transform 0.15s}
        .sbtn:active{transform:scale(0.85)}
        .sbtn i{font-size:28px;filter:drop-shadow(0 3px 8px rgba(0,0,0,0.5))}
        .sbtn.liked i{color:#f472b6}
        .nav-bottom{position:fixed;bottom:0;left:0;right:0;display:flex;justify-content:space-around;align-items:center;padding:8px 0 20px;background:rgba(26,10,20,0.8);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);z-index:100;border-top:1px solid var(--border)}
        .nav-item{display:flex;flex-direction:column;align-items:center;gap:3px;background:none;border:none;color:rgba(255,255,255,0.5);font-size:10px;cursor:pointer;transition:all 0.3s;text-decoration:none}
        .nav-item i{font-size:22px}
        .nav-item.active{color:var(--accent2)}
        .btn-add{width:48px;height:48px;background:linear-gradient(135deg,var(--accent),var(--accent2));border-radius:50%;display:flex;align-items:center;justify-content:center;margin-top:-24px;cursor:pointer;box-shadow:0 10px 30px rgba(236,72,153,0.6);border:none;color:#fff;font-size:20px;text-decoration:none}
        .toast{position:fixed;bottom:100px;left:50%;transform:translateX(-50%);background:rgba(26,10,20,0.9);padding:10px 22px;border-radius:50px;z-index:1000;opacity:0;transition:opacity 0.3s;pointer-events:none;border:1px solid var(--border);font-size:13px}
        .toast.show{opacity:1}
        .overlay{position:fixed;inset:0;background:rgba(26,10,20,0.97);backdrop-filter:blur(40px);z-index:400;overflow-y:auto}
        .overlay-header{display:flex;justify-content:space-between;align-items:center;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(26,10,20,0.8)}
        .btn-close{background:rgba(236,72,153,0.1);border:1px solid var(--border);color:#fff;width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:18px}
        .share-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;padding:20px;text-align:center}
        .share-item{display:flex;flex-direction:column;align-items:center;gap:8px;cursor:pointer;padding:12px;border-radius:16px;transition:all 0.2s;background:rgba(255,255,255,0.03)}
        .share-item:hover{background:rgba(236,72,153,0.1);transform:scale(1.05)}
        .share-item i{font-size:32px;padding:12px;border-radius:50%}
        .share-item span{font-size:11px;opacity:0.7}
    </style>
</head>
<body>
<div id="loaderScreen"><div class="spinner-big"></div><p style="color:rgba(255,255,255,0.6);font-size:15px">🌹 جاري التحميل...</p></div>
<div id="mainApp">
    <div class="topbar">
        <div style="display:flex;align-items:center">
            <div class="logo-icon">🌹</div>
            <span style="font-weight:800;font-size:17px;background:linear-gradient(to bottom,#fff,#f472b6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-left:8px">ROSE</span>
        </div>
        <div class="tabs">
            <button class="tab" onclick="switchFeed('following')">متابَعين</button>
            <button class="tab active" onclick="switchFeed('forYou')">استكشاف</button>
        </div>
    </div>
    <div class="videos-wrap" id="videosWrap">
        <div style="display:flex;align-items:center;justify-content:center;height:100vh;color:rgba(255,255,255,0.5);flex-direction:column;gap:12px">
            <i class="fas fa-video" style="font-size:48px;opacity:0.3;color:#ec4899"></i>
            <p>لا توجد فيديوهات بعد</p>
            <p style="font-size:12px;opacity:0.5">كن أول من يشارك! 🌸</p>
        </div>
    </div>
    <div class="nav-bottom">
        <a href="index.html" class="nav-item active"><i class="fas fa-home"></i><span>الرئيسية</span></a>
        <a href="explore.html" class="nav-item"><i class="fas fa-compass"></i><span>استكشاف</span></a>
        <a href="upload.html" class="btn-add"><i class="fas fa-plus"></i></a>
        <a href="chat.html" class="nav-item"><i class="fas fa-envelope"></i><span>رسائل</span></a>
        <a href="profile.html" class="nav-item"><i class="fas fa-user"></i><span>ملفي</span></a>
    </div>
    <div id="toast" class="toast">✅ تم</div>
</div>
<script src="firebase-config.js"></script>
<script>
    let currentUser = null, currentUserData = null, allUsers = {}, allVideos = [], currentFeed = 'forYou', isMuted = true;
    auth.onAuthStateChanged(async (user) => {
        if (!user) { window.location.replace('auth.html'); return; }
        currentUser = user;
        const snap = await db.ref('users/' + user.uid).get();
        if (snap.exists()) currentUserData = { uid: user.uid, ...snap.val() };
        if (currentUserData && currentUserData.banned) { alert('❌ حسابك محظور'); auth.signOut(); return; }
        await db.ref('users/' + user.uid + '/lastSeen').set(Date.now());
        db.ref('users').on('value', s => { allUsers = s.val() || {}; });
        db.ref('videos').on('value', s => {
            const data = s.val();
            allVideos = data ? Object.entries(data).map(([k,v]) => ({id:k, ...v})).sort((a,b) => (b.timestamp||0)-(a.timestamp||0)) : [];
            renderVideos();
        });
        db.ref('presence/' + user.uid).set(true); db.ref('presence/' + user.uid).onDisconnect().remove();
        document.getElementById('loaderScreen').style.display = 'none'; document.getElementById('mainApp').style.display = 'block';
    });
    function renderVideos() {
        const container = document.getElementById('videosWrap');
        let filtered = currentFeed === 'forYou' ? allVideos : allVideos.filter(v => currentUserData?.following?.[v.sender]);
        if (!filtered.length) { container.innerHTML = '<div style="display:flex;align-items:center;justify-content:center;height:100vh;color:rgba(255,255,255,0.5);flex-direction:column;gap:12px"><i class="fas fa-video" style="font-size:48px;opacity:0.3;color:#ec4899"></i><p>'+(currentFeed==='forYou'?'لا توجد فيديوهات بعد':'تابع مستخدمين لرؤية فيديوهاتهم')+'</p></div>'; return; }
        container.innerHTML = '';
        filtered.forEach(video => {
            const isLiked = video.likedBy && video.likedBy[currentUser?.uid];
            const user = allUsers[video.sender] || { username: video.senderName || 'مستخدم' };
            const isFollowing = currentUserData?.following && currentUserData.following[video.sender];
            const commentsCount = video.comments ? Object.keys(video.comments).length : 0;
            const avatarUrl = user.avatarUrl || (DICEBEAR_URL + '?seed=' + video.sender);
            const div = document.createElement('div'); div.className = 'vid-card';
            div.innerHTML = '<video loop playsinline muted data-src="'+video.url+'" poster="'+(video.thumbnail||'')+'"></video>'+
                '<div class="vid-info"><div class="author-row"><div class="author-avatar" onclick="window.location.href=\'profile.html?uid='+video.sender+'\'"><img src="'+avatarUrl+'" alt="avatar"></div>'+
                '<div class="author-name"><span onclick="window.location.href=\'profile.html?uid='+video.sender+'\'">@'+user.username+'</span>'+(user.isVerified?'<span class="verify-badge"><i class="fas fa-check"></i></span>':'')+
                (currentUser?.uid !== video.sender ? '<button class="btn-follow" onclick="toggleFollow(\''+video.sender+'\', this)">'+(isFollowing?'متابِع':'متابعة')+'</button>' : '')+
                '</div></div><div class="caption">'+(video.description||'')+'</div></div>'+
                '<div class="side-btns"><button class="sbtn" onclick="toggleMute()"><i class="fas '+(isMuted?'fa-volume-mute':'fa-volume-up')+'"></i></button>'+
                '<button class="sbtn like-btn '+(isLiked?'liked':'')+'" onclick="toggleLike(\''+video.id+'\', this)"><i class="fas fa-heart"></i><span>'+(video.likes||0)+'</span></button>'+
                '<button class="sbtn" onclick="openComments(\''+video.id+'\')"><i class="fas fa-comment"></i><span>'+commentsCount+'</span></button>'+
                '<button class="sbtn" onclick="openShare(\''+video.url+'\', \''+(video.description||'فيديو')+'\')"><i class="fas fa-share"></i></button></div>';
            const videoEl = div.querySelector('video'); videoEl.addEventListener('dblclick', e => { e.stopPropagation(); const likeBtn = div.querySelector('.like-btn'); if (likeBtn) toggleLike(video.id, likeBtn); });
            container.appendChild(div);
        });
        initVideoObserver();
    }
    function initVideoObserver() {
        const observer = new IntersectionObserver(entries => { entries.forEach(entry => { const video = entry.target.querySelector('video'); if (entry.isIntersecting) { if (!video.src) video.src = video.dataset.src; video.muted = isMuted; video.play().catch(() => {}); } else { video.pause(); } }); }, { threshold: 0.65 });
        document.querySelectorAll('.vid-card').forEach(seg => observer.observe(seg));
    }
    function toggleMute() { isMuted = !isMuted; document.querySelectorAll('video').forEach(v => v.muted = isMuted); }
    function switchFeed(feed) { currentFeed = feed; document.querySelectorAll('.tab').forEach(t => t.classList.remove('active')); event.target.classList.add('active'); renderVideos(); }
    async function toggleLike(videoId, btn) {
        if (!currentUser) return; const ref = db.ref('videos/' + videoId); const snap = await ref.get(); const video = snap.val(); if (!video) return;
        let likes = video.likes || 0, likedBy = video.likedBy || {};
        if (likedBy[currentUser.uid]) { likes--; delete likedBy[currentUser.uid]; } else { likes++; likedBy[currentUser.uid] = true; }
        await ref.update({ likes, likedBy }); btn.classList.toggle('liked'); const countSpan = btn.querySelector('span'); if (countSpan) countSpan.innerText = likes;
    }
    async function toggleFollow(userId, btn) {
        if (!currentUser || currentUser.uid === userId) return;
        const userRef = db.ref('users/' + currentUser.uid + '/following/' + userId), targetRef = db.ref('users/' + userId + '/followers/' + currentUser.uid);
        const snap = await userRef.get();
        if (snap.exists()) { await userRef.remove(); await targetRef.remove(); btn.innerText = 'متابعة'; }
        else { await userRef.set(true); await targetRef.set(true); btn.innerText = 'متابِع'; db.ref('notifications/' + userId).push({ from: currentUserData?.username || 'مستخدم', msg: 'بدأ بمتابعتك 🌹', type: 'follow', timestamp: Date.now(), read: false }); }
    }
    function openShare(url, title) {
        const overlayId = 'overlay_' + Date.now();
        const overlay = document.createElement('div'); overlay.className = 'overlay'; overlay.id = overlayId;
        overlay.innerHTML = '<div class="overlay-header"><h3>📤 مشاركة</h3><button class="btn-close" onclick="document.getElementById(\''+overlayId+'\').remove()"><i class="fas fa-times"></i></button></div>'+
            '<div class="share-grid">'+
            '<div class="share-item" onclick="copyLink(\''+url+'\',\''+overlayId+'\')"><i class="fas fa-link" style="background:rgba(236,72,153,0.2);color:#ec4899"></i><span>نسخ الرابط</span></div>'+
            '<div class="share-item" onclick="shareWA(\''+url+'\',\''+title+'\',\''+overlayId+'\')"><i class="fab fa-whatsapp" style="background:rgba(37,211,102,0.2);color:#25d366"></i><span>واتساب</span></div>'+
            '<div class="share-item" onclick="shareTG(\''+url+'\',\''+title+'\',\''+overlayId+'\')"><i class="fab fa-telegram" style="background:rgba(0,136,204,0.2);color:#08c"></i><span>تيليجرام</span></div>'+
            '<div class="share-item" onclick="shareFB(\''+url+'\',\''+overlayId+'\')"><i class="fab fa-facebook" style="background:rgba(24,119,242,0.2);color:#1877f2"></i><span>فيسبوك</span></div>'+
            '</div>';
        document.body.appendChild(overlay);
        window.copyLink = function(u, oid){ navigator.clipboard.writeText(u); document.getElementById(oid).remove(); const toast = document.getElementById('toast'); toast.innerHTML='✅ تم نسخ الرابط'; toast.classList.add('show'); setTimeout(()=>toast.classList.remove('show'),2000); };
        window.shareWA = function(u, t, oid){ window.open('https://wa.me/?text='+encodeURIComponent(t+'\n'+u), '_blank'); document.getElementById(oid).remove(); };
        window.shareTG = function(u, t, oid){ window.open('https://t.me/share/url?url='+encodeURIComponent(u)+'&text='+encodeURIComponent(t), '_blank'); document.getElementById(oid).remove(); };
        window.shareFB = function(u, oid){ window.open('https://www.facebook.com/sharer/sharer.php?u='+encodeURIComponent(u), '_blank'); document.getElementById(oid).remove(); };
    }
    async function openComments(videoId) {
        const snap = await db.ref('videos/' + videoId + '/comments').get(); const comments = snap.val() || {}; let commentsList = '';
        Object.values(comments).reverse().forEach(c => { const user = allUsers[c.userId] || { username: c.username || 'مستخدم' };
            commentsList += '<div style="display:flex;gap:10px;padding:10px 0;border-bottom:1px solid rgba(236,72,153,0.1)"><img src="'+(user.avatarUrl||(DICEBEAR_URL+'?seed='+c.userId))+'" style="width:36px;height:36px;border-radius:50%"><div><div style="font-weight:600">@'+user.username+'</div><div style="font-size:13px;opacity:0.8;margin-top:2px">'+c.text+'</div></div></div>'; });
        const overlayId = 'overlay_' + Date.now(); const overlay = document.createElement('div'); overlay.className = 'overlay'; overlay.id = overlayId;
        overlay.innerHTML = '<div class="overlay-header"><h3>💬 التعليقات</h3><button class="btn-close" onclick="document.getElementById(\''+overlayId+'\').remove()"><i class="fas fa-times"></i></button></div><div style="padding:16px">'+(commentsList||'<p style="opacity:0.5;text-align:center">لا توجد تعليقات</p>')+'<div style="display:flex;gap:8px;padding-top:12px"><input id="cmtInput_'+overlayId+'" placeholder="أضف تعليقاً..." style="flex:1;padding:12px;border-radius:30px;background:rgba(255,255,255,0.05);border:1px solid rgba(236,72,153,0.15);color:#fff;outline:none"><button onclick="addComment(\''+videoId+'\', \''+overlayId+'\')" style="background:linear-gradient(135deg,#ec4899,#f472b6);border:none;color:#fff;padding:12px 20px;border-radius:30px;cursor:pointer">نشر</button></div></div>';
        document.body.appendChild(overlay);
        window.addComment = async function(vid, oid) { const input = document.getElementById('cmtInput_' + oid); if (!input || !input.value.trim()) return; await db.ref('videos/' + vid + '/comments').push({ userId: currentUser.uid, username: currentUserData?.username || 'مستخدم', text: input.value, timestamp: Date.now() }); document.getElementById(oid).remove(); openComments(vid); };
    }
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 🌹 4. profile.html - الملف الشخصي + لوحة الأدمن + واجهة تعديل
# ═══════════════════════════════════════════════════════════

def build_profile():
    return r"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>🌹 ROSE SPHERE | ملفي</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root{--glass:rgba(255,255,255,0.03);--border:rgba(236,72,153,0.15);--accent:#ec4899;--accent2:#f472b6;--bg:#1a0a14}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:#fff;min-height:100vh;overflow-y:auto;overflow-x:hidden}
        .load-center{display:flex;align-items:center;justify-content:center;min-height:100vh;flex-direction:column;gap:12px;color:rgba(255,255,255,0.5)}
        .spinner{width:40px;height:40px;border:3px solid rgba(236,72,153,0.2);border-top-color:var(--accent);border-radius:50%;animation:spin 0.7s linear infinite}
        @keyframes spin{to{transform:rotate(360deg)}}
        .cover-section{position:relative;height:250px;display:flex;align-items:flex-end;justify-content:center;padding-bottom:50px;transition:background 0.5s}
        .btn-back{position:fixed;top:16px;right:16px;background:rgba(0,0,0,0.5);backdrop-filter:blur(10px);width:42px;height:42px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:50;border:1px solid rgba(236,72,153,0.2);color:#fff;font-size:18px;transition:all 0.3s}
        .btn-cover-edit{position:absolute;top:16px;left:16px;background:rgba(0,0,0,0.4);backdrop-filter:blur(10px);border:1px solid rgba(236,72,153,0.2);color:#fff;padding:8px 16px;border-radius:20px;font-size:12px;cursor:pointer;z-index:50;transition:all 0.3s}
        .avatar-container{width:120px;height:120px;border-radius:50%;overflow:hidden;border:4px solid rgba(236,72,153,0.6);box-shadow:0 12px 40px rgba(236,72,153,0.3);cursor:pointer;position:relative;z-index:2;transition:transform 0.3s}
        .avatar-container:hover{transform:scale(1.05)}
        .avatar-container img{width:100%;height:100%;object-fit:cover}
        .avatar-edit-overlay{position:absolute;inset:0;background:rgba(0,0,0,0.5);display:flex;align-items:center;justify-content:center;opacity:0;transition:opacity 0.3s;font-size:24px}
        .avatar-container:hover .avatar-edit-overlay{opacity:1}
        .profile-info{text-align:center;padding:10px 20px 0}
        .username-display{font-size:24px;font-weight:800;display:flex;align-items:center;justify-content:center;gap:8px;flex-wrap:wrap}
        .verify-badge{display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;border-radius:50%;background:linear-gradient(135deg, #ec4899, #f472b6);box-shadow:0 0 12px rgba(236,72,153,0.5);font-size:11px;color:#fff;flex-shrink:0;margin:0 4px;vertical-align:middle}
        .banned-badge{color:#f87171;font-size:13px;background:rgba(239,68,68,0.2);padding:4px 12px;border-radius:20px}
        .bio-display{font-size:14px;opacity:0.7;margin:8px 0;line-height:1.6}
        .meta-info{display:flex;justify-content:center;gap:20px;flex-wrap:wrap;font-size:12px;opacity:0.6;margin:8px 0}
        .last-seen{font-size:11px;opacity:0.4;margin:4px 0}
        .stats-row{display:flex;justify-content:center;gap:35px;margin:20px 0}
        .stat-item{text-align:center;cursor:pointer;transition:transform 0.2s;padding:8px;border-radius:12px}
        .stat-item:hover{transform:scale(1.05);background:rgba(236,72,153,0.05)}
        .stat-number{font-size:24px;font-weight:800;background:linear-gradient(135deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
        .stat-label{font-size:12px;opacity:0.5;margin-top:2px}
        .action-buttons{display:flex;justify-content:center;gap:10px;flex-wrap:wrap;margin:16px 0}
        .btn{padding:10px 24px;border-radius:30px;font-size:14px;font-weight:600;cursor:pointer;border:none;transition:all 0.3s;display:flex;align-items:center;gap:6px}
        .btn-primary{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;box-shadow:0 8px 25px rgba(236,72,153,0.3)}
        .btn-outline{background:rgba(255,255,255,0.05);border:1px solid var(--border);color:#fff}
        .btn-danger{background:rgba(239,68,68,0.2);border:1px solid rgba(239,68,68,0.3);color:#f87171}
        .profile-tabs{display:flex;border-bottom:1px solid var(--border);margin-top:10px;position:sticky;top:0;background:rgba(26,10,20,0.9);backdrop-filter:blur(20px);z-index:30}
        .profile-tab{flex:1;padding:14px;text-align:center;cursor:pointer;font-size:14px;font-weight:500;color:rgba(255,255,255,0.5);border-bottom:2px solid transparent;transition:all 0.3s;background:none;border-left:none;border-right:none;border-top:none}
        .profile-tab.active{color:#fff;border-bottom-color:var(--accent)}
        .tab-content{display:none;padding:12px}
        .tab-content.active{display:block}
        .grid{display:grid;grid-template-columns:repeat(3,1fr);gap:4px}
        .thumb{aspect-ratio:9/16;background:rgba(255,255,255,0.03);border-radius:8px;display:flex;align-items:center;justify-content:center;cursor:pointer;position:relative;overflow:hidden;transition:transform 0.2s}
        .thumb:hover{transform:scale(1.03);z-index:1}
        .thumb img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
        .thumb .delete-btn{position:absolute;top:4px;right:4px;width:24px;height:24px;background:rgba(239,68,68,0.8);border-radius:50%;display:flex;align-items:center;justify-content:center;z-index:3;font-size:10px;cursor:pointer;opacity:0;transition:opacity 0.3s}
        .thumb:hover .delete-btn{opacity:1}
        .modal-overlay{position:fixed;inset:0;background:rgba(26,10,20,0.95);backdrop-filter:blur(30px);z-index:500;display:flex;flex-direction:column}
        .modal-header{display:flex;justify-content:space-between;align-items:center;padding:16px;border-bottom:1px solid var(--border)}
        .modal-body{flex:1;overflow-y:auto;padding:16px}
        .user-list-item{display:flex;align-items:center;gap:12px;padding:14px;border-bottom:1px solid var(--border);cursor:pointer;transition:background 0.2s}
        .user-list-item:hover{background:rgba(236,72,153,0.05)}
        .user-list-avatar{width:48px;height:48px;border-radius:50%;overflow:hidden;flex-shrink:0}
        .user-list-avatar img{width:100%;height:100%;object-fit:cover}
        .admin-section{margin:20px 16px;padding:20px;background:rgba(236,72,153,0.05);border-radius:20px;border:1px solid rgba(236,72,153,0.2)}
        .admin-title{font-size:18px;font-weight:700;color:#ec4899;margin-bottom:16px;display:flex;align-items:center;gap:8px}
        .admin-stats-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-bottom:20px}
        .admin-stat-card{background:rgba(0,0,0,0.3);border-radius:12px;padding:14px;text-align:center}
        .admin-stat-num{font-size:24px;font-weight:800;color:#ec4899}
        .admin-stat-lbl{font-size:10px;opacity:0.5;margin-top:4px}
        .admin-user-item{display:flex;justify-content:space-between;align-items:center;background:rgba(0,0,0,0.3);padding:12px;border-radius:12px;margin-bottom:6px;flex-wrap:wrap;gap:8px}
        .admin-btn-sm{padding:6px 12px;border-radius:20px;font-size:11px;cursor:pointer;border:none;font-weight:600;color:#fff;transition:all 0.2s;white-space:nowrap}
        .btn-verify-user{background:rgba(52,211,153,0.3);color:#34d399}
        .btn-ban-user{background:rgba(239,68,68,0.3);color:#f87171}
        .btn-unban-user{background:rgba(52,211,153,0.3);color:#34d399}
        .btn-delete-video{background:rgba(239,68,68,0.3);color:#f87171}
        .btn-broadcast{background:rgba(236,72,153,0.3);color:#ec4899}
        .edit-form-group{margin-bottom:16px}
        .edit-form-group label{display:block;font-size:13px;opacity:0.7;margin-bottom:6px}
        .edit-form-group input,.edit-form-group textarea{width:100%;padding:14px 16px;border-radius:16px;background:rgba(255,255,255,0.05);border:1px solid rgba(236,72,153,0.2);color:#fff;font-size:14px;outline:none;font-family:'Segoe UI',sans-serif;resize:none;transition:border-color 0.3s}
        .edit-form-group input:focus,.edit-form-group textarea:focus{border-color:var(--accent)}
        .edit-form-group textarea{min-height:80px}
    </style>
</head>
<body>
<div id="loader" class="load-center"><div class="spinner"></div><span>🌹 تحميل الملف الشخصي...</span></div>
<div id="content" style="display:none">
    <div class="cover-section" id="profileCover">
        <button class="btn-back" onclick="goBack()"><i class="fas fa-arrow-right"></i></button>
        <button class="btn-cover-edit" id="editCoverBtn"><i class="fas fa-palette"></i> تغيير الغلاف</button>
        <div class="avatar-container" id="avatarDisplay">
            <img src="" alt="avatar" id="avatarImg">
            <div class="avatar-edit-overlay"><i class="fas fa-camera"></i></div>
        </div>
    </div>
    <input type="file" id="avatarInput" accept="image/*" style="display:none" onchange="uploadAvatar(this)">
    <div class="profile-info">
        <div class="username-display">
            <span id="nameDisplay">@username</span>
            <span class="verify-badge" id="verifiedBadge" style="display:none"><i class="fas fa-check"></i></span>
            <span class="banned-badge" id="bannedBadge" style="display:none"><i class="fas fa-ban"></i> محظور</span>
        </div>
        <div class="bio-display" id="bioDisplay">🌸 مرحباً!</div>
        <div class="last-seen" id="lastSeen"></div>
        <div class="meta-info">
            <span id="locationDisplay" style="display:none"><i class="fas fa-map-marker-alt"></i> <span></span></span>
            <span id="websiteDisplay" style="display:none"><i class="fas fa-globe"></i> <a class="website-link" href="#" target="_blank" style="color:#ec4899"></a></span>
            <span><i class="fas fa-calendar-alt"></i> <span id="joinedDate"></span></span>
        </div>
    </div>
    <div class="stats-row">
        <div class="stat-item" id="statPosts"><div class="stat-number">0</div><div class="stat-label">منشورات</div></div>
        <div class="stat-item" id="statFollowers"><div class="stat-number">0</div><div class="stat-label">متابعون</div></div>
        <div class="stat-item" id="statFollowing"><div class="stat-number">0</div><div class="stat-label">يتابع</div></div>
        <div class="stat-item" id="statLikes"><div class="stat-number">0</div><div class="stat-label">إعجابات</div></div>
    </div>
    <div class="action-buttons" id="actionsBar"></div>
    <div class="profile-tabs">
        <button class="profile-tab active" onclick="switchProfileTab('videos', this)"><i class="fas fa-th"></i> المنشورات</button>
        <button class="profile-tab" onclick="switchProfileTab('liked', this)"><i class="fas fa-heart"></i> أعجبني</button>
    </div>
    <div class="tab-content active" id="tabVideos"><div class="grid" id="videosGrid"></div></div>
    <div class="tab-content" id="tabLiked"><div class="grid" id="likedGrid"></div></div>
    <div id="adminSection" style="display:none"></div>
</div>
<script src="firebase-config.js"></script>
<script>
    let profileUserId=null,currentUser=null,currentUserData=null,allUsers={},allVideos=[],isOwnProfile=false,isAdmin=false;
    const params=new URLSearchParams(window.location.search);
    profileUserId=params.get('uid');
    auth.onAuthStateChanged(async u=>{if(!u){window.location.href='auth.html';return}currentUser=u;const snap=await db.ref('users/'+u.uid).get();if(snap.exists())currentUserData={uid:u.uid,...snap.val()};if(!profileUserId)profileUserId=u.uid;isOwnProfile=(profileUserId===u.uid);isAdmin=ADMIN_EMAILS.includes(u.email||'');await loadAllData();await loadProfile();document.getElementById('loader').style.display='none';document.getElementById('content').style.display='block';if(isAdmin){document.getElementById('adminSection').style.display='block';loadAdminPanel();}});
    async function loadAllData(){const us=await db.ref('users').once('value');allUsers=us.val()||{};const vs=await db.ref('videos').once('value');allVideos=vs.val()?Object.entries(vs.val()).map(([k,v])=>({id:k,...v})):[];}
    async function loadProfile(){
        const u=allUsers[profileUserId];if(!u){document.getElementById('content').innerHTML='<div style="text-align:center;padding:60px;opacity:0.5">❌ المستخدم غير موجود</div>';return;}
        document.getElementById('profileCover').style.background=u.coverColor||COVER_COLORS[0];
        document.getElementById('avatarImg').src=u.avatarUrl||(DICEBEAR_URL+'?seed='+profileUserId);
        document.getElementById('nameDisplay').innerText='@'+(u.username||'مستخدم');
        if(u.isVerified)document.getElementById('verifiedBadge').style.display='inline-flex';else document.getElementById('verifiedBadge').style.display='none';
        if(u.banned)document.getElementById('bannedBadge').style.display='inline';else document.getElementById('bannedBadge').style.display='none';
        document.getElementById('bioDisplay').innerText=u.bio||'🌸 مرحباً! أنا جديد في Rose Sphere';
        if(u.lastSeen){const d=new Date(u.lastSeen),now=Date.now(),diff=(now-u.lastSeen)/1000;let txt='';if(diff<60)txt='🟢 متصل الآن';else if(diff<3600)txt='🟡 آخر ظهور قبل '+Math.floor(diff/60)+' دقيقة';else if(diff<86400)txt='🟠 آخر ظهور قبل '+Math.floor(diff/3600)+' ساعة';else txt='🔴 آخر ظهور '+d.toLocaleDateString('ar-SA');document.getElementById('lastSeen').innerText=txt;}
        const locEl=document.getElementById('locationDisplay');if(u.location){locEl.style.display='flex';locEl.querySelector('span').innerText=u.location;}else locEl.style.display='none';
        const webEl=document.getElementById('websiteDisplay');if(u.website){webEl.style.display='flex';const link=webEl.querySelector('a');link.href=u.website.startsWith('http')?u.website:'https://'+u.website;link.innerText=u.website.replace(/^https?:\/\//,'');}else webEl.style.display='none';
        const d=new Date(u.createdAt||Date.now());document.getElementById('joinedDate').innerText=d.toLocaleDateString('ar-SA',{year:'numeric',month:'long',day:'numeric'});
        const userVideos=allVideos.filter(v=>v.sender===profileUserId);
        document.getElementById('statPosts').querySelector('.stat-number').innerText=userVideos.length;
        document.getElementById('statFollowers').querySelector('.stat-number').innerText=Object.keys(u.followers||{}).length;
        document.getElementById('statFollowing').querySelector('.stat-number').innerText=Object.keys(u.following||{}).length;
        document.getElementById('statLikes').querySelector('.stat-number').innerText=userVideos.reduce((s,v)=>s+(v.likes||0),0);
        document.getElementById('statFollowers').onclick=()=>showUserList('متابعون',u.followers||{});
        document.getElementById('statFollowing').onclick=()=>showUserList('يتابع',u.following||{});
        const actionsBar=document.getElementById('actionsBar'),editCoverBtn=document.getElementById('editCoverBtn'),avatarDisplay=document.getElementById('avatarDisplay');
        if(isOwnProfile){actionsBar.innerHTML='<button class="btn btn-primary" onclick="openEditProfileModal()"><i class="fas fa-edit"></i> تعديل الملف</button><button class="btn btn-outline" onclick="shareProfile()"><i class="fas fa-share"></i> مشاركة</button><button class="btn btn-outline" onclick="auth.signOut();window.location.href=\'auth.html\'"><i class="fas fa-sign-out-alt"></i> خروج</button>';editCoverBtn.style.display='block';avatarDisplay.onclick=()=>document.getElementById('avatarInput').click();}else{const isFollowing=currentUserData?.following&&currentUserData.following[profileUserId];actionsBar.innerHTML=(isFollowing?'<button class="btn btn-primary" onclick="toggleFollowBtn()"><i class="fas fa-check"></i> متابع</button><button class="btn btn-outline" onclick="goToChat()"><i class="fas fa-comment"></i> مراسلة</button>':'<button class="btn btn-primary" onclick="toggleFollowBtn()"><i class="fas fa-plus"></i> متابعة</button>')+'<button class="btn btn-outline" onclick="shareProfile()"><i class="fas fa-share"></i> مشاركة</button>';editCoverBtn.style.display='none';avatarDisplay.style.cursor='default';avatarDisplay.onclick=null;}
        renderVideoGrid('videosGrid',userVideos);renderVideoGrid('likedGrid',allVideos.filter(v=>v.likedBy&&v.likedBy[profileUserId]));
    }
    function renderVideoGrid(gridId,videos){const grid=document.getElementById(gridId);if(!videos.length){grid.innerHTML='<div style="text-align:center;opacity:0.5;padding:40px;grid-column:1/-1"><i class="fas fa-video" style="font-size:36px;display:block;margin-bottom:8px;opacity:0.3"></i>لا توجد منشورات</div>';return;}grid.innerHTML=videos.map(v=>'<div class="thumb" onclick="window.open(\''+v.url+'\',\'_blank\')">'+(v.thumbnail?'<img src="'+v.thumbnail+'" loading="lazy">':'')+'<span style="position:absolute;z-index:1;font-size:22px;opacity:0;transition:opacity 0.3s"><i class="fas fa-play"></i></span>'+(isAdmin?'<div class="delete-btn" onclick="event.stopPropagation();deleteVideo(\''+v.id+'\')"><i class="fas fa-trash"></i></div>':'')+'</div>').join('');}
    function switchProfileTab(tab,el){document.querySelectorAll('.profile-tab').forEach(t=>t.classList.remove('active'));document.querySelectorAll('.tab-content').forEach(t=>t.classList.remove('active'));if(el)el.classList.add('active');document.getElementById(tab==='videos'?'tabVideos':'tabLiked').classList.add('active');}
    window.openEditProfileModal=function(){const u=allUsers[profileUserId];const oid='modal_'+Date.now();const html='<div class="modal-overlay" id="'+oid+'"><div class="modal-header"><h3><i class="fas fa-edit"></i> تعديل الملف الشخصي</h3><button class="btn-close" onclick="document.getElementById(\''+oid+'\').remove()" style="background:rgba(236,72,153,0.1);border:1px solid var(--border);color:#fff;width:36px;height:36px;border-radius:50%;cursor:pointer;font-size:18px"><i class="fas fa-times"></i></button></div><div class="modal-body"><div class="edit-form-group"><label>👤 اسم المستخدم</label><input type="text" id="editName_'+oid+'" value="'+(u?.username||'')+'"></div><div class="edit-form-group"><label>📝 السيرة الذاتية</label><textarea id="editBio_'+oid+'">'+(u?.bio||'')+'</textarea></div><div class="edit-form-group"><label>📍 الموقع</label><input type="text" id="editLoc_'+oid+'" value="'+(u?.location||'')+'"></div><div class="edit-form-group"><label>🌐 الموقع الإلكتروني</label><input type="text" id="editWeb_'+oid+'" value="'+(u?.website||'')+'"></div><button class="btn btn-primary" style="width:100%" onclick="saveProfile(\''+oid+'\')"><i class="fas fa-save"></i> حفظ التغييرات</button></div></div>';document.body.insertAdjacentHTML('beforeend',html);
        window.saveProfile=async function(id){const name=document.getElementById('editName_'+id).value.trim(),bio=document.getElementById('editBio_'+id).value.trim(),loc=document.getElementById('editLoc_'+id).value.trim(),web=document.getElementById('editWeb_'+id).value.trim();if(!name)return alert('الاسم مطلوب');await db.ref('users/'+profileUserId).update({username:name,bio:bio,location:loc,website:web});document.getElementById(id).remove();await loadAllData();await loadProfile();};};
    window.toggleFollowBtn=async function(){if(!currentUser||currentUser.uid===profileUserId)return;const userRef=db.ref('users/'+currentUser.uid+'/following/'+profileUserId),targetRef=db.ref('users/'+profileUserId+'/followers/'+currentUser.uid);const snap=await userRef.get();if(snap.exists()){await userRef.remove();await targetRef.remove();}else{await userRef.set(true);await targetRef.set(true);db.ref('notifications/'+profileUserId).push({from:currentUserData?.username||'مستخدم',msg:'بدأ بمتابعتك 🌹',type:'follow',timestamp:Date.now(),read:false});}await loadAllData();await loadProfile();};
    window.shareProfile=function(){navigator.clipboard.writeText(window.location.href);alert('✅ تم نسخ رابط الملف الشخصي');};
    window.goToChat=function(){window.location.href='chat.html?uid='+profileUserId;};
    window.goBack=function(){window.location.href='index.html';};
    async function showUserList(title,usersObj){const userIds=Object.keys(usersObj);let html='<div class="modal-overlay" id="userListModal"><div class="modal-header"><h3>'+title+' ('+userIds.length+')</h3><button class="btn-close" onclick="document.getElementById(\'userListModal\').remove()" style="background:rgba(236,72,153,0.1);border:1px solid var(--border);color:#fff;width:36px;height:36px;border-radius:50%;cursor:pointer;font-size:18px"><i class="fas fa-times"></i></button></div><div class="modal-body">';if(!userIds.length)html+='<div style="text-align:center;opacity:0.5;padding:40px">لا يوجد</div>';else for(const uid of userIds){const user=allUsers[uid];if(!user)continue;html+='<div class="user-list-item" onclick="window.location.href=\'profile.html?uid='+uid+'\';document.getElementById(\'userListModal\').remove()"><div class="user-list-avatar"><img src="'+(user.avatarUrl||(DICEBEAR_URL+'?seed='+uid))+'" alt="avatar"></div><div class="user-list-info"><div class="user-list-name">@'+(user.username||'مستخدم')+(user.isVerified?' <span class="verify-badge"><i class="fas fa-check"></i></span>':'')+'</div><div style="font-size:12px;opacity:0.5;margin-top:2px">'+(user.bio?user.bio.substring(0,50):'')+'</div></div><i class="fas fa-chevron-left" style="opacity:0.3"></i></div>';}html+='</div></div>';document.body.insertAdjacentHTML('beforeend',html);}
    async function uploadAvatar(input){const file=input.files[0];if(!file)return;const fd=new FormData();fd.append('file',file);fd.append('upload_preset',UPLOAD_PRESET);try{const res=await fetch('https://api.cloudinary.com/v1_1/'+CLOUD_NAME+'/image/upload',{method:'POST',body:fd});const data=await res.json();if(data.secure_url){await db.ref('users/'+profileUserId).update({avatarUrl:data.secure_url,hasCustomAvatar:true});document.getElementById('avatarImg').src=data.secure_url;}}catch(e){alert('❌ فشل رفع الصورة');}}
    document.getElementById('editCoverBtn').addEventListener('click',async function(){const idx=prompt('اختر غلاف (1-'+COVER_COLORS.length+'):');if(idx&&idx>=1&&idx<=COVER_COLORS.length){const nc=COVER_COLORS[idx-1];await db.ref('users/'+profileUserId+'/coverColor').set(nc);document.getElementById('profileCover').style.background=nc;}});
    // Admin Panel
    async function loadAdminPanel(){const us=allUsers,vs={};allVideos.forEach(v=>vs[v.id]=v);const tl=Object.values(vs).reduce((s,v)=>s+(v.likes||0),0),vc=Object.values(us).filter(u=>u.isVerified).length,bc=Object.values(us).filter(u=>u.banned).length,oc=Object.values(us).filter(u=>u.lastSeen&&(Date.now()-u.lastSeen)<300000).length;
        document.getElementById('adminSection').innerHTML='<div class="admin-section"><div class="admin-title"><i class="fas fa-shield-alt"></i> لوحة تحكم الأدمن 👑</div><div class="admin-stats-grid"><div class="admin-stat-card"><div class="admin-stat-num">'+Object.keys(us).length+'</div><div class="admin-stat-lbl">👥 مستخدمين</div></div><div class="admin-stat-card"><div class="admin-stat-num">'+Object.keys(vs).length+'</div><div class="admin-stat-lbl">🎬 فيديوهات</div></div><div class="admin-stat-card"><div class="admin-stat-num">'+tl+'</div><div class="admin-stat-lbl">❤️ إعجابات</div></div><div class="admin-stat-card"><div class="admin-stat-num">'+oc+'</div><div class="admin-stat-lbl">🟢 متصلين</div></div></div><div class="admin-stats-grid" style="grid-template-columns:repeat(3,1fr);margin-bottom:12px"><div class="admin-stat-card"><div class="admin-stat-num" style="color:#34d399">'+vc+'</div><div class="admin-stat-lbl">✅ موثقين</div></div><div class="admin-stat-card"><div class="admin-stat-num" style="color:#f87171">'+bc+'</div><div class="admin-stat-lbl">🚫 محظورين</div></div><div class="admin-stat-card"><button class="admin-btn-sm btn-broadcast" onclick="broadcastMessage()" style="margin-top:8px"><i class="fas fa-bullhorn"></i> إشعار جماعي</button></div></div><div style="font-size:14px;font-weight:600;color:#f472b6;margin:16px 0 12px"><i class="fas fa-users"></i> إدارة المستخدمين</div><div id="adminUsersList" style="max-height:350px;overflow-y:auto">'+Object.entries(us).slice(0,20).map(([id,u])=>'<div class="admin-user-item"><div style="display:flex;align-items:center;gap:8px"><div style="width:36px;height:36px;border-radius:50%;overflow:hidden;flex-shrink:0"><img src="'+(u.avatarUrl||(DICEBEAR_URL+'?seed='+id))+'" style="width:100%;height:100%;object-fit:cover" alt=""></div><div><div style="font-weight:600;font-size:13px">@'+(u.username||'مستخدم')+' '+(u.isVerified?'<span class="verify-badge" style="width:16px;height:16px;font-size:8px"><i class="fas fa-check"></i></span>':'')+' '+(u.banned?'<span style="font-size:10px;background:rgba(239,68,68,0.3);color:#f87171;padding:2px 8px;border-radius:10px">🚫 محظور</span>':'')+'</div><div style="font-size:10px;opacity:0.5">'+(u.email||'')+'</div></div></div><div style="display:flex;gap:4px"><button class="admin-btn-sm '+(u.isVerified?'btn-unban-user':'btn-verify-user')+'" onclick="toggleVerifyUser(\''+id+'\')">'+(u.isVerified?'إلغاء':'✅ توثيق')+'</button><button class="admin-btn-sm '+(u.banned?'btn-unban-user':'btn-ban-user')+'" onclick="toggleBanUser(\''+id+'\')">'+(u.banned?'🔓 فك':'🚫 حظر')+'</button></div></div>').join('')+'</div></div>';
        window.toggleVerifyUser=async function(uid){if(confirm('تأكيد؟')){const r=await db.ref('users/'+uid).once('value');const d=r.val();await db.ref('users/'+uid).update({isVerified:!d.isVerified,verifiedAt:!d.isVerified?Date.now():null,verifiedBy:!d.isVerified?currentUser.email:null});db.ref('notifications/'+uid).push({from:'الإدارة',msg:(!d.isVerified?'🌹 تم توثيق حسابك!':'تم إلغاء توثيق حسابك'),type:'system',timestamp:Date.now(),read:false});await loadAllData();await loadProfile();loadAdminPanel();}};
        window.toggleBanUser=async function(uid){const r=await db.ref('users/'+uid).once('value');const d=r.val();const reason=!d.banned?prompt('سبب الحظر:'):'';if(!d.banned&&!reason)return;if(confirm('تأكيد؟')){await db.ref('users/'+uid).update({banned:!d.banned,banReason:!d.banned?reason:''});if(!d.banned)db.ref('notifications/'+uid).push({from:'الإدارة',msg:'🚫 تم حظر حسابك. السبب: '+reason,type:'system',timestamp:Date.now(),read:false});await loadAllData();await loadProfile();loadAdminPanel();}};
        window.deleteVideo=async function(vid){if(confirm('حذف الفيديو؟')){const snap=await db.ref('videos/'+vid).get();const v=snap.val();if(v&&v.sender)await db.ref('users/'+v.sender+'/posts/'+vid).remove();await db.ref('videos/'+vid).remove();await loadAllData();await loadProfile();loadAdminPanel();}};
        window.broadcastMessage=function(){const msg=prompt('📢 رسالة الإشعار الجماعي:');if(msg){if(confirm('إرسال: "'+msg+'" للجميع؟')){const promises=Object.keys(us).map(uid=>db.ref('notifications/'+uid).push({from:'الإدارة 👑',msg:msg,type:'broadcast',timestamp:Date.now(),read:false}));Promise.all(promises).then(()=>alert('✅ تم الإرسال!'));}}};}
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 🌹 5. upload.html - رفع فيديو احترافي
# ═══════════════════════════════════════════════════════════

def build_upload():
    return r"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>🌹 ROSE SPHERE | رفع</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root{--glass:rgba(255,255,255,0.03);--border:rgba(236,72,153,0.15);--accent:#ec4899;--accent2:#f472b6;--bg:#1a0a14}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:#fff;min-height:100vh;overflow-y:auto}
        .header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);background:rgba(26,10,20,0.8);position:sticky;top:0;z-index:10;backdrop-filter:blur(20px)}
        .btn-back{background:rgba(236,72,153,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px;transition:all 0.3s}
        .btn-back:hover{background:rgba(236,72,153,0.2)}
        .container{max-width:500px;margin:0 auto;padding:20px}
        .dropzone{border:2px dashed rgba(236,72,153,0.3);border-radius:20px;padding:60px 20px;text-align:center;cursor:pointer;background:var(--glass);margin-bottom:20px;transition:all 0.3s;position:relative}
        .dropzone:hover,.dropzone.dragover{border-color:var(--accent);background:rgba(236,72,153,0.05)}
        .dropzone i{font-size:56px;color:var(--accent);margin-bottom:12px;display:block}
        .dropzone video{width:100%;max-height:300px;object-fit:contain;margin-top:12px;border-radius:12px;display:none}
        .form-card{background:var(--glass);border:1px solid var(--border);border-radius:20px;padding:20px}
        .form-card label{display:block;font-size:13px;opacity:0.7;margin-bottom:6px;margin-top:12px}
        .form-card textarea,.form-card input{width:100%;padding:14px 16px;border-radius:16px;background:rgba(255,255,255,0.05);border:1px solid var(--border);color:#fff;font-size:14px;outline:none;resize:none;font-family:'Segoe UI',sans-serif;transition:border-color 0.3s}
        .form-card textarea:focus,.form-card input:focus{border-color:var(--accent)}
        .form-card textarea{min-height:80px}
        .progress-wrap{display:none;margin:16px 0}
        .progress-bar{background:rgba(255,255,255,0.1);border-radius:30px;height:8px;overflow:hidden}
        .progress-fill{background:linear-gradient(90deg,var(--accent),var(--accent2));height:100%;border-radius:30px;width:0%;transition:width 0.3s}
        .progress-text{text-align:center;font-size:12px;margin-top:6px;color:var(--accent)}
        .btn-upload{width:100%;padding:14px;background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;border-radius:30px;color:#fff;font-weight:700;font-size:15px;cursor:pointer;margin-top:16px;box-shadow:0 10px 25px rgba(236,72,153,0.4);transition:all 0.3s}
        .btn-upload:hover{transform:translateY(-2px);box-shadow:0 15px 35px rgba(236,72,153,0.6)}
        .btn-upload:disabled{opacity:0.5;transform:none;cursor:not-allowed}
        .status{text-align:center;margin-top:12px;font-size:13px;min-height:20px}
        .status.success{color:#4ade80}.status.error{color:#f87171}
    </style>
</head>
<body>
<div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2>📤 رفع فيديو جديد</h2></div>
<div class="container">
    <div class="dropzone" id="dropZone" onclick="document.getElementById('videoFile').click()">
        <i class="fas fa-cloud-upload-alt"></i>
        <p style="font-size:16px;font-weight:600">اسحب وأفلت الفيديو هنا</p>
        <span style="font-size:11px;opacity:0.5">أو اضغط للاختيار - MP4 حتى 100MB</span>
        <video id="preview" controls playsinline></video>
    </div>
    <input type="file" id="videoFile" accept="video/*" style="display:none" onchange="onFilePick(this)">
    <div class="form-card">
        <label>🎬 وصف الفيديو</label><textarea id="vidDesc" placeholder="اكتب وصفاً جذاباً... #هاشتاقات"></textarea>
        <label>🎵 الموسيقى</label><input type="text" id="vidMusic" placeholder="Original Sound">
        <div class="progress-wrap" id="progressWrap"><div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div><div class="progress-text" id="progressText">0%</div></div>
        <button class="btn-upload" id="uploadBtn" onclick="uploadVideo()">🌹 رفع الفيديو</button>
        <div class="status" id="status"></div>
    </div>
</div>
<script src="firebase-config.js"></script>
<script>
    let currentUser=null,currentUserData=null,selectedFile=null;
    auth.onAuthStateChanged(async u=>{if(!u){window.location.href='auth.html';return}currentUser=u;const snap=await db.ref('users/'+u.uid).get();if(snap.exists())currentUserData={uid:u.uid,...snap.val()};});
    const dropZone=document.getElementById('dropZone');
    dropZone.addEventListener('dragover',e=>{e.preventDefault();dropZone.classList.add('dragover')});
    dropZone.addEventListener('dragleave',()=>dropZone.classList.remove('dragover'));
    dropZone.addEventListener('drop',e=>{e.preventDefault();dropZone.classList.remove('dragover');const file=e.dataTransfer.files[0];if(file)handleFile(file)});
    function onFilePick(inp){const f=inp.files[0];if(f)handleFile(f);}
    function handleFile(f){
        if(!f.type.startsWith('video/')){alert('❌ اختر فيديو صحيح');return}if(f.size>100*1024*1024){alert('❌ أقل من 100MB');return}
        selectedFile=f;const r=new FileReader();r.onload=e=>{const v=document.getElementById('preview');v.src=e.target.result;v.style.display='block';document.querySelector('.dropzone i').style.display='none';document.querySelector('.dropzone p').style.display='none';document.querySelector('.dropzone span').style.display='none'};r.readAsDataURL(f);
    }
    async function uploadVideo(){
        if(!selectedFile){alert('❌ اختر فيديو');return}if(!currentUser||!currentUserData){alert('❌ انتظر تحميل البيانات');return}
        const desc=document.getElementById('vidDesc').value||'',music=document.getElementById('vidMusic').value||'Original Sound';
        const pw=document.getElementById('progressWrap'),pf=document.getElementById('progressFill'),pt=document.getElementById('progressText'),st=document.getElementById('status'),btn=document.getElementById('uploadBtn');
        pw.style.display='block';pf.style.width='0%';pt.innerText='0%';st.innerHTML='';st.className='status';btn.disabled=true;btn.innerText='⏳ جاري الرفع...';
        const fd=new FormData();fd.append('file',selectedFile);fd.append('upload_preset',UPLOAD_PRESET);
        try{const res=await fetch('https://api.cloudinary.com/v1_1/'+CLOUD_NAME+'/video/upload',{method:'POST',body:fd});const r=await res.json();
            if(r.secure_url){pf.style.width='100%';pt.innerText='100%';const videoRef=db.ref('videos/').push();await videoRef.set({url:r.secure_url,thumbnail:r.secure_url.replace(/\.\w+$/,'.jpg'),description:desc,music:music,sender:currentUser.uid,senderName:currentUserData.username||'مستخدم',likes:0,likedBy:{},comments:{},timestamp:Date.now()});await db.ref('users/'+currentUser.uid+'/posts/'+videoRef.key).set(true);st.innerHTML='✅ تم الرفع بنجاح! جاري التوجيه...';st.className='status success';setTimeout(()=>window.location.href='profile.html',1500);}else throw new Error(r.error?.message||'فشل الرفع');}
        catch(e){st.innerHTML='❌ فشل: '+(e.message||'خطأ');st.className='status error';btn.disabled=false;btn.innerText='🌹 رفع الفيديو';pw.style.display='none';}
    }
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 🌹 6. chat.html - دردشة + صور + نسخ + آخر ظهور
# ═══════════════════════════════════════════════════════════

def build_chat():
    return r"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>🌹 ROSE SPHERE | دردشة</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root{--glass:rgba(255,255,255,0.03);--border:rgba(236,72,153,0.15);--accent:#ec4899;--accent2:#f472b6;--bg:#1a0a14}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:#fff;height:100vh;display:flex;flex-direction:column}
        .header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);flex-shrink:0}
        .btn-back{background:rgba(236,72,153,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px}
        .chat-avatar{width:40px;height:40px;border-radius:50%;overflow:hidden;flex-shrink:0}
        .chat-avatar img{width:100%;height:100%;object-fit:cover}
        .online-status{font-size:11px;opacity:0.6}.online-status.online{color:#4ade80}
        .msgs{flex:1;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:8px}
        .bubble{max-width:80%;padding:10px 16px;border-radius:20px;word-break:break-word;font-size:14px;line-height:1.5;position:relative}
        .bubble.sent{background:linear-gradient(135deg,var(--accent),var(--accent2));align-self:flex-end}
        .bubble.received{background:rgba(255,255,255,0.06);align-self:flex-start}
        .bubble .time{font-size:9px;opacity:0.5;margin-top:4px}
        .bubble .copy-btn{position:absolute;top:4px;left:4px;background:rgba(0,0,0,0.4);width:20px;height:20px;border-radius:50%;display:none;align-items:center;justify-content:center;cursor:pointer;font-size:8px;border:none;color:#fff}
        .bubble:hover .copy-btn{display:flex}
        .bubble img{border-radius:12px;max-width:200px;cursor:pointer;display:block}
        .input-bar{display:flex;gap:10px;padding:12px;background:rgba(26,10,20,0.9);border-top:1px solid var(--border);flex-shrink:0;align-items:center}
        .input-bar input{flex:1;padding:12px 16px;border-radius:30px;background:rgba(255,255,255,0.05);border:1px solid var(--border);color:#fff;font-size:14px;outline:none}
        .btn-send{width:42px;height:42px;background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;border-radius:50%;color:#fff;cursor:pointer;font-size:18px;transition:transform 0.2s;flex-shrink:0}
        .btn-send:active{transform:scale(0.9)}
        .btn-image{width:42px;height:42px;background:rgba(255,255,255,0.05);border:1px solid var(--border);border-radius:50%;color:#fff;cursor:pointer;font-size:18px;flex-shrink:0;display:flex;align-items:center;justify-content:center;transition:all 0.2s}
        .btn-image:hover{background:rgba(236,72,153,0.2)}
        .conv-item{display:flex;align-items:center;gap:12px;padding:14px;border-bottom:1px solid var(--border);cursor:pointer;transition:background 0.2s}
        .conv-item:hover{background:rgba(236,72,153,0.05)}
        .spinner{width:32px;height:32px;border:3px solid rgba(236,72,153,0.2);border-top-color:var(--accent);border-radius:50%;animation:spin 0.7s linear infinite;margin:30px auto}
        @keyframes spin{to{transform:rotate(360deg)}}
        .toast{position:fixed;bottom:100px;left:50%;transform:translateX(-50%);background:rgba(26,10,20,0.9);padding:10px 22px;border-radius:50px;z-index:1000;opacity:0;transition:opacity 0.3s;pointer-events:none;border:1px solid var(--border);font-size:13px}
        .toast.show{opacity:1}
    </style>
</head>
<body>
<div id="loader" style="flex:1;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:12px"><div class="spinner"></div><span>🌹 تحميل...</span></div>
<div id="convView" style="display:none;flex:1;flex-direction:column;overflow:hidden"><div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2>💬 المحادثات</h2></div><div id="convList" style="flex:1;overflow-y:auto"></div></div>
<div id="chatView" style="display:none;flex:1;flex-direction:column;overflow:hidden"><div class="header"><button class="btn-back" onclick="showConvs()"><i class="fas fa-arrow-right"></i></button><div class="chat-avatar" id="chatAvatar"></div><div style="flex:1"><h3 id="chatName">محادثة</h3><div class="online-status" id="onlineStatus"></div></div></div><div class="msgs" id="msgsList"></div><div class="input-bar"><button class="btn-image" onclick="document.getElementById('imageInput').click()"><i class="fas fa-image"></i></button><input type="text" id="msgInput" placeholder="اكتب رسالة..." onkeydown="if(event.key==='Enter')sendMsg()"><input type="file" id="imageInput" accept="image/*" style="display:none" onchange="sendImage(this)"><button class="btn-send" onclick="sendMsg()"><i class="fas fa-paper-plane"></i></button></div></div>
<div id="toast" class="toast">✅ تم</div>
<script src="firebase-config.js"></script>
<script>
    let currentUser=null,currentUserData=null,allUsers={},chatUserId=null,lastSeenInterval=null;
    auth.onAuthStateChanged(async u=>{if(!u){window.location.href='auth.html';return}currentUser=u;const snap=await db.ref('users/'+u.uid).get();if(snap.exists())currentUserData={uid:u.uid,...snap.val()};const us=await db.ref('users').once('value');allUsers=us.val()||{};document.getElementById('loader').style.display='none';const params=new URLSearchParams(window.location.search);const targetUid=params.get('uid');if(targetUid){showConvs();openChat(targetUid);}else showConvs();});
    function showConvs(){document.getElementById('chatView').style.display='none';document.getElementById('convView').style.display='flex';chatUserId=null;if(lastSeenInterval)clearInterval(lastSeenInterval);loadConvs();}
    async function loadConvs(){const cl=document.getElementById('convList');cl.innerHTML='';const snap=await db.ref('private_messages').once('value');const all=snap.val()||{};const found=new Set();Object.keys(all).forEach(cid=>{const[u1,u2]=cid.split('_');const other=u1===currentUser.uid?u2:u2===currentUser.uid?u1:null;if(other&&!found.has(other)&&allUsers[other])found.add(other)});if(!found.size){cl.innerHTML='<div style="text-align:center;opacity:0.5;padding:40px">لا توجد محادثات</div>';return}const convsArr=[];found.forEach(uid=>{const lastMsg=all[[currentUser.uid,uid].sort().join('_')];const msgs=lastMsg?Object.values(lastMsg).sort((a,b)=>(b.timestamp||0)-(a.timestamp||0)):[];convsArr.push({uid,lastMsg:msgs.length?msgs[0]:null})});convsArr.sort((a,b)=>(b.lastMsg?.timestamp||0)-(a.lastMsg?.timestamp||0));convsArr.forEach(({uid,lastMsg})=>{const u=allUsers[uid];const d=document.createElement('div');d.className='conv-item';d.innerHTML='<div class="chat-avatar"><img src="'+(u?.avatarUrl||(DICEBEAR_URL+'?seed='+uid))+'" alt="avatar"></div><div style="flex:1"><div style="font-weight:600">@'+(u?.username||'?')+' '+(u?.isVerified?'<span class="verify-badge" style="width:14px;height:14px;font-size:7px"><i class="fas fa-check"></i></span>':'')+'</div>'+(lastMsg?'<div style="font-size:12px;opacity:0.5;margin-top:2px">'+(lastMsg.type==='image'?'📷 صورة':(lastMsg.text||'').substring(0,30))+'</div>':'')+'</div><i class="fas fa-chevron-left" style="opacity:0.3"></i>';d.onclick=()=>openChat(uid);cl.appendChild(d)});}
    function getChatId(){return[currentUser.uid,chatUserId].sort().join('_');}
    async function openChat(uid){chatUserId=uid;const u=allUsers[uid];document.getElementById('chatName').innerText='@'+(u?.username||'مستخدم');document.getElementById('chatAvatar').innerHTML='<img src="'+(u?.avatarUrl||(DICEBEAR_URL+'?seed='+uid))+'" alt="avatar">';updateOnlineStatus();if(lastSeenInterval)clearInterval(lastSeenInterval);lastSeenInterval=setInterval(updateOnlineStatus,30000);document.getElementById('convView').style.display='none';document.getElementById('chatView').style.display='flex';loadMsgs();document.getElementById('msgInput').focus();}
    function updateOnlineStatus(){const u=allUsers[chatUserId];if(!u)return;const el=document.getElementById('onlineStatus');const diff=u.lastSeen?(Date.now()-u.lastSeen)/1000:999999;if(diff<60){el.innerHTML='🟢 متصل الآن';el.className='online-status online';}else if(diff<3600){el.innerHTML='🟡 آخر ظهور قبل '+Math.floor(diff/60)+' دقيقة';el.className='online-status';}else if(diff<86400){el.innerHTML='🟠 آخر ظهور قبل '+Math.floor(diff/3600)+' ساعة';el.className='online-status';}else{el.innerHTML='🔴 آخر ظهور '+new Date(u.lastSeen).toLocaleDateString('ar-SA');el.className='online-status';}}
    async function loadMsgs(){const ml=document.getElementById('msgsList');ml.innerHTML='';if(!chatUserId)return;db.ref('private_messages/'+getChatId()).on('value',snap=>{const ms=snap.val()||{};ml.innerHTML='';Object.values(ms).sort((a,b)=>(a.timestamp||0)-(b.timestamp||0)).forEach(m=>{const sent=m.senderId===currentUser.uid;const d=document.createElement('div');d.className='bubble '+(sent?'sent':'received');if(m.type==='image'){d.innerHTML='<img src="'+m.imageUrl+'" style="max-width:200px;border-radius:12px;cursor:pointer" onclick="window.open(\''+m.imageUrl+'\')" loading="lazy"><div class="time">'+new Date(m.timestamp).toLocaleTimeString('ar-SA',{hour:'2-digit',minute:'2-digit'})+'</div>';}else{d.innerHTML=m.text+'<button class="copy-btn" onclick="copyMsg(\''+m.text.replace(/'/g,"\\'").replace(/"/g,'&quot;')+'\')"><i class="fas fa-copy"></i></button><div class="time">'+new Date(m.timestamp).toLocaleTimeString('ar-SA',{hour:'2-digit',minute:'2-digit'})+'</div>';}ml.appendChild(d)});ml.scrollTop=ml.scrollHeight});}
    window.copyMsg=function(text){navigator.clipboard.writeText(text);const toast=document.getElementById('toast');toast.innerHTML='✅ تم نسخ النص';toast.classList.add('show');setTimeout(()=>toast.classList.remove('show'),2000);};
    async function sendMsg(){const inp=document.getElementById('msgInput');const txt=inp.value.trim();if(!txt||!chatUserId)return;await db.ref('private_messages/'+getChatId()).push({senderId:currentUser.uid,text:txt,type:'text',timestamp:Date.now()});db.ref('notifications/'+chatUserId).push({from:currentUserData?.username||'مستخدم',msg:'💬 '+txt.substring(0,30),type:'message',timestamp:Date.now(),read:false});inp.value='';}
    async function sendImage(input){const file=input.files[0];if(!file||!chatUserId)return;const toast=document.getElementById('toast');toast.innerHTML='⏳ جاري رفع الصورة...';toast.classList.add('show');const fd=new FormData();fd.append('file',file);fd.append('upload_preset',UPLOAD_PRESET);try{const res=await fetch('https://api.cloudinary.com/v1_1/'+CLOUD_NAME+'/image/upload',{method:'POST',body:fd});const data=await res.json();if(data.secure_url){await db.ref('private_messages/'+getChatId()).push({senderId:currentUser.uid,imageUrl:data.secure_url,type:'image',timestamp:Date.now()});db.ref('notifications/'+chatUserId).push({from:currentUserData?.username||'مستخدم',msg:'📷 أرسل لك صورة',type:'message',timestamp:Date.now(),read:false});toast.innerHTML='✅ تم إرسال الصورة';}else{toast.innerHTML='❌ فشل رفع الصورة';}}catch(e){toast.innerHTML='❌ خطأ';}setTimeout(()=>toast.classList.remove('show'),2000);input.value='';}
</script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 🌹 7, 8, 9 - explore, notifications, settings
# ═══════════════════════════════════════════════════════════

def build_explore():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover"><title>🌹 ROSE SPHERE | استكشاف</title><script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script><script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script><script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script><link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet"><style>:root{--border:rgba(236,72,153,0.15);--accent:#ec4899;--bg:#1a0a14}*{margin:0;padding:0;box-sizing:border-box}body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:#fff;min-height:100vh;overflow-y:auto}.header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(26,10,20,0.8);backdrop-filter:blur(20px);z-index:10}.btn-back{background:rgba(236,72,153,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px}.search-bar{flex:1;display:flex;align-items:center;background:rgba(255,255,255,0.05);border:1px solid var(--border);border-radius:30px;padding:8px 16px;gap:8px}.search-bar input{flex:1;background:none;border:none;color:#fff;font-size:14px;outline:none}.section-title{padding:16px;font-weight:700;font-size:16px;opacity:0.7}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:2px}.thumb{aspect-ratio:9/16;background:rgba(255,255,255,0.03);display:flex;align-items:center;justify-content:center;cursor:pointer;position:relative;overflow:hidden;transition:transform 0.2s}.thumb:hover{transform:scale(1.03);z-index:1}.thumb img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}.thumb .likes-badge{position:absolute;bottom:4px;left:4px;font-size:10px;background:rgba(0,0,0,0.6);padding:2px 6px;border-radius:10px}.user-card{display:flex;align-items:center;gap:12px;padding:14px 16px;border-bottom:1px solid var(--border);cursor:pointer;transition:background 0.2s}.user-card:hover{background:rgba(236,72,153,0.05)}.user-avatar{width:50px;height:50px;border-radius:50%;overflow:hidden;flex-shrink:0}.user-avatar img{width:100%;height:100%;object-fit:cover}.verify-badge{display:inline-flex;align-items:center;justify-content:center;width:14px;height:14px;border-radius:50%;background:linear-gradient(135deg,#ec4899,#f472b6);font-size:7px;color:#fff;margin:0 3px;vertical-align:middle}.spinner{width:32px;height:32px;border:3px solid rgba(236,72,153,0.2);border-top-color:var(--accent);border-radius:50%;animation:spin 0.7s linear infinite;margin:30px auto}@keyframes spin{to{transform:rotate(360deg)}}</style></head>
<body><div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><div class="search-bar"><i class="fas fa-search"></i><input type="text" id="searchInput" placeholder="ابحث عن مستخدمين..." onkeyup="doSearch()"></div></div><div id="searchResults" style="display:none"></div><div id="mainContent"><div class="section-title">🔥 الأكثر شيوعاً</div><div class="grid" id="exploreGrid"><div class="spinner" style="grid-column:1/-1"></div></div><div class="section-title">👥 مستخدمون مميزون</div><div id="featuredUsers"></div></div>
<script src="firebase-config.js"></script><script>let cu=null,av=[],au={};auth.onAuthStateChanged(async u=>{if(!u){window.location.href='auth.html';return}cu=u;await ld()});async function ld(){const us=await db.ref('users').once('value');au=us.val()||{};const vs=await db.ref('videos').once('value');av=vs.val()?Object.entries(vs.val()).map(([k,v])=>({id:k,...v})).sort((a,b)=>(b.likes||0)-(a.likes||0)):[];document.getElementById('exploreGrid').innerHTML=av.slice(0,30).map(v=>'<div class="thumb" onclick="window.open(\''+v.url+'\',\'_blank\')">'+(v.thumbnail?'<img src="'+v.thumbnail+'" loading="lazy">':'')+'<span class="likes-badge">❤️ '+(v.likes||0)+'</span></div>').join('')||'<div style="text-align:center;opacity:0.5;padding:40px;grid-column:1/-1">لا توجد فيديوهات</div>';const ua=Object.entries(au).filter(([id,u])=>!u.banned&&Object.keys(u.followers||{}).length>0).sort((a,b)=>(Object.keys(b[1].followers||{}).length)-(Object.keys(a[1].followers||{}).length)).slice(0,10);document.getElementById('featuredUsers').innerHTML=ua.map(([id,u])=>'<div class="user-card" onclick="window.location.href=\'profile.html?uid='+id+'\'"><div class="user-avatar"><img src="'+(u.avatarUrl||(DICEBEAR_URL+'?seed='+id))+'" alt="avatar"></div><div style="flex:1"><div style="font-weight:600">@'+(u.username||'مستخدم')+' '+(u.isVerified?'<span class="verify-badge"><i class="fas fa-check"></i></span>':'')+'</div><div style="font-size:12px;opacity:0.5">'+Object.keys(u.followers||{}).length+' متابع</div></div><i class="fas fa-chevron-left" style="opacity:0.3"></i></div>').join('')}function doSearch(){const q=document.getElementById('searchInput').value.toLowerCase();if(!q){document.getElementById('searchResults').style.display='none';document.getElementById('mainContent').style.display='block';return}document.getElementById('mainContent').style.display='none';document.getElementById('searchResults').style.display='block';const mu=Object.entries(au).filter(([id,u])=>u.username?.toLowerCase().includes(q)||u.bio?.toLowerCase().includes(q));document.getElementById('searchResults').innerHTML=mu.length?mu.map(([id,u])=>'<div class="user-card" onclick="window.location.href=\'profile.html?uid='+id+'\'"><div class="user-avatar"><img src="'+(u.avatarUrl||(DICEBEAR_URL+'?seed='+id))+'" alt="avatar"></div><div style="flex:1"><div style="font-weight:600">@'+(u.username||'مستخدم')+' '+(u.isVerified?'<span class="verify-badge"><i class="fas fa-check"></i></span>':'')+'</div><div style="font-size:12px;opacity:0.5">'+(u.bio?u.bio.substring(0,50):'')+'</div></div></div>').join(''):'<div style="text-align:center;opacity:0.5;padding:40px">لا توجد نتائج</div>'}</script>
</body></html>"""

def build_notifications():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover"><title>🌹 ROSE SPHERE | إشعارات</title><script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script><script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script><script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script><link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet"><style>:root{--border:rgba(236,72,153,0.15);--accent:#ec4899;--bg:#1a0a14}*{margin:0;padding:0;box-sizing:border-box}body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:#fff;min-height:100vh;overflow-y:auto}.header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(26,10,20,0.8);backdrop-filter:blur(20px);z-index:10}.btn-back{background:rgba(236,72,153,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px}.notif-item{display:flex;gap:12px;padding:14px 16px;border-bottom:1px solid var(--border);align-items:center;transition:background 0.2s}.notif-item:hover{background:rgba(236,72,153,0.05)}.notif-item.unread{background:rgba(236,72,153,0.08)}.notif-icon{width:42px;height:42px;border-radius:50%;background:rgba(236,72,153,0.15);display:flex;align-items:center;justify-content:center;font-size:18px;color:var(--accent);flex-shrink:0}.notif-content{flex:1}.notif-msg{font-size:14px;line-height:1.4}.notif-time{font-size:11px;opacity:0.4;margin-top:4px}.spinner{width:32px;height:32px;border:3px solid rgba(236,72,153,0.2);border-top-color:var(--accent);border-radius:50%;animation:spin 0.7s linear infinite;margin:30px auto}@keyframes spin{to{transform:rotate(360deg)}}</style></head>
<body><div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2>🔔 الإشعارات</h2></div><div id="notifsList"><div class="spinner"></div></div>
<script src="firebase-config.js"></script><script>let cu=null;auth.onAuthStateChanged(u=>{if(!u){window.location.href='auth.html';return}cu=u;loadNotifs()});function loadNotifs(){db.ref('notifications/'+cu.uid).on('value',snap=>{const ns=snap.val()||{};const c=document.getElementById('notifsList');const items=Object.entries(ns).reverse();if(!items.length){c.innerHTML='<div style="text-align:center;opacity:0.5;padding:60px"><i class="fas fa-bell" style="font-size:48px;color:#ec4899;margin-bottom:12px;display:block;opacity:0.3"></i><p>لا توجد إشعارات</p></div>';return}c.innerHTML=items.map(([key,n])=>'<div class="notif-item '+(n.read?'':'unread')+'"><div class="notif-icon"><i class="fas fa-'+(n.type==='follow'?'user-plus':n.type==='like'?'heart':n.type==='comment'?'comment':n.type==='message'?'envelope':n.type==='broadcast'?'bullhorn':'bell')+'"></i></div><div class="notif-content"><div class="notif-msg"><strong>@'+(n.from||'مستخدم')+'</strong> '+(n.msg||'')+'</div><div class="notif-time">'+new Date(n.timestamp).toLocaleString('ar-SA')+'</div></div></div>').join('')})}</script>
</body></html>"""

def build_settings():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover"><title>🌹 ROSE SPHERE | إعدادات</title><script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script><script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script><script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script><link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet"><style>:root{--border:rgba(236,72,153,0.15);--accent:#ec4899;--bg:#1a0a14}*{margin:0;padding:0;box-sizing:border-box}body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:#fff;min-height:100vh;overflow-y:auto}.header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(26,10,20,0.8);backdrop-filter:blur(20px);z-index:10}.btn-back{background:rgba(236,72,153,0.1);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px}.setting-group{margin:20px 0}.setting-group-title{padding:8px 16px;font-size:12px;opacity:0.5;text-transform:uppercase}.setting-item{display:flex;justify-content:space-between;align-items:center;padding:16px;border-bottom:1px solid var(--border);cursor:pointer;transition:background 0.2s}.setting-item:hover{background:rgba(255,255,255,0.03)}.setting-item i{color:var(--accent);font-size:18px;width:30px}.setting-item .left{display:flex;align-items:center;gap:12px}.btn-danger{background:rgba(239,68,68,0.2);border:1px solid rgba(239,68,68,0.3);color:#f87171;padding:12px 24px;border-radius:30px;cursor:pointer;font-size:14px;margin:20px auto;display:block}</style></head>
<body><div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2>⚙️ الإعدادات</h2></div><div class="setting-group"><div class="setting-group-title">الحساب</div><div class="setting-item" onclick="window.location.href='profile.html'"><div class="left"><i class="fas fa-user"></i><span>الملف الشخصي</span></div><i class="fas fa-chevron-left" style="opacity:0.5"></i></div><div class="setting-item"><div class="left"><i class="fas fa-lock"></i><span>الخصوصية والأمان</span></div><i class="fas fa-chevron-left" style="opacity:0.5"></i></div></div><div class="setting-group"><div class="setting-group-title">التطبيق</div><div class="setting-item"><div class="left"><i class="fas fa-globe"></i><span>اللغة</span></div><span style="opacity:0.5;font-size:13px">العربية</span></div></div><button class="btn-danger" onclick="if(confirm('تسجيل الخروج؟')){auth.signOut();window.location.href='auth.html'}"><i class="fas fa-sign-out-alt"></i> تسجيل الخروج</button>
<script src="firebase-config.js"></script><script>auth.onAuthStateChanged(u=>{if(!u)window.location.href='auth.html'});</script></body></html>"""

# ═══════════════════════════════════════════════════════════
# 🌹 MAIN
# ═══════════════════════════════════════════════════════════

def main():
    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║  🌹  ROSE SPHERE - Premium Social Platform  🌹        ║
║     Ultimate Edition - 9 Files - 1700+ Lines            ║
║     💖 Pink Design - 👑 Admin - 📸 Images              ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
    """)
    section("BUILDING FILES")
    write("firebase-config.js", build_config())
    write("auth.html", build_auth())
    write("index.html", build_index())
    write("profile.html", build_profile())
    write("upload.html", build_upload())
    write("chat.html", build_chat())
    write("explore.html", build_explore())
    write("notifications.html", build_notifications())
    write("settings.html", build_settings())
    print(f"""
{'='*60}
  🌹 BUILD COMPLETE! 🌹
{'='*60}
  📊 {TOTAL_LINES}+ Lines | 9 Files
  👑 Admin: jasim28v@gmail.com
  💖 ROSE SPHERE v3.0 READY!
{'='*60}
""")

if __name__ == "__main__":
    main()
