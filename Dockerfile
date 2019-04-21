FROM python:3.6.8-stretch

WORKDIR /usr/src/app

ADD . /usr/src/app

RUN apt-get update
RUN pip install numpy
RUN pip install --no-cache-dir -r requirements.txt


ENTRYPOINT ["python"]

CMD ["app.py"]