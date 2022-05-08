import mlflow
from sklearn.linear_model import LogisticRegression

MLFLOW_SERVER_URL = 'http://127.0.0.1:5000/'
mlflow.set_tracking_uri(MLFLOW_SERVER_URL)

c, max_iter = 10, 100
with mlflow.start_run() as run:
      lr = LogisticRegression(C=c, max_iter=max_iter)
      mlflow.log_param("c", c)
      mlflow.log_param("max_iter", max_iter)
      # Log the sklearn model and register as version 1
      mlflow.sklearn.log_model(
            sk_model=lr,
            artifact_path="/opt/mlflow/artifactStore",
            registered_model_name="sentiment-model"
      )