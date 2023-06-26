FROM python:3.11

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt

RUN python3 manage.py migrate

RUN python3 manage.py createsuperuser
RUN admin
RUN vwfwf@g.com
RUN 14bujhm14
RUN 14bujhm14
CMD python3 manage.py runserver 0.0.0.0:8000
