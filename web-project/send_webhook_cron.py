#!/usr/bin/python
from discord_webhook import DiscordWebhook
import os


webhook = DiscordWebhook(url='$WEBHOOOKURL', content="", rate_limit_retry=True)
with open('calculator/static/json/requetes.json','r', encoding='utf-8') as f:
	webhook.add_file(file=f.read(), filename='requetes.json')
response = webhook.execute()

try:
	os.system("python -Xutf8 /app/manage.py dumpdata > data.json")
	check = DiscordWebhook(url='$WEBHOOOKURL', content="Database has been dumped in data.json", rate_limit_retry=True)
	response = check.execute()
except:
	pass