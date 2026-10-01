# Week 12 - MLOps

## W12D1: MLOps Overview — CI/CD for ML Systems

This week introduces an MLOps workflow for a machine learning API.

### Components

- FastAPI ML prediction API
- Scikit-learn LinearRegression model
- Docker containerisation
- GitHub Actions CI/CD
- GitHub Container Registry
- Automated linting
- Automated testing
- Monitoring and retraining strategy

### CI/CD Pipeline

Code
→ Lint
→ Test
→ Docker Build
→ Docker Image Push

### Day 1 Folder

`day1-mlops-cicd/`

The API exposes:

- `GET /`
- `GET /health`
- `POST /predict`

The Docker image can be built locally and the same container build is
automated through GitHub Actions.

### Local Verification

- Ruff linting passed
- Pytest: 3 tests passed
- Docker image built successfully
- Docker container ran successfully
- `/health` returned a healthy status
- `/predict` returned a prediction

### Monitoring

The monitoring and retraining strategy is documented in:

`day1-mlops-cicd/monitoring.md`