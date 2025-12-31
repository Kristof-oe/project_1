## Project overview
This projects demonstrates end-to-end DevOps workflow built around FastApi backend service. This main goal is automated build, test and deployment process using Github Actions, Docker, Helm and Kubernetes

This app itself is simple focusing on CI/CD pipeline and infrastructure automation

- **FastApi** - Backend REST API
- **Gihub Actions** - CI/CD orchestration
- **Docker** - Application containerization
- **Helm** - Kubernetes package management
- **Kubernetes (kind)** – Local Kubernetes cluster for deployment and testing

Github Push --> Github Actions
- **Build**
    -  Run Python unit test (pytest) 
    -  Build Docker image
    -  Test Docker image locally (smoke test)
    -  Push image to Docker Hub
- **Deploy**
    - Deploy to Kubernetes via Helm
    - Test via /health endpoint (smoke test)

