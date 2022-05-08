# ML-service to solve Sentiment Analysis

## Dataset 
The data is tweet messages with a sentimental score.
http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip

## Jupyter
With the help of Google Colab, the initial data was processed, vectorized with the help of Burt (the following tutorial was used https://jalammar.github.io/a-visual-guide-to-using-bert-for-the-first-time/) and the semantic score was predicted using logistic regression. The rmse, mae, r2 metrics were calculated for different parameters. The experiment was registered in MLFlow.

## Flask
http server with connected to Celery via port 8000 (app conteiner)


## Celery
asynchronous task processing; connected to Flask (port 8000) and MLFlow (port 5000)(celery conteiner)
In file model.py is registered best parameters Logistic Regression c = 10, max_iter = 100 in MLFlow.


## Redis
stores Celery data (redis conteiner)

## MLFlow
track model training (mlflow conteiner)

## DB
Database server for mlflow (db conteiner)


## Build project

To run the whole application, execute the following commands from the project directory: 
 
 ```
 docker-compose up --build
 ```
 
 Then enter in your web browser:  `http://localhost:9091/`

<p align="center">
  <img src="predict.png" width="1500" title="example">
</p>
