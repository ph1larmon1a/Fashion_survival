## 🎥 Fashion Survival Guide

A simple Kubernetes-deployed web app that helps users stay updated with fashion trends. Powered by **FastAPI** for the backend and **NGINX** for the frontend.

### 📦 Tech Stack

* Python 3.11 + FastAPI (Backend API)
* HTML + NGINX (Frontend)
* Docker / Docker Compose (Local Dev)
* Kubernetes (Production Simulation via Minikube)

---

### 📁 Project Structure

```
.
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       ├── main.py
│       └── data.py
├── frontend/
│   ├── Dockerfile
│   ├── index.html
│   └── nginx.conf
├── docker-compose.yml
└── fashion-app.yaml
```

---

### 🚀 Quick Start

#### 🐳 Local Development (Docker Compose)

```bash
docker-compose up --build
```

Access:

* Frontend: [http://localhost:80](http://localhost)
* Backend: [http://localhost:8001](http://localhost:8001)

---

#### ☘️ Kubernetes Deployment (via Minikube)

```bash
# Start Minikube
minikube start

# Apply Kubernetes configs
kubectl apply -f k8s/

# Access the app
minikube service fashion-nginx-service
```

---

### 🧪 API Endpoints

Base URL: `/api/`

* `GET /` → Welcome message
* `GET /steps` → Fashion guide steps
* `GET /news` → Fashion news sources
* `GET /brands` → Popular brands
* `GET /communities` → Online communities

---

### 📊 TODO (Next Steps)

* [ ] Setup Prometheus + Grafana monitoring
* [ ] CI/CD with GitHub Actions
