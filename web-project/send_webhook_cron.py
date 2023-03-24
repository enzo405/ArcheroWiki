#!/usr/bin/python
from discord_webhook import DiscordWebhook, DiscordWebhook, DiscordEmbed
import os
import json
import re

def checkUsernameCredentials(username,ingame_id):
	pattern = re.compile(r'^\d{1}-\d{6,12}$')
	if (len(username) >= 3 and len(username) < 20 and re.fullmatch(pattern, ingame_id) and ingame_id != "" and ingame_id != None and all(c.isdigit() or c == '-' for c in ingame_id)):
		return True
	else:
		return False

def clearFile():
	with open('calculator/static/json/requetes.json', "w") as f:
		data_init = {"user": []}
		json.dump(data_init, f)
		f.close()


WEBHOOK_URL = "https://discord.com/api/webhooks/#########/#############################################"
webhook = DiscordWebhook(url=WEBHOOK_URL, content="", rate_limit_retry=True)
with open('calculator/static/json/requetes.json','r', encoding='utf-8') as f:
	user = DiscordEmbed(title='Number Request', description='', color='1ed9be')
	suspect = []
	for i in json.load(f)['user']:
		if checkUsernameCredentials(i['username'],i['ingame_id']):
			user.add_embed_field(name=f"{i['username']} | {i['ingame_id']} = {i['number_request']}", value=f"", inline=False)
		else:
			suspect.append(f"{i['username']} | {i['ingame_id']}")
	user.set_footer(text=f'{str(suspect)}', icon_url='')
	webhook.add_embed(user)
clearFile()


os.system("python -Xutf8 manage.py dumpdata > data.json")
with open('data.json','r', encoding='utf-8') as f:
	webhook.add_file(file=f.read(), filename='data.json')


response = webhook.execute()