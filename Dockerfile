FROM python:3.11-slim

WORKDIR /to-do-flaskrestx-microservice

COPY requirements.txt /to-do-flaskrestx-microservice/

RUN pip install -r requirements.txt

COPY . /to-do-flaskrestx-microservice/

EXPOSE 5000

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]