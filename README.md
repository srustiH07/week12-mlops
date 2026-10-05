# Week 12 - MLOps

This repository contains the Week 12 MLOps internship tasks completed using Docker, FastAPI, GitHub Actions, and production monitoring practices.

## Technology Stack

* Python 3.12
* FastAPI
* Scikit-learn
* Docker
* GitHub Actions
* GitHub Container Registry
* Ruff
* Pytest
* MLflow concepts for model tracking and retraining

---

# W12D1 - MLOps CI/CD

## Objective

Build and containerise a machine learning API and implement a CI/CD workflow for automated linting, testing, Docker image building, and registry publishing.

## Implementation

The W12D1 application uses FastAPI with a Linear Regression model.

Directory:

```text
day1-mlops-cicd/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── test_app.py
└── monitoring.md
```

## CI/CD

The W12D1 GitHub Actions workflow is located at:

```text
.github/workflows/ci.yml
```

The pipeline performs:

```text
Lint
  ↓
Test
  ↓
Build Docker Image
  ↓
Push Image to GitHub Container Registry
```

## Monitoring

The W12D1 monitoring documentation covers:

* API health
* Request and error monitoring
* CPU and memory usage
* Container health
* Model performance
* Data drift
* Retraining conditions

---

# W12D2 - Containerising ML Apps - Docker for AI

## Objective

Containerise a machine learning API using Docker, implement a CI/CD pipeline, and document a production monitoring strategy.

## Implementation

The W12D2 application uses FastAPI with a RandomForestClassifier trained on the Iris dataset.

Directory:

```text
day2-docker-ai/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── test_app.py
└── monitoring.md
```

## Local Docker Build

Docker image:

```text
w12d2-docker-ai:1.0
```

Container:

```text
w12d2-docker-ai-container
```

Port mapping:

```text
localhost:8001 -> container:8000
```

## API Verification

Health endpoint:

```text
status: healthy
model: RandomForestClassifier
```

Prediction endpoint:

```text
prediction: 0
class_name: setosa
```

## Local Testing

Ruff validation:

```text
All checks passed!
```

Pytest validation:

```text
3 passed
```

## CI/CD

The W12D2 workflow is:

```text
.github/workflows/w12d2-ci.yml
```

Pipeline:

```text
Lint
  ↓
Test
  ↓
Build Docker Image
  ↓
Push to GitHub Container Registry
```

Registry image:

```text
ghcr.io/srustih07/week12-mlops:w12d2-latest
```

## Monitoring

The W12D2 monitoring strategy is documented in:

```text
day2-docker-ai/monitoring.md
```

It covers:

* API and system metrics
* Machine learning metrics
* MLOps metrics
* Alerts
* Retraining triggers
* Monitoring workflow
* Model retraining process

---

# W12D3 - Monitoring ML Models in Production

## Objective

Containerise an ML API, implement a CI/CD workflow, and document a production monitoring and model retraining strategy.

## Implementation

The W12D3 task uses a FastAPI application with a RandomForestClassifier trained on the Iris dataset.

Directory:

```text
day3-monitoring-ml-models/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── test_app.py
└── monitoring.md
```

## Local Docker Build

Docker image:

```text
w12d3-monitoring-ml:1.0
```

Container:

```text
w12d3-monitoring-ml-container
```

Port mapping:

```text
localhost:8002 -> container:8000
```

## Docker Verification

The container starts successfully and runs Uvicorn on port 8000.

Health endpoint result:

```text
status: healthy
model: RandomForestClassifier
```

Prediction endpoint result:

```text
prediction: 0
class_name: setosa
```

## Code Quality and Testing

Ruff validation:

```text
All checks passed!
```

Pytest validation:

```text
3 passed
```

The tests verify:

1. Root endpoint availability.
2. Health endpoint response.
3. Iris prediction endpoint.

## CI/CD

The W12D3 GitHub Actions workflow is:

