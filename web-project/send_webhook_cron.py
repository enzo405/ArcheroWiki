#!/usr/bin/python
from discord_webhook import DiscordWebhook, DiscordWebhook, DiscordEmbed
from const import WEBHOOK_URL, ADMIN_CREDENTIAL
import os, json, re, sys
import hashlib



class sendWebhook():
	def __init__(self) -> None:
		self.webhook = DiscordWebhook(url=WEBHOOK_URL, content="", rate_limit_retry=True)

	def execute(self):
		response = self.webhook.execute()
		return response
	
	def message(self,msg):
		self.webhook = DiscordWebhook(url=WEBHOOK_URL, content=msg, rate_limit_retry=True)
		self.webhook.execute()

	def database_dump(self):
		webhook = self.webhook
		os.system("python -Xutf8 manage.py dumpdata > database_dump.json")
		with open('database_dump.json','r', encoding='utf-8') as f:
			webhook.add_file(file=f.read(), filename='database_dump.json')


webhook = sendWebhook()
if __name__ == '__main__':
	webhook.database_dump()
	webhook.execute()