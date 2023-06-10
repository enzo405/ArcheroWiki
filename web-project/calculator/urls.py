from django.urls import path
from calculator import views
from calculator import api
from calculator import views_wiki
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views_wiki.menu, name='menu'),
    path('Terms-of-Use/', views_wiki.tos, name='tos'),
    path('changelog/', views_wiki.changelog, name='changelog'),
    path('calculator/', views.index_calc, name='calc'),
    path('calculator/show/<str:pbid>/', views.affiche_calc, name='affiche_calc'),
    path('calculator/create/', views.formulaire_calc, name='create_calc'),
    path('calculator/calc/', views.traitement_calc, name='traitement_calc'),
    path('calculator/index/', views.index_calc, name='index_calc'),
    path('calculator/update/<str:pbid>/', views.update_calc, name='update_calc'),
    path('calculator/updatecalc/<str:pbid>/', views.updatetraitement_calc, name='traitement_update_calc'),
    path('calculator/delete/<str:pbid>/', views.delete_user),
    path('calculator/show_debug/<str:pbid>/', api.show_debug, name='show_debug'),
    path('api_view/<str:pbid>/', api.json_payload_profile, name='api_view'),
    path('login/', views_wiki.login, name='login'),
    path('login/processing/<str:username_raw>/<str:id_raw>/', views_wiki.login_processing, name='login_process'),
    path('wiki/maze/', views_wiki.maze, name='maze'),
    path('wiki/menu/', views_wiki.wiki_theorycrafting, name='theorycrafting'),
    path('wiki/item/', views_wiki.item_description, name='item_desc'),
    path('wiki/item/<str:item>/', views_wiki.item_description),
    path('wiki/heroes/', views_wiki.heros_description, name='heroes_desc'),
    path('wiki/heroes/<str:hero>/', views_wiki.heros_description),
    path('wiki/skill-list/', views_wiki.skill_description, name='skill_list'),
    path('wiki/skill-list/<str:skill>/', views_wiki.skill_description),
    path('wiki/damage-calculator/', views_wiki.damage, name='damage_calc'),
    path('wiki/damage-calculator/calc/<str:pbid>/', views_wiki.dmgCalc_processing, name='damage_calc_process'),
    path('wiki/damage-calculator/<str:pbid>/', views_wiki.damageCalc, name='damage_calc_calc'),
    path('wiki/archive/', views_wiki.ghssetGrid, name='archives'),
    path('wiki/upgrade/', views_wiki.upgrade_cost, name='upgrade_cost'),
    path('wiki/upgrade/<str:cost_type>/<int:lvl1>/<int:lvl2>/', views_wiki.upgrade_cost),
    path('wiki/upgrade/<str:cost_type>/<int:lvl1>/<int:lvl2>/<str:rank>/', views_wiki.upgrade_cost),
    path('wiki/promo-code/', views_wiki.promocode, name='promo_code'),
    path('wiki/advanced-stats/', views_wiki.advanced_stats, name='advanced_stats'),
    path('wiki/news/', views_wiki.news, name='news'),
    path('wiki/news/<str:titleArticle>/', views_wiki.news, name='news'),
    path('habby-secret/', views_wiki.rickroll),
    path('stats/calc/<str:pbid>/<int:redirectPath>/', views.views_calc_stats, name='stats_calc_api'),
    path('data/', api.data),
    path('del_dev/<int:pbid>/', views.admin_reload_stats),
    path('api/', api.CalculatorAPI.as_view()),
    path('create_user_queue/', api.create_user_queue),
    path('validate_user_queue/<int:pk>/', api.validate_user_queue, name='validate_user_queue'), ## keep the name attribute for the reverse function in api.py
]

urlpatterns += staticfiles_urlpatterns()