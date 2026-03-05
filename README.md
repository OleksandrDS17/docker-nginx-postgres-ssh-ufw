# docker-nginx-postgres-ssh-ufw
Modern Debian server stack using Docker, Nginx, PostgreSQL and Python API with security configuration (SSH + UFW).

# Docker Nginx PostgreSQL Python Server Stack

A modern Debian-based server stack using Docker, Nginx reverse proxy, PostgreSQL database and a Python FastAPI backend.

This project demonstrates a production-like setup with containerization, security configuration and CI.

## Tech Stack

* Debian Linux
* Docker & Docker Compose
* Nginx (reverse proxy)
* PostgreSQL
* Python FastAPI
* UFW Firewall
* SSH hardening
* GitHub Actions CI

## Architecture

Client → Nginx → FastAPI (Python) → PostgreSQL

## Project Structure

```
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
```

## Quick Start

Clone repository

```
git clone https://github.com/YOUR_USERNAME/docker-nginx-postgres-ssh-ufw.git
cd docker-nginx-postgres-ssh-ufw
```

Start the system

```
docker compose up -d
```

Open in browser

```
http://localhost
```

## Services

| Service    | Description        |
| ---------- | ------------------ |
| Nginx      | Reverse proxy      |
| FastAPI    | Python backend API |
| PostgreSQL | Database           |
| Docker     | Container platform |

## Security

* SSH hardened configuration
* UFW firewall rules
* Environment variables for secrets

## Example API

```
GET /api/health
```

Response:

```
{
  "status": "ok"
}
```

## Roadmap

* HTTPS with Let's Encrypt
* Monitoring (Prometheus / Grafana)
* Kubernetes deployment



