## 🎥 Fashion Survival Guide

A simple Kubernetes-deployed web app that helps users stay updated with fashion trends. Powered by **FastAPI** for the backend and **NGINX** for the frontend.

### 📦 Features

* ✨ FastAPI backend exposing a fashion trends API
* 🖼️ Static HTML frontend served with NGINX
* 🐳 Docker Compose for local development
* ☸️ Kubernetes manifests for production-like deployments via Minikube
* 📊 Monitoring with Prometheus and Grafana
* 🔁 Health checks and resource limits in Kubernetes

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

Requirements:

* Docker
* Docker Compose

Run Locally:
```bash
docker-compose up --build
```

Access:

* Frontend: [http://localhost:80](http://localhost)
* Backend: [http://localhost:8001](http://localhost:8001)

---

#### ☘️ Kubernetes Deployment (via Minikube)

Prerequisites:

* Minikube
* kubectl

Deploy:

```bash
# Start Minikube
minikube start

# Apply Kubernetes configs
kubectl apply -f fashion-app.yaml

# Access the app
minikube service fashion-nginx-service
```

---
### 📊 Monitoring with Prometheus & Grafana

#### 📦 Install Monitoring Stack

Prerequisites:

* Helm
  
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

helm install prometheus prometheus-community/kube-prometheus-stack
```

#### 📈 Access Grafana
```bash
kubectl port-forward svc/prometheus-grafana 3000:80
```
Visit [http://localhost:3000](http://localhost:3000)

* **Username:** `admin`
* **Password:** `prom-operator`

---

### 🧪 API Endpoints

Base URL: `/api/`

* `GET /` → Welcome message
* `GET /steps` → Fashion guide steps
* `GET /news` → Fashion news sources
* `GET /brands` → Popular brands
* `GET /communities` → Online communities

---

### 🐳 Docker Images

* **Backend:** `s1mphonia/fashion-backend`
* **Frontend:** `s1mphonia/fashion-nginx`

---

### 📊 TODO (Next Steps)

* [ ] CI/CD with GitHub Actions
