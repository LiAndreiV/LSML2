from celery import Celery
from celery.result import AsyncResult
from flask import Flask, render_template, request, url_for, redirect
import time

celery_app = Celery('tasks', backend='redis://redis', broker='redis://redis')
app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def sentiment():
    input_text = request.form['data']
    task = celery_app.send_task('tasks.predict', [input_text])
    return redirect(url_for("get_predict", task_id=task.id))


@app.route('/predict/<task_id>', methods=['GET'])
def get_predict(task_id):
    task = AsyncResult(task_id, app=celery_app)
    while not task.ready():
        time.sleep(2.0)
    prediction = 'Positive' if task.result == 1 else "Negative"
    return render_template('index.html', prediction=prediction)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
