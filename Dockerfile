FROM ubuntu:latest

RUN apt update && apt install -y python3-pip

WORKDIR /etc/happyalya/

COPY . /etc/happyalya/

RUN pip3 install -r requirements.txt

ENV FLASK_APP=main.py
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
EXPOSE 5000
CMD flask run --host=0.0.0.0
