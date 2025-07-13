import streamlit as st
import time
import hashlib
import re
from datetime import datetime

# Configure page
st.set_page_config(
    page_title=" Futuristic Login",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for futuristic design
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #0c0c0c 0%, #1a1a2e 25%, #16213e 50%, #0f3460 75%, #533a7b 100%);
        background-attachment: fixed;
    }
    
    .main-container {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3); }
        to { box-shadow: 0 8px 32px rgba(83, 58, 123, 0.4); }
    }
    
    .logo-container {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .logo {
        
        font-family: 'Orbitron', cursive;
        font-size: 3rem;
        font-weight: 900;
        background: linear-gradient(45deg, #00f5ff, #ff00ff, #00ff00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: rainbow 3s ease-in-out infinite;
        text-shadow: 0 0 30px rgba(0, 245, 255, 0.5);
    }
    
    @keyframes rainbow {
        0% { filter: hue-rotate(0deg); }
        100% { filter: hue-rotate(360deg); }
    }
    
    .subtitle {
        font-family: 'Orbitron', monospace;
        color: #00f5ff;
        font-size: 1.2rem;
        text-align: center;
        margin-bottom: 2rem;
        opacity: 0.8;
    }
    
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid rgba(0, 245, 255, 0.3) !important;
        border-radius: 10px !important;
        color: #ffffff !important;
        font-family: 'Orbitron', monospace !important;
        padding: 0.75rem !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #00f5ff !important;
        box-shadow: 0 0 20px rgba(0, 245, 255, 0.5) !important;
        transform: translateY(-2px) !important;
    }
    
    .stButton > button {
        background: linear-gradient(45deg, #00f5ff, #ff00ff) !important;
        border: none !important;
        border-radius: 25px !important;
        color: white !important;
        font-family: 'Orbitron', monospace !important;
        font-weight: 700 !important;
        padding: 0.75rem 2rem !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        width: 100% !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 10px 25px rgba(0, 245, 255, 0.4) !important;
        background: linear-gradient(45deg, #ff00ff, #00f5ff) !important;
    }
    
    .success-message {
        background: rgba(0, 255, 0, 0.1);
        border: 1px solid #00ff00;
        border-radius: 10px;
        padding: 1rem;
        color: #00ff00;
        font-family: 'Orbitron', monospace;
        text-align: center;
        animation: pulse 1s ease-in-out infinite;
    }
    
    .error-message {
        background: rgba(255, 0, 0, 0.1);
        border: 1px solid #ff0000;
        border-radius: 10px;
        padding: 1rem;
        color: #ff0000;
        font-family: 'Orbitron', monospace;
        text-align: center;
        animation: shake 0.5s ease-in-out;
    }
    
    @keyframes pulse {
        0% { opacity: 0.8; }
        50% { opacity: 1; }
        100% { opacity: 0.8; }
    }
    
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
        20%, 40%, 60%, 80% { transform: translateX(5px); }
    }
    
    .form-section {
        margin-bottom: 1.5rem;
    }
    
    .form-label {
        color: #00f5ff;
        font-family: 'Orbitron', monospace;
        font-weight: 700;
        margin-bottom: 0.5rem;
        display: block;
    }
    
    .loading-spinner {
        border: 4px solid rgba(0, 245, 255, 0.3);
        border-top: 4px solid #00f5ff;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        animation: spin 1s linear infinite;
        margin: 0 auto;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #00f5ff, transparent);
        margin: 2rem 0;
    }
    
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 1rem;
        margin-top: 2rem;
    }
    
    .feature-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(0, 245, 255, 0.2);
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        border-color: #00f5ff;
    }
    
    .feature-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    
    .feature-title {
        color: #00f5ff;
        font-family: 'Orbitron', monospace;
        font-size: 0.9rem;
        font-weight: 700;
    }
    
    .stats-container {
        display: flex;
        justify-content: space-around;
        margin: 2rem 0;
    }
    
    .stat-item {
        text-align: center;
        color: #00f5ff;
        font-family: 'Orbitron', monospace;
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: 900;
        display: block;
    }
    
    .stat-label {
        font-size: 0.8rem;
        opacity: 0.7;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Demo credentials (in production, use proper database)
DEMO_USERS = {
    "admin": hashlib.sha256("quantum2024".encode()).hexdigest(),
    "user": hashlib.sha256("future123".encode()).hexdigest(),
    "demo": hashlib.sha256("demo123".encode()).hexdigest()
}

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def authenticate_user(username, password):
    if username in DEMO_USERS:
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        return DEMO_USERS[username] == password_hash
    return False

def show_loading():
    with st.empty():
        st.markdown('<div class="loading-spinner"></div>', unsafe_allow_html=True)
        time.sleep(2)

def main():
    load_css()
    
    # Initialize session state
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'login_attempts' not in st.session_state:
        st.session_state.login_attempts = 0
    if 'last_attempt_time' not in st.session_state:
        st.session_state.last_attempt_time = 0
    
    # Main container
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    if not st.session_state.logged_in:
        # Logo and branding
        st.markdown("""
        <div class="logo-container">
            <div class="logo">Futuristic Login</div>
            <div class="subtitle">Next-Generation Authentication Portal</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Create tabs for Login and Sign Up
        tab1, tab2 = st.tabs(["🚀 LOGIN", "👤 SIGN UP"])
        
        with tab1:
            st.markdown('<div class="form-section">', unsafe_allow_html=True)
            
            # Login form
            with st.form("login_form", clear_on_submit=False):
                st.markdown('<label class="form-label">USERNAME</label>', unsafe_allow_html=True)
                username = st.text_input("", placeholder="Enter your username", key="username", label_visibility="collapsed")
                
                st.markdown('<label class="form-label">PASSWORD</label>', unsafe_allow_html=True)
                password = st.text_input("", placeholder="Enter your password", type="password", key="password", label_visibility="collapsed")
                
                col1, col2 = st.columns([1, 1])
                with col1:
                    remember_me = st.checkbox("Remember me", key="remember")
                with col2:
                    st.markdown('<a href="#" style="color: #00f5ff; text-decoration: none; float: right;">Forgot Password?</a>', unsafe_allow_html=True)
                
                submit_button = st.form_submit_button("INITIALIZE LOGIN SEQUENCE")
                
                if submit_button:
                    current_time = time.time()
                    
                    # Rate limiting
                    if st.session_state.login_attempts >= 3 and current_time - st.session_state.last_attempt_time < 300:
                        st.markdown('<div class="error-message">⚠️ TOO MANY ATTEMPTS. PLEASE WAIT 5 MINUTES.</div>', unsafe_allow_html=True)
                    else:
                        if not username or not password:
                            st.markdown('<div class="error-message">⚠️ PLEASE FILL IN ALL FIELDS</div>', unsafe_allow_html=True)
                        else:
                            # Show loading animation
                            show_loading()
                            
                            if authenticate_user(username, password):
                                st.session_state.logged_in = True
                                st.session_state.username = username
                                st.session_state.login_attempts = 0
                                st.markdown('<div class="success-message">✅ AUTHENTICATION SUCCESSFUL</div>', unsafe_allow_html=True)
                                time.sleep(1)
                                st.rerun()
                            else:
                                st.session_state.login_attempts += 1
                                st.session_state.last_attempt_time = current_time
                                st.markdown('<div class="error-message">❌ INVALID CREDENTIALS</div>', unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Demo credentials info
            st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
            st.markdown("### 🔐 Demo Credentials")
            st.markdown("```")
            st.markdown("Username: admin | Password: quantum2024")
            st.markdown("Username: user  | Password: future123")
            st.markdown("Username: demo  | Password: demo123")
            st.markdown("```")
        
        with tab2:
            st.markdown('<div class="form-section">', unsafe_allow_html=True)
            
            # Sign up form
            with st.form("signup_form"):
                st.markdown('<label class="form-label">FULL NAME</label>', unsafe_allow_html=True)
                full_name = st.text_input("", placeholder="Enter your full name", key="signup_name", label_visibility="collapsed")
                
                st.markdown('<label class="form-label">EMAIL</label>', unsafe_allow_html=True)
                email = st.text_input("", placeholder="Enter your email", key="signup_email", label_visibility="collapsed")
                
                st.markdown('<label class="form-label">USERNAME</label>', unsafe_allow_html=True)
                new_username = st.text_input("", placeholder="Choose a username", key="signup_username", label_visibility="collapsed")
                
                st.markdown('<label class="form-label">PASSWORD</label>', unsafe_allow_html=True)
                new_password = st.text_input("", placeholder="Create a password", type="password", key="signup_password", label_visibility="collapsed")
                
                st.markdown('<label class="form-label">CONFIRM PASSWORD</label>', unsafe_allow_html=True)
                confirm_password = st.text_input("", placeholder="Confirm your password", type="password", key="confirm_password", label_visibility="collapsed")
                
                col1, col2 = st.columns([1, 1])
                with col1:
                    accept_terms = st.checkbox("I accept the Terms of Service", key="terms")
                with col2:
                    newsletter = st.checkbox("Subscribe to newsletter", key="newsletter")
                
                signup_button = st.form_submit_button("CREATE QUANTUM ACCOUNT")
                
                if signup_button:
                    if not all([full_name, email, new_username, new_password, confirm_password]):
                        st.markdown('<div class="error-message">⚠️ PLEASE FILL IN ALL FIELDS</div>', unsafe_allow_html=True)
                    elif not validate_email(email):
                        st.markdown('<div class="error-message">⚠️ INVALID EMAIL FORMAT</div>', unsafe_allow_html=True)
                    elif new_password != confirm_password:
                        st.markdown('<div class="error-message">⚠️ PASSWORDS DO NOT MATCH</div>', unsafe_allow_html=True)
                    elif len(new_password) < 6:
                        st.markdown('<div class="error-message">⚠️ PASSWORD MUST BE AT LEAST 6 CHARACTERS</div>', unsafe_allow_html=True)
                    elif not accept_terms:
                        st.markdown('<div class="error-message">⚠️ PLEASE ACCEPT THE TERMS OF SERVICE</div>', unsafe_allow_html=True)
                    else:
                        show_loading()
                        st.markdown('<div class="success-message">✅ ACCOUNT CREATED SUCCESSFULLY</div>', unsafe_allow_html=True)
                        st.balloons()
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Features section
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown("### 🌟It's Features")
        
        st.markdown("""
        <div class="features-grid">
            <div class="feature-card">
                <div class="feature-icon">🔒</div>
                <div class="feature-title">HIGH ENCRYPTION</div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">⚡</div>
                <div class="feature-title">LIGHTNING FAST</div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🛡️</div>
                <div class="feature-title">SECURE PROTOCOL</div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🌐</div>
                <div class="feature-title">GLOBAL ACCESS</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Stats section
        st.markdown("""
        <div class="stats-container">
            <div class="stat-item">
                <span class="stat-number">99.9%</span>
                <span class="stat-label">UPTIME</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">1M+</span>
                <span class="stat-label">USERS</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">256</span>
                <span class="stat-label">BIT ENCRYPTION</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    else:
        # Dashboard for logged-in users
        st.markdown("""
        <div class="logo-container">
            <div class="logo">WELCOME BACK</div>
            <div class="subtitle"> Dashboard Initialized</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"### 👋 Hello, {st.session_state.username}!")
        st.markdown(f"**Login Time:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        st.markdown(f"**Status:** ✅ Authenticated")
        st.markdown(f"**Security Level:** 🔒 Maximum")
        
        # Dashboard content
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Active Sessions", "1", "↗️ 100%")
        
        with col2:
            st.metric("Security Score", "100", "🔒 Secure")
        
        with col3:
            st.metric("Last Login", "Now", "⚡ Active")
        
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        
        # Action buttons
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🚀 LAUNCH DASHBOARD", key="dashboard"):
                st.success("Dashboard module loading...")
        
        with col2:
            if st.button("⚙️ SETTINGS", key="settings"):
                st.info("Settings panel activated...")
        
        with col3:
            if st.button("🔓 LOGOUT", key="logout"):
                st.session_state.logged_in = False
                st.session_state.username = None
                st.rerun()
        
        # Activity feed
        st.markdown("### 📊 Recent Activity")
        activity_data = [
            {"time": "2025-07-12 10:30", "action": "Login successful", "status": "✅"},
            {"time": "2025-07-12 09:15", "action": "Security scan completed", "status": "🔒"},
            {"time": "2025-07-12 08:45", "action": "System update applied", "status": "⚙️"},
            {"time": "2025-07-12 08:00", "action": "Backup completed", "status": "💾"},
        ]
        
        for item in activity_data:
            st.markdown(f"**{item['time']}** {item['status']} {item['action']}")
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()