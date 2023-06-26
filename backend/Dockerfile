FROM python:3.11

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN chmod a+x docker/*.sh