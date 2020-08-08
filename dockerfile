FROM python:3.8

ADD . /tmp

RUN pip install flask pymongo

CMD python /tmp/app.py