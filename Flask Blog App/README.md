# Flask Blog App

A compact **Flask** demo that feels like a mini blog: a home page with sample posts, registration, and login. Users are stored in **SQLite** via **Flask-SQLAlchemy**, and passwords are **hashed** (not stored in plain text).

## You’ll need

- Python 3.10+  
- Dependencies from `requirements.txt` (Flask, Flask-WTF, Flask-SQLAlchemy, WTForms, etc.)

## Quick start

```bash
cd "Flask Blog App"
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

On first run the app creates database tables. **Sign up** a user, then **log in** with the same email and password. The admin-style hardcoded login from older tutorials is gone—this app uses the database.

## Project layout (the useful bits)

- `app.py` — routes, models, app factory-ish setup  
- `forms.py` — WTForms for register / login  
- `templates/` — Jinja2 HTML  
- `static/` — CSS  

Local data (`site.db`, `instance/`) is meant to stay on your machine—don’t commit it.

## Heads-up

`SECRET_KEY` in `app.py` is for **local dev only**. For anything public, use an environment variable and a real secret.
