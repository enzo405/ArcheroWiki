#!/usr/bin/python
from discord_webhook import DiscordWebhook, DiscordWebhook, DiscordEmbed
from const import WEBHOOK_URL, ADMIN_CREDENTIAL
import os, json, re, sys
import hashlib


def clearFile():
	with open('calculator/static/json/requetes.json', "w") as f:
		data_init = {"user": []}
		json.dump(data_init, f)
		f.close()


class sendWebhook():
	def __init__(self) -> None:
		self.webhook = DiscordWebhook(url=WEBHOOK_URL, content="", rate_limit_retry=True)

	def execute(self):
		response = self.webhook.execute()
		return response
	
	def message(self,msg):
		self.webhook = DiscordWebhook(url=WEBHOOK_URL, content=msg, rate_limit_retry=True)
		self.webhook.execute()

	def sendRequestFile(self):
		webhook = self.webhook
		with open('calculator/static/json/requetes.json','r', encoding='utf-8') as f:
			user = DiscordEmbed(title='Number Request', description='', color='1ed9be')
			for i in json.load(f)['user']:
				user.add_embed_field(name=f"{i['username']} | {i['ingame_id']} = {i['number_request']}", value=f"", inline=False)
			webhook.add_embed(user)
		clearFile()

	def database_dump(self):
		webhook = self.webhook
		os.system("python -Xutf8 manage.py dumpdata > database_dump.json")
		with open('database_dump.json','r', encoding='utf-8') as f:
			webhook.add_file(file=f.read(), filename='database_dump.json')
	
	def local_api_dump(self):
		webhook = self.webhook
		with open('calculator/local_data.json','r', encoding='utf-8') as f:
			webhook.add_file(file=f.read(), filename='local_data.json')


webhook = sendWebhook()
try:
	if __name__ == '__main__':
		if sys.argv[1] == 'db_dump':
			webhook.database_dump()
			webhook.execute()
		elif sys.argv[1] == 'req':
			webhook.sendRequestFile()
			webhook.execute()
		elif sys.argv[1] == 'api':
			webhook.local_api_dump()
			webhook.execute()
		elif sys.argv[1] == 'all':
			webhook.database_dump()
			webhook.sendRequestFile()
			webhook.local_api_dump()
			webhook.execute()
		else:
			print('Erreur: commande inconnue')
except:
	webhook.database_dump()
	webhook.sendRequestFile()
	webhook.local_api_dump()
	webhook.execute()