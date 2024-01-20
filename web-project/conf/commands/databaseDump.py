#!/usr/bin/conf/python
from discord_webhook import DiscordWebhook, DiscordWebhook
from conf.conf import ADMIN_LOG_WEBHOOK_URL
import os

current_directory = os.getcwd()

class SendWebhook():
	def __init__(self) -> None:
		self.webhook = DiscordWebhook(url=ADMIN_LOG_WEBHOOK_URL, content="", rate_limit_retry=True)

	def execute(self):
		response = self.webhook.execute()
		return response

	def database_dump(self):
		webhook = self.webhook
		os.system(f"python -Xutf8 /app/manage.py dumpdata > /app/conf/database/database_dump.json")
		with open(f'/app/conf/database/database_dump.json','r', encoding='utf-8') as f:
			webhook.add_file(file=f.read(), filename='database_dump.json')


webhook = SendWebhook()
if __name__ == '__main__':
	webhook.database_dump()
	webhook.execute()