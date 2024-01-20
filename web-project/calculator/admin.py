from django.contrib import admin
from calculator.models import *
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .function import send_webhook

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
	# to have a date-based drilldown navigation in the admin page
	date_hierarchy = 'action_time'

	# to filter the resultes by users, content types and action flags
	list_filter = [
		'user',
		'content_type',
		'action_flag'
	]

	# when searching the user will be able to search in both object_repr and change_message
	search_fields = [
		'object_repr',
		'change_message'
	]

	list_display = [
		'action_time',
		'user',
		'content_type',
		'action_flag',
	]


def group(model:models.Model):
	# Register the model to the admin panel
	admin.site.register(model)
	# Create customized group to be able to edit the model when needed
	content_type = ContentType.objects.get_for_model(model)
	# Check if the permissions already exist
	view_permission, view_created = Permission.objects.get_or_create(codename=f'view_{model.__name__.lower()}',content_type=content_type,defaults={'name': f'Can View {model.__name__}'})
	add_permission, add_created = Permission.objects.get_or_create(codename=f'add_{model.__name__.lower()}',content_type=content_type,defaults={'name': f'Can Add {model.__name__}'})
	change_permission, change_created = Permission.objects.get_or_create(codename=f'change_{model.__name__.lower()}',content_type=content_type,defaults={'name': f'Can Change {model.__name__}'})
	group_name = f'{model.__name__}Editor'
	custom_group, created = Group.objects.get_or_create(name=group_name)
	custom_group.permissions.add(view_permission, add_permission, change_permission)

try:
	group(ServerManagement)
	group(user)
	group(StuffTable)
	group(HeroTable)
	group(TalentTable)
	group(SkinTable)
	group(AltarTable)
	group(JewelTypeTable)
	group(JewelLevelTable)
	group(EggTable)
	group(EggEquippedTable)
	group(DragonTable)
	group(RunesTable)
	group(ReforgeTable)
	group(RefineTable)
	group(DamageCalcTable)
	group(MedalsTable)
	group(RelicsTable)
	group(WeaponSkinsTable)
	group(PromoCode)
	group(Contributor)
	group(ArticleMenu)
	group(PromoCodeReward)
	group(GoogleSheet)
	group(TheorycraftingArticle)
except Exception as e:
	send_webhook(f"Admin panel initialization failed : {e}", admin_log=True)