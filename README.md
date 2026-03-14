# Container Technology Project

This project demonstrates a microservices-based deployment using Docker and Kubernetes. It consists of three main components: API, Frontend, and Worker, along with Redis for caching and message brokering. All services are containerized and orchestrated via Kubernetes manifests.

## Project Structure

```
API/
  app.py
  Dockerfile
Frontend/
  app.py
  Dockerfile
Worker/
  worker.py
  Dockerfile
  requirements.txt
k8s-manifests/
  api-deployment.yaml
  api-service.yaml
  frontend-deployment.yaml
  frontend-service.yaml
  redis-deployment.yaml
  redis-service.yaml
  worker-deployment.yaml
docs/
```

## Components

- **API**: Backend service (Python) providing core business logic.
- **Frontend**: Web interface (Python, likely Flask or Streamlit).
- **Worker**: Background processing service (Python).
- **Redis**: Used for caching and as a message broker.

## Deployment Instructions

### 1. Build Docker Images

Navigate to each service directory and build the Docker images:

```
cd API
# Build API image
docker build -t api-service .

cd ../Frontend
# Build Frontend image
docker build -t frontend-service .

cd ../Worker
# Build Worker image
docker build -t worker-service .
```

### 2. Kubernetes Deployment

Apply the Kubernetes manifests from the `k8s-manifests` directory:

```
kubectl apply -f k8s-manifests/
```

This will deploy:
- API, Frontend, Worker, and Redis as separate pods
- Services for API, Frontend, Redis

### 3. Accessing the Services

- **Frontend**: Exposed via a Kubernetes service. Use `kubectl get svc` to find the external IP/port.
- **API**: Accessible via its service.
- **Worker**: Runs as a background job, not directly exposed.
- **Redis**: Internal service for API and Worker communication.

### 4. Local Development

You can run each component locally for development:

```
# Example for API
cd API
python app.py

# Example for Frontend
cd Frontend
python app.py

# Example for Worker
cd Worker
python worker.py
```

## Requirements

- Docker
- Kubernetes (minikube, kind, or local cluster)
- Python 3.x
- Redis

## Notes

- All manifests are designed for local development. For cloud deployment, update image repositories and service types as needed.
- Make sure to configure environment variables and secrets securely for production.

## License

This project is for educational purposes.
