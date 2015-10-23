FROM python:2.7

ENV PYTHONPATH=/app
RUN apt-get update -qq
RUN apt-get install mysql-client -qq

ADD requirements.txt /requirements.txt
ADD requirements /requirements
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
