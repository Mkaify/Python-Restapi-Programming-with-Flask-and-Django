# Game Store

A **Django 4** sample: browse games, sign up, log in, use a **shopping cart**, and manage data through the **admin** site. The database is **SQLite** (`db.sqlite3` next to `manage.py`).

## You’ll need

- Python 3.8–3.11 (3.10 works well)  
- `pip install -r requirements.txt` → Django 4.0.2 and Pillow (for image fields)

## Quick start

```bash
cd "Game Store"
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open **http://127.0.0.1:8000/**.

### First-time setup tips

- Create an admin user: `python manage.py createsuperuser` → then **http://127.0.0.1:8000/admin/** to add platforms, games, and prices.  
- The storefront may look empty until you add data in admin.  
- Optional front-end tooling: `package.json` / `node_modules` for Bootstrap-style assets—Django will still run if you skip Node.

## Layout

- `manage.py` — Django CLI entry  
- `gamestore/` — project settings, `urls.py`, WSGI  
- `main/` — app: models, views, templates under `main/templates/`  
- `templates/` & `static/` — shared site templates and static files  

`DEBUG` and `SECRET_KEY` in `gamestore/settings.py` are for **learning only**—never ship that to production unchanged.
