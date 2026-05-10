# Flask Web App

A **course-style Flask** project: SQLAlchemy models for users and posts, forms, and a few routes. It’s a sibling to *Flask Blog App*—same general idea (Flask + SQLite + templates), often used as book or tutorial source code.

## You’ll need

- Python 3.10+  
- Packages in `requirements.txt`

## Quick start

```bash
cd "Flask Web App"
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Visit **http://127.0.0.1:5000** (or the port shown in the terminal).

## Layout

- `app.py` — Flask app, models, routes  
- `forms.py` — registration / login forms  
- `templates/` & `static/` — front end  

If this copy still uses a **short password column** or **demo-only login** logic, compare with *Flask Blog App* for patterns like password hashing and `confirm_password` on the register form.

## Security note

Treat `SECRET_KEY` and any demo credentials as **development-only**. Rotate secrets before any real deployment.
