# 🔐 Secure Email OTP Authentication System

A production-ready email-based OTP authentication system built with Python and Django. Features time-bound OTP generation, real-time verification, and secure identity validation — with zero reported auth bypass issues in testing.

**Live Demo → [secureauth-1-vsla.onrender.com](https://secureauth-1-vsla.onrender.com)**

---

## What It Does

- User enters their email address to request a one-time password
- System generates a unique OTP and sends it to the user's email
- OTP expires automatically after a set time window (expiry handling built in)
- User submits the OTP for real-time verification
- On success, user identity is confirmed and session is established
- Invalid or expired OTPs are rejected cleanly with appropriate error feedback

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3, Django |
| Database | SQLite |
| Email | Django email backend (SMTP) |
| Frontend | HTML5, CSS3 (responsive) |
| Deployment | Render (with Procfile + runtime.txt) |

---

## Key Features

- **Time-bound OTPs** — automatically expire to prevent replay attacks
- **Real-time verification logic** — instant feedback on valid/invalid/expired OTP
- **Secure identity validation** — no auth bypass vulnerabilities found in testing
- **Clean Django project structure** — modular, readable, reusable as a base module
- **Deployed live** — not just a local demo; runs on Render with a real CI pipeline

---

## Project Structure

```
SecureAuth/
├── Email/          # Email sending logic and OTP generation
├── EmailOTP/       # Django app: views, models, URLs for OTP flow
├── manage.py
├── requirements.txt
├── runtime.txt     # Python version for Render
└── procfile        # Render deployment config
```

---

## Run Locally

```bash
# Clone the repo
git clone https://github.com/jananisri004/SecureAuth.git
cd SecureAuth

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up your email credentials in settings.py (EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
```

Then open `http://localhost:8000` in your browser.

---

## About the Developer

Built by **Janani Sri S** — Python Full Stack Developer based in Erode, Tamil Nadu.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/jananisrisenthilkumar)
[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=flat&logo=netlify&logoColor=white)](https://jananisris-portfolio.netlify.app)
