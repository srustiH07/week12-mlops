# W12D5 Monitoring Strategy - 3M Capstone Production AI System

## 1. Overview

The W12D5 capstone application is a production-style containerised FastAPI machine learning API using a RandomForestClassifier for Iris flower classification.

The monitoring strategy covers API reliability, infrastructure health, machine learning performance, data quality, and retraining conditions.

## 2. What to Track

### API Metrics

- Request count
- Response latency
- Error rate
- HTTP status codes
- Health-check failures
- Request throughput

### Infrastructure Metrics

- CPU usage
- Memory usage
- Container restarts
- Container health
- Docker image version
- Deployment status

### ML Model Metrics

- Prediction distribution
- Prediction confidence
- Accuracy
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

Production alerts should be configured for:

- Error rate above 5% for five consecutive minutes.
- p95 API latency above one second.
- Health-check failures.
- CPU or memory usage above 80% for a sustained period.
- Unexpected container restarts.
- Significant input data drift.
- F1-score dropping more than 10% from the production baseline.
- Unexpected changes in prediction distribution.

## 4. Retraining Triggers

The model should be considered for retraining when:

1. Data drift remains above the accepted threshold.
2. Model F1-score falls below the production baseline.
3. New labelled production data becomes available.
4. Prediction distribution changes significantly.
5. Concept drift is detected.
6. Scheduled evaluation identifies model degradation.

## 5. Full Production Pipeline

```text
Incoming Request
       |
       v
FastAPI ML API
       |
       v
Docker Container
       |
       +----> API Monitoring
       +----> Infrastructure Monitoring
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
       Track with
         MLflow
           |
           v
      Build Docker
         Image
           |
           v
       CI/CD Tests
           |
           v
        Deploy
           |
           v
     Monitor Again