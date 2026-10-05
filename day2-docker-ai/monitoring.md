# W12D2 Monitoring Strategy - Docker AI ML API

## 1. Overview

The W12D2 application is a containerised FastAPI machine learning API that uses a RandomForestClassifier to classify Iris flowers.

The monitoring strategy covers application health, system resources, model behaviour, data quality, and retraining conditions.

## 2. What to Monitor

### API and System Metrics

- Request count
- API response latency
- Error rate
- HTTP status codes
- CPU usage
- Memory usage
- Container restarts
- Health-check failures

### Machine Learning Metrics

- Prediction class distribution
- Prediction confidence
- Input feature distributions
- Data drift
- Model accuracy when labelled data becomes available
- Precision, recall, and F1-score
- Confusion matrix

### MLOps Metrics

- Model version
- Docker image version
- Dataset version
- Deployment version
- Number of retraining runs
- Model evaluation results

## 3. Alerts

The following alerts should be configured:

- Error rate greater than 5% for 5 consecutive minutes.
- p95 API latency greater than 1 second.
- Health-check failures.
- CPU or memory usage above 80% for a sustained period.
- Unexpected increase in container restarts.
- Significant input data drift.
- Model F1-score drops by more than 10% from the baseline.

## 4. Retraining Triggers

The model should be considered for retraining when:

1. Data drift remains above the accepted threshold.
2. Model F1-score falls below the production baseline.
3. New labelled training data becomes available.
4. The distribution of prediction classes changes significantly.
5. Concept drift is detected.
6. A scheduled model review identifies performance degradation.

## 5. Monitoring Workflow

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
## 7. Goal

The objective of this monitoring strategy is to keep the ML API reliable, detect infrastructure and model problems early, and ensure that retraining happens only when measurable conditions indicate that the deployed model needs improvement.