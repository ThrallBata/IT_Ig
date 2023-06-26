FROM python:3.11

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt

CMD python3 manage.py migrate
CMD python3 manage.py runserver 0.0.0.0:8000