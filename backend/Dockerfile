FROM python:3.11

RUN mkdir /ites_app

WORKDIR /ites_app

COPY . .

RUN pip install -r requirements.txt

RUN chmod a+x docker/*.sh