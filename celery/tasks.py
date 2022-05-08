import numpy as np
from celery import Celery
import transformers as ppb
import mlflow
import torch
import mlflow.pytorch

celery_app = Celery('tasks', backend='redis://redis', broker='redis://redis')

MLFLOW_SERVER_URL = 'http://127.0.0.1:5000/'
client = mlflow.tracking.MlflowClient(MLFLOW_SERVER_URL)

# get model
model_name = 'sentiment-model'
models = client.search_registered_models(f'name={model_name}')
model = mlflow.pytorch.load_model(model_uri=f'models:/{model_name}/{models[0].latest_versions[0].version}')


@celery_app.task(name='tasks.predict')
def predict(data):
    text = embedding_bert(data)
    prediction = model.predict(text)
    return prediction


def embedding_bert(text):
    model_class = ppb.DistilBertModel
    tokenizer_class = ppb.DistilBertTokenizer
    pretrained_weights = 'distilbert-base-uncased'
    tokenizer = tokenizer_class.from_pretrained(pretrained_weights)
    sk_model = model_class.from_pretrained(pretrained_weights)
    tokenized = tokenizer.encode(text, add_special_tokens=True)
    padded = np.array([tokenized])
    attention_mask = np.where(padded != 0, 1, 0)
    input_ids = torch.tensor(padded)
    attention_mask = torch.tensor(attention_mask)

    with torch.no_grad():
        last_hidden_states = sk_model(input_ids, attention_mask=attention_mask)

    x = last_hidden_states[0][:, 0, :].numpy()

    return x
