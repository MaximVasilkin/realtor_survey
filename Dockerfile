FROM python:3.10-alpine


RUN apk update && apk add curl

RUN adduser -D myuser
WORKDIR /home/myuser/project
COPY ../requirements.txt ./web_app ./
RUN pip install -r requirements.txt
RUN python3 manage.py collectstatic --noinput
RUN chown -R myuser:myuser /home/myuser/project

USER myuser

EXPOSE 8000

CMD python3 manage.py makemigrations && \
    python3 manage.py migrate --run-syncdb && \
    gunicorn --workers 1 employe.wsgi -b 0.0.0.0:8000
