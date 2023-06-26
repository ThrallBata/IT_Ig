FROM python:3.11

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

CMD python3 manage.py createsuperuser --username=admin --email=admin@example.com
CMD 14bujhm14
CMD 14bujhm14
CMD python3 manage.py runserver 0.0.0.0:8000
