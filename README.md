<div align="center">

# 📝 Byline

**A multi-author publishing platform, built with FastAPI.**

Async PostgreSQL · JWT Authentication · AWS S3 Image Uploads · Email Password Reset · Docker · Deployed on Render

[![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Neon-4169E1?style=flat&logo=postgresql&logoColor=white)](https://neon.tech/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![AWS S3](https://img.shields.io/badge/AWS-S3-FF9900?style=flat&logo=amazons3&logoColor=white)](https://aws.amazon.com/s3/)
[![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?style=flat&logo=render&logoColor=white)](https://render.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[Live Demo](https://fastapi-blog-x6vf.onrender.com) · [API Docs](https://fastapi-blog-x6vf.onrender.com/docs) · [Health Check](https://fastapi-blog-x6vf.onrender.com/health)

</div>

---

## 📖 Overview

**Byline** is a multi-author publishing platform where users register, authenticate, write and manage posts under their own byline, upload profile pictures to AWS S3, reset passwords via email, and browse posts with pagination.

The project follows modern backend engineering practices: asynchronous database operations, Alembic-managed migrations, Docker containerization, environment-based configuration, secure authentication, and cloud deployment — built to mirror the structure of a real production system rather than a simple CRUD demo.

**Live stack:** deployed on **Render**, backed by **Neon PostgreSQL**, storing media in **AWS S3**, and sending transactional email via **Mailtrap SMTP**.

---

## 🚀 Live Demo

| Resource | Link |
|---|---|
| 🌐 Application | [fastapi-blog-x6vf.onrender.com](https://fastapi-blog-x6vf.onrender.com) |
| 📑 Swagger API Docs | [/docs](https://fastapi-blog-x6vf.onrender.com/docs) |
| 💓 Health Endpoint | [/health](https://fastapi-blog-x6vf.onrender.com/health) |

> ⚠️ Hosted on Render's free tier — the app may take a few seconds to spin up after inactivity.

---

## 💡 Why I Built This

I built this project to move beyond basic CRUD apps and get hands-on experience building a **production-style backend** with FastAPI. Rather than another simple to-do API, I wanted to implement the kind of features that show up in real-world applications — proper auth, file storage, email flows, migrations, and cloud deployment — all working together.

**Focus areas:**

- FastAPI application architecture & async programming
- PostgreSQL with SQLAlchemy (async)
- JWT authentication & secure password hashing
- Cloud file storage (AWS S3)
- Transactional email integration
- Docker & database migrations
- Production deployment & environment management

---

## 🎓 What I Learned

Building this project gave me practical, hands-on experience with:

| Area | Skills Gained |
|---|---|
| **Backend** | FastAPI, async SQLAlchemy, dependency injection, REST API design |
| **Database** | PostgreSQL, Neon, Alembic migrations, relational modeling |
| **Auth & Security** | JWT authentication, Argon2 hashing, password reset workflows |
| **Cloud & Storage** | AWS S3 integration with boto3, secure image upload validation |
| **Email** | SMTP integration via Mailtrap |
| **DevOps** | Docker, multi-stage builds, production deployment on Render |
| **Frontend** | Jinja2 templating, server-rendered HTML/CSS/JS |
| **Engineering Practice** | Environment variable management, health monitoring, pagination, project structure |

---

## 🛠️ Tech Stack

<table>
<tr>
<td valign="top" width="33%">

**Backend**
- Python 3.14
- FastAPI
- SQLAlchemy (Async)
- Alembic

**Database**
- PostgreSQL
- Neon

</td>
<td valign="top" width="33%">

**Frontend**
- HTML / CSS / JavaScript
- Jinja2 Templates

**Authentication**
- JWT
- Argon2 Password Hashing

</td>
<td valign="top" width="33%">

**Cloud & Infra**
- AWS S3
- Render
- Docker

**Email**
- Mailtrap SMTP

**Tooling**
- uv (package management)

</td>
</tr>
</table>

**Key libraries:** `boto3` · `Pillow` · `psycopg` · `pydantic-settings` · `PyJWT`

---

## ✨ Current Features

| Category | Features |
|---|---|
| 🔐 **Authentication** | User registration, login, JWT auth, secure password hashing, email-based password reset |
| ✍️ **Blog** | Create, edit, delete, and view posts · pagination |
| 👤 **User Profiles** | Profile page, profile picture upload, AWS S3 storage, image validation & processing (Pillow) |
| 🗄️ **Database** | Async SQLAlchemy, PostgreSQL, Alembic migrations, relational models |
| 🚢 **Deployment** | Dockerized app, multi-stage builds, Render + Neon + S3 + Mailtrap in production |
| 🛡️ **Security** | JWT auth, protected routes, password hashing, secure env vars, security headers, file validation |
| 📊 **Monitoring** | `/health` check endpoint |

---

## 🏗️ Architecture

```
Browser
   │
   ▼
Render (Docker Container)
   │
   ▼
FastAPI Application
   │
 ┌──┴────────────────┐
 ▼                    ▼
Neon PostgreSQL     AWS S3
   │
   ▼
Mailtrap SMTP
```

---

## 📁 Folder Structure

```
FastAPI_Blog/
├── alembic/
│   └── versions/
├── media/
├── populate_images/
├── routers/
│   ├── posts.py
│   └── users.py
├── static/
├── templates/
├── tests/
├── auth.py
├── config.py
├── database.py
├── email_utils.py
├── image_utils.py
├── main.py
├── models.py
├── populate_db.py
├── schemas.py
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── uv.lock
├── requirements.txt
├── alembic.ini
└── .env.example
```

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/pruthviklshetty/FastAPI_Blog.git
cd FastAPI_Blog

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install dependencies with uv
uv sync

# 4. Configure environment variables
cp .env.example .env
# Fill in .env with your own values (see table below)

# 5. Run database migrations
alembic upgrade head

# 6. Start the development server
uvicorn main:app --reload
```

The app will be available at `http://127.0.0.1:8000`, with interactive docs at `http://127.0.0.1:8000/docs`.

---

## 🐳 Docker

```bash
# Build the image
docker build -t fastapi-blog .

# Run the container, passing environment variables from your .env file
docker run --env-file .env -p 8000:8000 fastapi-blog
```

Or, using Docker Compose:

```bash
docker-compose up --build
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root with the following variables:

| Variable | Description |
|---|---|
| `DATABASE_URL` | Async PostgreSQL connection string |
| `SECRET_KEY` | Secret key used to sign JWTs |
| `S3_BUCKET_NAME` | AWS S3 bucket name for image storage |
| `S3_REGION` | AWS region of the S3 bucket |
| `S3_ACCESS_KEY_ID` | AWS access key ID |
| `S3_SECRET_ACCESS_KEY` | AWS secret access key |
| `MAIL_SERVER` | SMTP server host (e.g. Mailtrap) |
| `MAIL_PORT` | SMTP server port |
| `MAIL_USERNAME` | SMTP username |
| `MAIL_PASSWORD` | SMTP password |
| `MAIL_FROM` | Sender email address |
| `MAIL_USE_TLS` | Whether to use TLS for SMTP (`true`/`false`) |
| `FRONTEND_URL` | Base URL used in password-reset email links |

> See `.env.example` for a template.

---

## 📡 API Overview

| Group | Description |
|---|---|
| **Authentication** | Register, login, JWT token issuance |
| **Users** | Profile retrieval, profile picture upload/update |
| **Blog** | Create, read, update, delete posts, with pagination |
| **Password Reset** | Request reset link via email, confirm and set new password |
| **Health** | Simple `/health` endpoint for uptime/monitoring checks |

Full interactive documentation (request/response schemas, try-it-out console) is auto-generated by FastAPI and available at [`/docs`](https://fastapi-blog-x6vf.onrender.com/docs).

---



## 👤 Author

**Pruthvik L Shetty**

- GitHub: [@pruthviklshetty](https://github.com/pruthviklshetty)
- LinkedIn: - www.linkedin.com/in/pruthviklshetty

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

⭐ If you found this project interesting, consider giving it a star!

</div>
