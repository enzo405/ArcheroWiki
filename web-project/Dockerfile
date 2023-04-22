FROM python:3.10.5

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
COPY send_webhook_cron.py /bin/send_webhook_cron.py
COPY const.py /bin/const.py
COPY root /var/spool/cron/crontabs/root

RUN chmod +x /bin/send_webhook_cron.py
RUN pip install -r requirements.txt
RUN apt update && apt-get install -y cron nano

COPY . /app
WORKDIR /app
EXPOSE 8000
CMD sh start.sh