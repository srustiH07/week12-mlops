# W12D1 Monitoring and Retraining Strategy

## 1. Monitoring Objectives

The ML API should be monitored for system reliability, application performance,
data quality, model behaviour, and prediction quality.

## 2. Metrics to Track

### API and System Metrics

- Request count and throughput
- HTTP error rate
- Response latency: p50, p95, and p99
- CPU utilisation
- Memory utilisation
- Container restarts
- API health-check status

### ML Model Metrics

- Prediction distribution
- Input feature distribution
- Missing or invalid input values
- Data drift
- Prediction drift
- Model accuracy or error metrics when ground-truth labels become available

### MLOps Metrics

- Model version
- Deployment version
- Training dataset version
- Experiment/run information
- Number of retraining events

MLflow can be used to track experiments, model versions, parameters, metrics,
and deployment-related metadata.

## 3. Alerts

Example alert conditions:

- HTTP error rate above 5% for 5 consecutive minutes
- p95 API latency above 1 second for 5 consecutive minutes
- Health check fails repeatedly
- CPU or memory usage remains above 80%
- Significant data or prediction drift is detected
- Model performance falls more than 10% below the established baseline

Alert thresholds should be adjusted according to the production workload.

## 4. Retraining Triggers

The model should be considered for retraining when:

1. Data drift remains above the accepted threshold.
2. Model performance drops below the agreed baseline.
3. A significant amount of newly labelled data becomes available.
4. Concept drift is detected.
5. A scheduled model review determines that retraining is required.

## 5. Retraining Workflow

A recommended workflow is:

Data collection
→ Data validation
→ Drift/performance check
→ Model retraining
→ Model evaluation
→ MLflow experiment tracking
→ Model approval
→ Docker image build
→ CI/CD deployment
→ Production monitoring

## 6. Incident Response

If the API becomes unhealthy or model quality degrades:

1. Confirm the alert and inspect logs.
2. Check API and container health.
3. Check recent model and data changes.
4. Roll back to the previous validated model/image if necessary.
5. Investigate the root cause.
6. Retrain and validate the model when required.
7. Redeploy only after successful testing.