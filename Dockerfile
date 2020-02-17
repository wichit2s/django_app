FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /mysite
WORKDIR /mysite
ADD requirements.txt /mysite/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /mysite/
