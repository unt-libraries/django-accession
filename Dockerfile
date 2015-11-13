FROM python:2.7

ENV PYTHONPATH=/app

ADD requirements.txt /requirements.txt
ADD requirements /requirements
RUN pip install -r /requirements.txt
CMD python ./manage.py migrate --noinput && \
    python manage.py runserver 0.0.0.0:80

RUN mkdir /app
WORKDIR /app
