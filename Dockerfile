FROM tiangolo/meinheld-gunicorn-flask:python3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONFAULTHANDLER 1 

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0


COPY requirements.txt requirements.txt
COPY gunicorn_conf.py /gunicorn_conf.py

RUN pip3 install -r requirements.txt

EXPOSE 5000
COPY . .

CMD ["flask", "run"]