FROM python:3.10.5

RUN pip install --upgrade pip

COPY conf/requirements.txt requirements.txt
ADD conf/db_dump.py /bin/conf/db_dump.py
COPY conf/global_variable.py /bin/conf/global_variable.py
COPY conf/root /var/spool/cron/crontabs/root

RUN chmod +x /bin/conf/db_dump.py
RUN pip install -r requirements.txt
RUN apt update && apt-get install -y cron nano && apt-get install -y gettext

COPY . /app
WORKDIR /app
EXPOSE 8000
CMD sh conf/start.sh