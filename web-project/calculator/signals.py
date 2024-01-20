from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.admin.models import LogEntry
from app.settings import c_hostname, WEBHOOK_URL, DEV_MODE
from discord_webhook import DiscordWebhook, DiscordEmbed
from .function import checkDbMaintenance

@receiver(post_save, sender=LogEntry)
def handle_new_log_entry(sender, instance, created, **kwargs):
	if DEV_MODE:
		return
	if checkDbMaintenance() and not created:
		return
	user = instance.user.username if instance.user else "Unknown User"
	if user != "Unknown User":
		action_time_timestamp = int(instance.action_time.timestamp())
		content_type = instance.content_type.model.capitalize()
		action_flag = instance.get_action_flag_display()

		try:
			content_object = instance.content_type.get_object_for_this_type(pk=instance.object_id)
			app_label = content_object._meta.app_label
			model_name = content_object._meta.model_name
			content_object_link = reverse(
				f"admin:{app_label}_{model_name}_change",
				args=[content_object.pk]
			)
			object_link = f"[{content_object}]({c_hostname}{content_object_link})"
		except Exception as e:
			object_link = "Object link not available"
		
		message = (
			f"- Created at : <t:{action_time_timestamp}:f>\n"
			f"- Action: {action_flag}\n"
			f"- {object_link}\n"
		)

		avatar_url = f"{c_hostname}/static/image/favicon.png"
		webhook = DiscordWebhook(url=WEBHOOK_URL, content="", rate_limit_retry=True)
		embed = DiscordEmbed(title="A new LogEntry was created:", description="", color="F1C232")
		embed.set_author(name=user,icon_url=avatar_url)
		embed.add_embed_field(name=f"Object: {content_type} {instance.object_id}", value=str(message), inline=False)
		webhook.add_embed(embed)
		try:
			webhook.execute()
		except:
			pass