```text
.github/workflows/w12d3-monitoring-ci.yml
```

The workflow implements:

```text
Lint
  ↓
Test
  ↓
Build Docker Image
  ↓
Push to GitHub Container Registry
```

The workflow uses GitHub Actions to automatically validate the application and publish the Docker image.

Registry image:

```text
ghcr.io/srustih07/week12-mlops:w12d3-latest
```

## Monitoring Strategy

The monitoring strategy is documented in:

```text
day3-monitoring-ml-models/monitoring.md
```

The strategy covers:

* API request count
* API response latency
* Error rate
* HTTP status codes
* CPU usage
* Memory usage
* Container restarts
* Health-check failures
* Prediction class distribution
* Prediction confidence
* Input feature distributions
* Data drift
* Model accuracy
* Precision
* Recall
* F1-score
* Model version
* Docker image version
* Dataset version
* Deployment version

## Alerts

Production alerts should be configured for:

* Error rate above 5% for five consecutive minutes.
* p95 API latency above one second.
* Health-check failures.
* CPU or memory usage above 80% for a sustained period.
* Unexpected container restarts.
* Significant input data drift.
* Model F1-score dropping more than 10% from the production baseline.

## Retraining Triggers

Model retraining should be considered when:

1. Data drift remains above the accepted threshold.
2. Model F1-score falls below the production baseline.
3. New labelled training data becomes available.
4. Prediction-class distribution changes significantly.
5. Concept drift is detected.
6. Scheduled model review identifies performance degradation.

## Monitoring and Retraining Workflow

```text
Incoming Requests
        |
        v
API and Container Monitoring
        |
        +----> Latency / Errors / CPU / Memory
        |
        v
ML Prediction Monitoring
        |
        +----> Prediction Distribution
        +----> Input Data Drift
        +----> Model Performance
        |
        v
Threshold Check
        |
   +----+----+
   |         |
Normal    Threshold Exceeded
   |         |
   v         v
Continue   Alert
             |
             v
        Investigate
             |
             v
       Retrain Model
             |
             v
       Evaluate Model
             |
             v
      Track with MLflow
             |
             v
      Build Docker Image
             |
             v
        CI/CD Deploy
             |
             v
        Monitor Again
```

## Retraining Process

When a retraining trigger occurs:

1. Collect new production data.
2. Validate data quality.
3. Check for data and concept drift.
4. Retrain the machine learning model.
5. Evaluate the new model against the production baseline.
6. Track the experiment and model using MLflow.
7. Approve the model if performance requirements are satisfied.
8. Build a new Docker image.
9. Run CI/CD checks.
10. Deploy the updated model.
11. Continue monitoring the new model version.

## W12D3 Result

The W12D3 implementation successfully demonstrates:

* ML API containerisation using Docker.
* Local Docker image creation.
* Local Docker container execution.
* FastAPI health monitoring.
* ML prediction verification.
* Automated linting with Ruff.
* Automated testing with Pytest.
* GitHub Actions CI/CD.
* Docker image publishing to GitHub Container Registry.
* Production monitoring planning.
* Model retraining triggers.
* MLflow-based model tracking as part of the MLOps workflow.

---

# Week 12 Summary

Week 12 demonstrates an end-to-end MLOps workflow:

```text
Machine Learning Model
        ↓
FastAPI Application
        ↓
Automated Testing
        ↓
Docker Container
        ↓
GitHub Actions CI/CD
        ↓
GitHub Container Registry
        ↓
Production Monitoring
        ↓
Drift / Performance Detection
        ↓
Model Retraining
        ↓
MLflow Tracking
        ↓
New Docker Image
        ↓
CI/CD Deployment
```

The three daily tasks are maintained inside the same Week 12 repository:

```text
week12-mlops/
├── README.md
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── w12d2-ci.yml
│       └── w12d3-monitoring-ci.yml
├── day1-mlops-cicd/
├── day2-docker-ai/
└── day3-monitoring-ml-models/
```
