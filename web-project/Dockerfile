FROM python:3.10.5

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app
EXPOSE 8000
CMD ["gunicorn"  , "--bind", "0.0.0.0:8000", "app:app"]