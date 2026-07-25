# AGENTS.md

## Project

Flask web app scaffolded with `uv`. Python 3.10+.

## Setup

```sh
uv sync          # install dependencies into .venv
```

## Run

```sh
uv run python main.py
```

## Structure

```
app/
├── __init__.py          # Flask app factory (create_app)
├── config.py            # Config classes (dev/prod/testing)
├── routes/              # Blueprints
│   ├── main.py          # Home page route
│   ├── users.py         # User CRUD routes
│   ├── api.py           # JSON API endpoints
│   ├── htmx.py          # HTMX-powered page
│   └── docs.py          # Swagger UI
├── models/              # SQLAlchemy models
│   └── user.py          # User entity
├── templates/           # Jinja2 templates
│   ├── base.html        # Layout base
│   ├── main/            # Home page
│   ├── users/           # User views (Jinja2)
│   └── htmx/            # HTMX-powered views
│       ├── index.html   # Main HTMX page
│       └── partials/    # HTML fragments for HTMX
├── static/              # CSS, JS, images (add when needed)
└── database/            # SQLAlchemy db instance and migrations
```

## Key facts

- Package manager: **uv** (lockfile: `uv.lock`, version pinned in `.python-version`)
- Entry point: `main.py` → calls `create_app()` from `app/__init__.py`
- Config loaded via `FLASK_ENV` env var (default: `development`)
- All config from env vars via `.env` — no hardcoded secrets. Required: `SECRET_KEY`, `DATABASE_URL`, `FLASK_ENV`
- `python-dotenv` loads `.env` before config is read
- ORM: **Flask-SQLAlchemy** (SQLAlchemy 2.0). Migrations: **Flask-Migrate** (Alembic)
- Database URI comes from `DATABASE_URL` env var, mapped to `SQLALCHEMY_DATABASE_URI` in config
- Models import in `app/models/__init__.py` — import there to register with SQLAlchemy
- `main.py` calls `db.create_all()` for dev; use `flask db migrate` / `flask db upgrade` for schema changes
- No tests, linter config, or CI exist yet
