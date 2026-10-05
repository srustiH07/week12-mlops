# W12D4 Monitoring Strategy - End-to-End MLOps Pipeline Review

## 1. Overview

The W12D4 application is a containerised FastAPI machine learning API using a RandomForestClassifier for Iris flower classification.

The monitoring strategy covers infrastructure health, API performance, machine learning behaviour, data quality, and model retraining.

## 2. What to Track

### API Metrics

- Request count
- Response latency
- Error rate
- HTTP status codes
- Health-check failures

### Infrastructure Metrics

- CPU usage
- Memory usage
- Container restarts
- Container health
- Docker image version

### ML Model Metrics

- Prediction distribution
- Prediction confidence
- Model accuracy
- Precision
- Recall
- F1-score
- Confusion matrix
- Model version

### Data Metrics

- Input feature distributions
- Missing values
- Invalid inputs
- Data drift
- Concept drift
- Dataset version

## 3. Alerts

The following production alerts should be configured:

- Error rate above 5% for five consecutive minutes.
- p95 latency above one second.
- Health-check failures.
- CPU or memory usage above 80% for a sustained period.
- Unexpected container restarts.
- Significant input data drift.
- F1-score drops more than 10% from the production baseline.

## 4. Retraining Triggers

Retraining should be considered when:

1. Data drift remains above the accepted threshold.
2. Model F1-score falls below the production baseline.
3. New labelled training data becomes available.
4. Prediction distribution changes significantly.
5. Concept drift is detected.
6. Scheduled evaluation identifies model degradation.

## 5. End-to-End Monitoring Workflow

```text
User Request
     |
     v
FastAPI ML API
     |
     v
Docker Container
     |
     +----> API Health
     +----> Latency
     +----> Errors
     +----> CPU / Memory
     |
     v
ML Prediction
     |
     +----> Prediction Distribution
     +----> Model Performance
     +----> Data Drift
     |
     v
Threshold Evaluation
     |
   +---+---+
   |       |
 Normal  Problem
   |       |
   v       v
Continue Alert
           |
           v
      Investigation
           |
           v
    Retrain if Required
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