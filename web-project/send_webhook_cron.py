#!/usr/bin/python
from discord_webhook import DiscordWebhook
import os
import json

def clearFile():
	with open('calculator/static/json/requetes.json', "w") as f:
		data_init = {"user": []}
		json.dump(data_init, f)
		f.close()

webhook = DiscordWebhook(url='WEBHOOK_URL', content="", rate_limit_retry=True)
with open('calculator/static/json/requetes.json','r', encoding='utf-8') as f:
	webhook.add_file(file=f.read(), filename='requetes.json')
response = webhook.execute()
clearFile()

try:
	os.system("python -Xutf8 /app/manage.py dumpdata > data.json")
	webhook = DiscordWebhook(url='WEBHOOK_URL', content="", rate_limit_retry=True)
	with open('data.json','r', encoding='utf-8') as f:
		webhook.add_file(file=f.read(), filename='data.json')
	response = webhook.execute()
except Exception as e:
	exception = DiscordWebhook(url='WEBHOOK_URL', content=e, rate_limit_retry=True)
	response = exception.execute()