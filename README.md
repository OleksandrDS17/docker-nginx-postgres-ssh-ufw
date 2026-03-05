# docker-nginx-postgres-ssh-ufw
Modern Debian server stack using Docker, Nginx, PostgreSQL and Python API with security configuration (SSH + UFW).

# Docker Nginx PostgreSQL Python Server Stack

A modern Debian-based server stack using Docker, Nginx reverse proxy, PostgreSQL database and a Python FastAPI backend.

This project demonstrates a production-like setup with containerization, security configuration and CI.

## Tech Stack

- Debian Linux
- Docker & Docker Compose
- Nginx (reverse proxy)
- PostgreSQL
- Python FastAPI
- UFW Firewall
- SSH hardening
- GitHub Actions CI

## Architecture

Client → Nginx → FastAPI (Python) → PostgreSQL

## Project Structure
.
├─ README.md
├─ docker-compose.yml
├─ .env.example
├─ nginx/
├─ app/
├─ db/
├─ scripts/
├─ docs/
└─ .github/workflows/ci.yml


