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
## W12D2: Containerising ML Apps - Docker for AI

W12D2 extends the MLOps workflow by containerising a separate machine
learning API and adding a dedicated CI/CD workflow.

### Components

- FastAPI ML prediction API
- Scikit-learn RandomForestClassifier
- Iris classification dataset
- Docker containerisation
- GitHub Actions CI/CD
- GitHub Container Registry
- Automated Ruff linting
- Automated Pytest testing
- ML API and model monitoring strategy

### Day 2 Folder

`day2-docker-ai/`

The API exposes:

- `GET /`
- `GET /health`
- `POST /predict`

### Docker Image

Local image:

`w12d2-docker-ai:1.0`

The container maps:

`localhost:8001 -> container:8000`

### Local Verification

- Ruff linting passed
- Pytest: 3 tests passed
- Docker image built successfully
- Docker container ran successfully
- `/health` returned `healthy`
- `/predict` returned Iris class `setosa`

### W12D2 CI/CD Pipeline

Code
→ Lint
→ Test
→ Docker Build
→ Docker Image Push

The dedicated GitHub Actions workflow is:

`.github/workflows/w12d2-ci.yml`

The Docker image is published to GitHub Container Registry as:

`ghcr.io/srustih07/week12-mlops:w12d2-latest`

### Monitoring

The W12D2 monitoring and retraining strategy is documented in:

`day2-docker-ai/monitoring.md`