** Django Docker Project

A production-structured Django web application containerized with Docker Compose.

 **Stacks
- Django 6.0 + Gunicorn
- PostgreSQL 16
- Redis 7
- Nginx (reverse proxy)

** Architecture
Browser → Nginx (port 80) → Gunicorn (port 8000) → PostgreSQL + Redis

** Quick Start
```bash
git clone https://github.com/YOUR_USERNAME/django-docker-project
cd django-docker-project
cp .env.example .env.dev   # fill in your values
docker compose up --build
docker compose exec web python manage.py migrate
```

Visit http://localhost/admin

** Features
- Multi-stage Docker builds (60% smaller images)
- Health-checked service startup ordering
- Persistent Postgres data via named volumes
- Environment-based configuration
- Nginx serving static files directly
