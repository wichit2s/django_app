FROM python:3.8-buster
ENV PYTHONUNBUFFERED 1
RUN mkdir /mysite
WORKDIR /mysite
ADD requirements.txt /mysite/
RUN pip install -r requirements.txt
ADD . /mysite/
