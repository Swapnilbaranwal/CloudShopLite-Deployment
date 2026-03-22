
# CloudShop Lite — Microservices Demo

This project showcases a microservices architecture using Docker and Kubernetes, featuring:

- **API**: Python Flask backend
- **Frontend**: Python Flask web UI
# CloudShop Lite — Microservices Demo (Swapnil Edition)

This project demonstrates a microservices architecture using Docker and Kubernetes, featuring:

- **API**: Python Flask backend
- **Frontend**: Python Flask web UI
- **Worker**: Python background job processor
- **Redis**: Caching & message broker

All services are containerized and orchestrated with Kubernetes manifests. The live demo will be available at your public cloud URL after deployment.

---

## Project Structure

```
API/           # Backend Flask app
Frontend/      # Web UI Flask app
Worker/        # Background job processor
k8s-manifests/ # Kubernetes YAMLs
helm/          # Helm chart for advanced deployment
docs/          # Documentation
ci-cd/         # CI/CD configs
```

## Features

- **Frontend** displays visit count and background job stats
- **API** exposes endpoints for visit tracking and health checks
- **Worker** increments background job count in Redis
- **Redis** enables fast state sharing between services

---

## Quick Start

### 1. Build Docker Images

Navigate to each service directory and build the Docker images:

```bash
cd API && docker build -t swapnil-api-service .
cd ../Frontend && docker build -t swapnil-frontend-service .
cd ../Worker && docker build -t swapnil-worker-service .
```

### 2. Deploy to Kubernetes

Apply all manifests:

```bash
kubectl apply -f k8s-manifests/
```

This will deploy:
- API, Frontend, Worker, Redis as pods
- Services for API, Frontend (LoadBalancer), Redis

**Frontend** is exposed via LoadBalancer. Access the app at the public URL after deployment.

---

### 3. Local Development

You can run each component locally:

```bash
cd API && python app.py
cd Frontend && python app.py
cd Worker && python worker.py
```

---

## Requirements

- Docker
- Kubernetes (minikube, kind, or cloud cluster)
- Python 3.x
- Redis

---

## Environment Variables

- `REDIS_HOST`: Hostname for Redis (default: `localhost` or `redis-service` in k8s)
- `API_URL`: API endpoint for Frontend (default: `http://localhost:5000` or `http://api-service:5000` in k8s)

---

## Cloud & Production Notes

- Update image repositories in manifests for your registry
- Use Helm for advanced configuration and upgrades
- Secure environment variables and secrets for production

---

## License

MIT — For educational use
