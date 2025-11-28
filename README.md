# Advanced Task Management REST API

![Typing Animation](https://readme-typing-svg.demolab.com?font=Fira%20Code&size=28&pause=2000&center=true&width=700&height=48&lines=Advanced+Task+Management+REST+API;Building+scalable+APIs+with+FastAPI+%F0%9F%92%BB)

<!-- Badges -->
[![Status](https://img.shields.io/badge/status-Under%20Development-orange)](#)
[![Python](https://img.shields.io/badge/python-3.13+-blue?style=flat-square&logo=python&logoColor=white)](#)
[![FastAPI](https://img.shields.io/badge/FastAPI-%23009688.svg?style=flat-square&logo=fastapi&logoColor=white)](#)
[![Tortoise ORM](https://img.shields.io/badge/Tortoise--ORM-07C160?style=flat-square&logo=data:image/png;base64,iVBORw0KGgo=)](#)

---

## 🔧 Project Overview

Advanced Task Management REST API is a small, modern backend for managing users, projects, and tasks. It's built on top of FastAPI for fast development and async performance, using Tortoise ORM + Aerich for database models and migrations, and is designed to be easy to extend.

This repository is currently **not finished — still under development**, and active improvements are in progress.

## 🚀 Tech Stack

Tech & services used (quick glance):

- ![Python](https://img.shields.io/badge/-Python-3670A0?style=flat-square&logo=python&logoColor=white)
- ![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
- ![Uvicorn](https://img.shields.io/badge/-Uvicorn-000?style=flat-square&logo=uvicorn&logoColor=white)
- ![Tortoise ORM](https://img.shields.io/badge/-Tortoise--ORM-07C160?style=flat-square)
- ![Aerich](https://img.shields.io/badge/-Aerich-6B8E23?style=flat-square)
- ![asyncpg](https://img.shields.io/badge/-asyncpg-4B8BBE?style=flat-square)
- ![PyJWT](https://img.shields.io/badge/-PyJWT-ffb86b?style=flat-square)

---

## 📦 Key Features

- User authentication and JWT tokens
- Projects and tasks management endpoints
- Database migrations using Aerich and Tortoise ORM
- Async endpoints and connection-ready for Postgres

---

## 💡 Getting Started (development)

### Prerequisites

- Python 3.13 or later
- PostgreSQL (or another supported DB for asyncpg)

### Quick Start

1. Clone repository

```bash
git clone https://github.com/JonniTech/Advanced-Task-Management-REST-API.git
cd "Task Management API"
```

2. Create a virtual environment and activate it

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install project dependencies

```bash
pip install -r requirements.txt
```

4. Create .env with DB and secret settings (see `configs/settings.py` for env names)

5. Run database migrations (aerich)

```bash
aerich init -t database.aerich_config.TORTOISE_ORM
aerich upgrade
```

6. Start the app locally

```bash
uvicorn main:app --reload
```

Open API docs at http://127.0.0.1:8000/docs

---

## 🧭 Project Structure

High level structure (abridged):

```
api/                 # Routers and API routes (v1)
auth/                # Authentication helpers and token logic
database/            # Connection and migration config (aerich)
models/              # Tortoise models
schemas/             # Pydantic request/response schemas
services/            # Business logic / services
main.py              # FastAPI bootstrapping
```

---

## 🤝 Contributing

Contributions and feedback are very welcome — open issues or submit a pull request. As the project is under active development, please open an issue to discuss bigger changes before implementing them.

---

## 📣 Status

This project is **under active development** — expect incomplete functionality and breaking changes on the main branch.

---

## 📫 Contact / Support

If you want to follow or contribute, open an issue or PR. You can reach the maintainer via GitHub: @JonniTech

---

_Thanks for checking this project — improvements coming soon!_ 

