# 🚀 Futuristic Login Application

A modern, cyberpunk-inspired authentication system built with Streamlit featuring advanced UI design, secure login functionality, and an immersive user experience.


## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Code Architecture](#code-architecture)
- [Demo Credentials](#demo-credentials)
- [Dependencies](#dependencies)

## 🌟 Overview

The Futuristic Login Application is a single-file Streamlit application that provides a complete authentication system with both login and registration functionality. The application features a cyberpunk-inspired design with custom CSS styling, secure password handling, and session management.

## ✨ Features

### 🔐 Authentication System
- **Secure Login**: SHA-256 password hashing
- **User Registration**: Complete signup form with validation
- **Session Management**: Login state persistence using Streamlit session state
- **Rate Limiting**: 3 failed attempts trigger 5-minute lockout
- **Remember Me**: Checkbox option for login persistence

### 🎨 User Interface
- **Cyberpunk Design**: Dark gradient backgrounds with neon colors
- **Glass Morphism**: Translucent containers with backdrop blur effects
- **Custom Animations**: Glow effects, rainbow text, hover transitions
- **Responsive Layout**: Centered design with custom styling
- **Interactive Elements**: Animated buttons, loading spinners, form effects

### 🛡️ Security Features
- **Password Hashing**: SHA-256 encryption for stored passwords
- **Email Validation**: Regex pattern matching for email format
- **Input Validation**: Required field checking and password confirmation
- **Brute Force Protection**: Automatic lockout after multiple failed attempts


## 🚀 Installation

### Prerequisites
- Python 3.7+
- Streamlit

### Setup
1. Save the code as `app.py`
2. Install Streamlit:
   ```bash
   pip install streamlit
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

## 💻 Usage

### Login Process
1. Open the application in your browser
2. Use the "🚀 LOGIN" tab
3. Enter username and password
4. Optional: Check "Remember me"
5. Click "INITIALIZE LOGIN SEQUENCE"

### Registration Process
1. Switch to "👤 SIGN UP" tab
2. Fill in all required fields:
   - Full Name
   - Email
   - Username
   - Password (minimum 6 characters)
   - Confirm Password
3. Check "I accept the Terms of Service"
4. Click "CREATE QUANTUM ACCOUNT"


## 🏗️ Project Structure

```
├── app.py                 # Single file containing entire application
```

## 🔧 Code Architecture

### Main Components

#### 1. **Page Configuration**
```python
st.set_page_config(
    page_title=" Futuristic Login",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed"
)
```

#### 2. **CSS Styling (`load_css()`)**
- Custom CSS with Orbitron font from Google Fonts
- Glass morphism effects with backdrop filters
- Gradient backgrounds and neon color schemes
- Keyframe animations for glow, rainbow, pulse, shake, and spin effects
- Responsive design elements

#### 3. **Authentication Functions**

**User Validation**
```python
def authenticate_user(username, password):
    if username in DEMO_USERS:
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        return DEMO_USERS[username] == password_hash
    return False
```

**Email Validation**
```python
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
```

#### 4. **Session State Management**
- `st.session_state.logged_in`: Boolean for authentication status
- `st.session_state.login_attempts`: Counter for failed login attempts
- `st.session_state.last_attempt_time`: Timestamp for rate limiting
- `st.session_state.username`: Current logged-in user

#### 5. **UI Components**

**Loading Animation**
```python
def show_loading():
    with st.empty():
        st.markdown('<div class="loading-spinner"></div>', unsafe_allow_html=True)
        time.sleep(2)
```

**Form Handling**
- Streamlit forms with custom styling
- Real-time validation and error messages
- Success notifications with balloons effect

#### 6. **Hardcoded Data**
- Demo user credentials stored in `DEMO_USERS` dictionary
- Mock activity data for dashboard display
- Static feature cards and statistics

## 🔑 Demo Credentials

The application includes three hardcoded demo accounts:

| Username | Password    |
|----------|-------------|
| admin    | quantum2024 |
| user     | future123   |
| demo     | demo123     |

## 📦 Dependencies

### Required Libraries
```python
import streamlit as st
import time
import hashlib
import re
from datetime import datetime
```

### External Resources
- **Google Fonts**: Orbitron font family
- **Streamlit**: Web framework and UI components

### CSS Features Used
- Backdrop filters for glass morphism
- CSS Grid for responsive layouts
- Keyframe animations
- Custom form styling
- Gradient backgrounds

## 🎨 Design Elements

### Color Scheme
- **Primary Cyan**: #00f5ff
- **Secondary Magenta**: #ff00ff
- **Accent Green**: #00ff00
- **Background Gradient**: #0c0c0c to #533a7b

### Animations
- **Glow Effect**: Pulsing box shadows
- **Rainbow Text**: Hue rotation animation
- **Loading Spinner**: Rotating border animation
- **Shake Effect**: Error message animation
- **Hover Effects**: Transform and shadow transitions

### Typography
- **Primary Font**: Orbitron (Google Fonts)
- **Fallback**: cursive
- **Usage**: Headers, labels, and UI text

## 🔒 Security Implementation

### Password Security
- SHA-256 hashing for all passwords
- Passwords stored as hashed strings in `DEMO_USERS`
- No plain text password storage

### Rate Limiting
- Maximum 3 failed login attempts
- 5-minute (300 seconds) cooldown period
- Time-based lockout implementation

### Input Validation
- Email format validation using regex
- Required field checking
- Password length minimum (6 characters)
- Password confirmation matching

## 📊 Dashboard Features

### User Information Display
- Current username
- Login timestamp
- Authentication status
- Security level indicator

### Mock Statistics
- **Active Sessions**: 1
- **Security Score**: 100
- **Last Login**: Now

### Activity Feed
Hardcoded activity items:
- Login successful
- Security scan completed
- System update applied
- Backup completed

### Action Buttons
- **Launch Dashboard**
- **Settings**

- **Logout** (clears session state)

## Author
Developed by **Ganesh**.

---

### License

This project is for educational and visualization purposes. Please check the data source for any restrictions on data usage.

---

### Contact

If you have any questions or need help with the visualization, feel free to reach out to me at [email](mailto:roy862452@gmail.com) and I'll be happy to help. You can also open an issue on GitHub or submit a pull request if you'd like to contribute to the project. Alternatively, you can message me on [WhatsApp](https://wa.me/8249873663).
