FROM python:3.8
ADD . /celery
WORKDIR /celery
RUN pip install -r requirements.txt
CMD python /celery/model.py
CMD python /celery/tasks.py
CMD celery -A tasks worker --loglevel=info
