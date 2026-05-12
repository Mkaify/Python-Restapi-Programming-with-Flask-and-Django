# Python: REST APIs, Flask & Django

This repo is a **learning workspace**—a handful of small, self-contained projects that sit side by side. Each folder is its own app with its own dependencies and run instructions. Nothing here is wired together; pick a project, open that folder, and run it on its own.

## What’s inside

| Project | Stack | What it is |
|--------|--------|------------|
| **[Flask Blog App](Flask%20Blog%20App/)** | Flask | Blog-style UI: posts, register, login, SQLite users with hashed passwords. |
| **[Flask Web App](Flask%20Web%20App/)** | Flask | Similar Flask + SQLAlchemy tutorial app (course-style). |
| **[Game Store](Game%20Store/)** | Django | Game storefront: cart, auth, admin, SQLite. |
| **[Messaging Service](Messaging%20Service/)** | Nameko + Redis + RabbitMQ | Tiny messaging microservice with HTTP + RPC. |

## Before you start

- **Python 3.10+** is a safe default for these projects.
- Use a **virtual environment per project** (`python -m venv .venv`, then `pip install -r requirements.txt`).
- The root **`.gitignore`** keeps secrets, databases, and virtualenvs out of Git—don’t disable it for convenience.

## Need help?

Open the **README in the project you care about**—each one explains how to run that app and what to install. If you move folders on disk, paths in your editor (Python interpreter, terminals) may need a quick update; the code itself doesn’t depend on living under a parent named `Projects`.

Happy hacking.
