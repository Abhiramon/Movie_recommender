FROM python:3.6.8-stretch

WORKDIR /usr/src/app

ADD . .

RUN pip install numpy
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["python","app.py"]