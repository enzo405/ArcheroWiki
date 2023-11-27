from django.urls import path
from calculator import views
from calculator import api
from calculator import views_wiki
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from app.settings import DEV_MODE
from django.utils.translation import gettext_lazy as _


urlpatterns = [
    path('', views_wiki.menu, name='menu'),
    path('Terms-of-Use/', views_wiki.tos, name='tos'),
    path('changelog/', views_wiki.changelog, name='changelog'),
    path('calculator/', views.index_calc, name='calc'),
    path('calculator/show/<int:pbid>/', views.affiche_calc, name='affiche_calc'),
    path('calculator/create/', views.formulaire_calc, name='create_calc'),
    path('calculator/calc/', views.traitement_calc, name='traitement_calc'),
    path('calculator/index/', views.index_calc, name='index_calc'),
    path('calculator/update/<int:pbid>/', views.update_calc, name='update_calc'),
    path('calculator/updatecalc/<int:pbid>/', views.updatetraitement_calc, name='traitement_update_calc'),
    path('calculator/delete/<int:pbid>/', views.delete_user),
    path('calculator/duplicate/', views.duplicate_user, name='duplicate_user'),
    path('stats/calc/<int:pbid>/<int:redirectPath>/', views.views_calc_stats, name='stats_calc_api'),
    path('login/', views_wiki.login, name='login'),
    path('login/processing/<str:username_raw>/<str:id_raw>/', views_wiki.login_processing, name='login_process'),
    path('wiki/maze/', views_wiki.maze, name='maze'),
    path('wiki/menu/', views_wiki.wiki_menu, name='wiki'),
    path('wiki/menu/<str:article>/', views_wiki.wiki_menu, name='wiki'),
    path('wiki/item/', views_wiki.item_description, name='item_desc'),
    path('wiki/item/<str:item>/', views_wiki.item_description),
    path('wiki/heroes/', views_wiki.heros_description, name='heroes_desc'),
    path('wiki/heroes/<str:hero>/', views_wiki.heros_description),
    path('wiki/skill/', views_wiki.skill_description, name='skill'),
    path('wiki/skill/<str:skill>/', views_wiki.skill_description),
    path('wiki/damage-calculator/', views_wiki.damage, name='damage_calc'),
    path('wiki/damage-calculator/calc/<int:pbid>/', views_wiki.dmgCalc_processing, name='damage_calc_process'),
    path('wiki/damage-calculator/<int:pbid>/', views_wiki.damageCalc, name='damage_calc_calc'),
    path('wiki/google-sheet/', views_wiki.gsheetGrid, name='google_sheet'),
    path('wiki/upgrade/', views_wiki.upgrade_cost, name='upgrade_cost'),
    path('wiki/upgrade/<str:cost_type>/<int:lvl1>/<int:lvl2>/', views_wiki.upgrade_cost),
    path('wiki/upgrade/<str:cost_type>/<int:lvl1>/<int:lvl2>/<str:rank>/', views_wiki.upgrade_cost),
    path('wiki/promo-code/', views_wiki.promocode, name='promo_code'),
    path('wiki/theorycraft/', views_wiki.theorycraft, name='theorycraft'),
    path('wiki/<str:titleArticle>/', views_wiki.news, name='news'),
    path('data/', api.data),
    path('del_dev/<int:pbid>/', views.admin_reload_stats),
    path('api/calculator/', api.CalculatorAPI.as_view()),
    path('api/wiki/', api.WikiAPI.as_view()),
    path('create_user_queue/', api.create_user_queue),
    path('validate_user_queue/<int:pk>/', api.validate_user_queue, name='validate_user_queue'), ## keep the name attribute for the reverse function in api.py
    path('delete_cookie/<str:key>/<str:name_redirect>/', views_wiki.delete_cookie),
    path('logout/', views_wiki.delete_session),
]

if DEV_MODE:
    urlpatterns += [
        path('set_cookie/<str:key_cookie>/<str:value_cookie>/', views_wiki.set_cookie),
        path('set_session/<str:key_cookie>/<str:value_cookie>/', views_wiki.set_session),
        path('page_set/', views_wiki.page_set)
    ]

urlpatterns += staticfiles_urlpatterns()